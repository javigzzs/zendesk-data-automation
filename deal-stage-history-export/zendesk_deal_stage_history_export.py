import requests
import csv
import time


ACCESS_TOKEN = ""

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Accept": "application/json"
}

BASE_URL = "https://api.getbase.com/v2"


all_deals = []
page = 1

print("Descargando lista de tratos...")

while True:
    url = f"{BASE_URL}/deals?page={page}"
    r = requests.get(url, headers=headers)
    data = r.json()

    if "items" not in data or len(data["items"]) == 0:
        break

    for item in data["items"]:
        deal_id = item["data"]["id"]
        all_deals.append(deal_id)

    page += 1
    time.sleep(0.2)

print(f"Total de tratos encontrados: {len(all_deals)}")

rows = []

print("Descargando historial de etapas...")

for deal_id in all_deals:
    url = f"{BASE_URL}/deals/{deal_id}/stages"
    r = requests.get(url, headers=headers)
    data = r.json()

    if "items" in data:
        for item in data["items"]:
            stage = item["data"]
            rows.append([
                deal_id,
                stage.get("stage_id"),
                stage.get("stage_name"),
                stage.get("entered_at"),
                stage.get("exited_at")
            ])

    time.sleep(0.1)


with open("historial_fases_zendesk.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["deal_id", "stage_id", "stage_name", "entered_at", "exited_at"])
    writer.writerows(rows)

print("✔ Archivo generado: historial_fases_zendesk.csv")
