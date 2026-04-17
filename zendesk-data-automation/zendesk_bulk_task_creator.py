import pandas as pd
import requests
import time

API_TOKEN = ""
BASE_URL = "https://api.getbase.com/v2"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

CSV_PATH = r"C:\Users\Javier Gonzalez\Downloads\PCEJ 4 tareas.csv"

OWNER_ID = ""
DUE_DATE = "2026-03-20"
TASK_CONTENT = "Realizar llamada de Seguimiento"

df = pd.read_csv(CSV_PATH)
df = df.dropna(subset=["contact_id"])
df["contact_id"] = df["contact_id"].astype(int)

first_contact = df["contact_id"].iloc[0]

print(f"\nProbando con contacto: {first_contact}")

url = f"{BASE_URL}/tasks"

payload = {
    "data": {
        "content": TASK_CONTENT,
        "due_date": DUE_DATE,
        "resource_type": "contact",
        "resource_id": int(first_contact),
        "owner_id": OWNER_ID
    }
}

response = requests.post(url, json=payload, headers=HEADERS)

print("Response:", response.status_code, response.text)

continuar = input("\n¿Continuar con TODOS los contactos? (si/no): ").strip().lower()

if continuar != "si":
    print("Proceso detenido.")
    exit()

print("\nCreando tareas para el resto...\n")

for contact_id in df["contact_id"].iloc[1:]:
    payload["data"]["resource_id"] = int(contact_id)

    response = requests.post(url, json=payload, headers=HEADERS)

    print(contact_id, response.status_code)

    time.sleep(0.2)

print("\nProceso terminado.")