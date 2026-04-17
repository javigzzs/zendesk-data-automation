import pdfplumber
import re
import pandas as pd

ruta_pdf = "/Users/jgonzalez/Downloads/Lista de Precios Industronic 01.12.25_.pdf"

regex_sap = re.compile(r"\b\d{5,6}\b")

regex_precio = re.compile(r"\b\d{1,3}(?:,\d{3})*(?:\.\d+)?\b")

resultados = []

with pdfplumber.open(ruta_pdf) as pdf:
    for pagina in pdf.pages:  # Todas las páginas
        texto = pagina.extract_text() or ""
        for linea in texto.split("\n"):
            saps = [s for s in regex_sap.findall(linea) if int(s) > 10000]
            precios = [p for p in regex_precio.findall(linea) if ("," in p or len(p) <= 4)]
            for sap in saps:
                resultados.append((sap, precios[-1] if precios else ""))

df = pd.DataFrame(resultados, columns=["SAP", "Precio"])

#df.to_excel("/Users/jgonzalez/Downloads/SAP_Precio_23_10_25.xlsx", index=False)

df.to_csv("/Users/jgonzalez/Downloads/SAP_Precio_01.12_25.csv", index=False)
