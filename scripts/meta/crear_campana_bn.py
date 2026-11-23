#!/usr/bin/env python3
"""Crea la campaña Black November de SIN PENA en Meta, TODO en estado PAUSED.

No crea anuncios (se agregan cuando los creativos estén listos) y nunca activa nada.
Los IDs van por variables de entorno porque el repo es público:

  META_AD_ACCOUNT_ID   (sin "act_")
  META_PIXEL_ID
  META_TOKEN           (opcional: si el proxy de la sesión ya inyecta el token, no hace falta)
  GRAPH_VERSION        (opcional, por defecto v23.0)

Uso:
  python3 scripts/meta/crear_campana_bn.py            # solo muestra lo que crearía
  python3 scripts/meta/crear_campana_bn.py --crear    # lo crea, pausado
"""
import json, os, sys, urllib.parse, urllib.request

VERSION = os.environ.get("GRAPH_VERSION", "v23.0")
BASE = f"https://graph.facebook.com/{VERSION}"
ACCOUNT = os.environ.get("META_AD_ACCOUNT_ID", "").replace("act_", "")
PIXEL = os.environ.get("META_PIXEL_ID", "")
TOKEN = os.environ.get("META_TOKEN", "")

PRESUPUESTO_DIARIO_COP = 15000
FIN = "2026-11-30T23:59:00-0500"  # 30 nov 23:59 Bogotá

CAMPANA = {
    "name": "SIN PENA · Ventas · Black November 2026",
    "objective": "OUTCOME_SALES",
    "status": "PAUSED",
    "special_ad_categories": [],
    "is_adset_budget_sharing_enabled": False,
}

def conjunto(campaign_id, presupuesto_api):
    return {
        "name": "BN · CO+MX · 25-55 · Inicio de pago",
        "campaign_id": campaign_id,
        "status": "PAUSED",
        "daily_budget": presupuesto_api,
        "billing_event": "IMPRESSIONS",
        "optimization_goal": "OFFSITE_CONVERSIONS",
        "bid_strategy": "LOWEST_COST_WITHOUT_CAP",
        "promoted_object": {"pixel_id": PIXEL, "custom_event_type": "INITIATED_CHECKOUT"},
        "targeting": {
            "geo_locations": {"countries": ["CO", "MX"]},
            "age_min": 25,
            "age_max": 55,
            "targeting_automation": {"advantage_audience": 0},
        },
        "end_time": FIN,
    }

def llamar(metodo, ruta, datos=None):
    url = f"{BASE}/{ruta}"
    headers = {"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}
    cuerpo = None
    if datos is not None:
        cuerpo = urllib.parse.urlencode(
            {k: json.dumps(v) if isinstance(v, (dict, list, bool)) else v for k, v in datos.items()}
        ).encode()
    req = urllib.request.Request(url, data=cuerpo, method=metodo, headers=headers)
    try:
        with urllib.request.urlopen(req) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"Error {e.code} en {ruta}: {e.read().decode()}")

def main():
    crear = "--crear" in sys.argv
    if not ACCOUNT or not PIXEL:
        sys.exit("Faltan META_AD_ACCOUNT_ID y/o META_PIXEL_ID.")

    cuenta = llamar("GET", f"act_{ACCOUNT}?fields=name,currency,timezone_name,account_status")
    print("Cuenta:", json.dumps(cuenta, ensure_ascii=False))
    if cuenta.get("currency") != "COP":
        sys.exit(f"La cuenta está en {cuenta.get('currency')}, no en COP: revisar el presupuesto antes de seguir.")
    # Meta expresa el presupuesto en la unidad mínima de la moneda; se valida leyendo
    # el valor creado de vuelta (abajo) antes de dar nada por bueno.
    presupuesto_api = PRESUPUESTO_DIARIO_COP

    print("\nCampaña:", json.dumps(CAMPANA, ensure_ascii=False, indent=2))
    print("\nConjunto:", json.dumps(conjunto("<id de la campaña>", presupuesto_api), ensure_ascii=False, indent=2))
    if not crear:
        print("\nModo prueba: no se creó nada. Usa --crear para crearlo PAUSADO.")
        return

    camp = llamar("POST", f"act_{ACCOUNT}/campaigns", CAMPANA)
    print("Campaña creada:", camp)
    cs = llamar("POST", f"act_{ACCOUNT}/adsets", conjunto(camp["id"], presupuesto_api))
    print("Conjunto creado:", cs)

    v = llamar("GET", f"{cs['id']}?fields=name,status,effective_status,daily_budget,end_time")
    c = llamar("GET", f"{camp['id']}?fields=name,status,effective_status,objective")
    print("\nVerificación:\n", json.dumps(c, ensure_ascii=False), "\n", json.dumps(v, ensure_ascii=False))
    if c.get("status") != "PAUSED" or v.get("status") != "PAUSED":
        sys.exit("ATENCIÓN: algo no quedó en PAUSED. Revisar ya en el Administrador de anuncios.")

if __name__ == "__main__":
    main()
