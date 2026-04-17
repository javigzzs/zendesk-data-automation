import requests
import csv
import os

API_TOKEN = ""
BASE_URL = "https://api.getbase.com/v2"

CSV_PATH = os.path.expanduser(
    "~/Downloads/Borrado de tratos BESS 2-01-26.csv"
)

def borrar_trato(deal_id):
    url = f"{BASE_URL}/deals/{deal_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Accept": "application/json"
    }

    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print(f"Trato {deal_id} eliminado correctamente.")
    else:
        print(f"Error al borrar trato {deal_id}")
        print(f"Status: {response.status_code}")
        print(response.text)

def leer_ids_csv(ruta_csv):
    ids = []

    with open(ruta_csv, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        if "ID del trato" not in reader.fieldnames:
            print("El CSV no contiene la columna 'ID del trato'.")
            return ids

        for row in reader:
            deal_id = row["ID del trato"].strip()
            if deal_id.isdigit():
                ids.append(deal_id)

    return ids

if __name__ == "__main__":
    if not os.path.exists(CSV_PATH):
        print("No se encontró el archivo CSV en Downloads.")
        exit()

    deal_ids = leer_ids_csv(CSV_PATH)

    if not deal_ids:
        print("El CSV no contiene IDs de trato válidos.")
        exit()

    print(f"Se encontraron {len(deal_ids)} tratos para borrar:")
    print(", ".join(deal_ids))

    confirmacion = input(
        "¿Estás seguro de borrar TODOS estos tratos? "
        "Esto NO se puede deshacer. (SI / NO): "
    ).strip().upper()

    if confirmacion == "SI":
        for deal_id in deal_ids:
            borrar_trato(deal_id)
    else:
        print("Operación cancelada.")
