# PDF Price Extractor

This script extracts SAP codes and prices from a PDF price list and converts them into a structured CSV file.

## What it does

The script opens a PDF document, extracts text page by page, identifies SAP codes and price values using regular expressions, and exports the results into a tabular dataset.

## Business use case

I built this to reduce manual extraction work from price lists and turn unstructured PDF data into a format ready for review, reporting, or further analysis.

## Main features

- Opens PDF files with `pdfplumber`
- Extracts text page by page
- Uses regular expressions to identify SAP codes
- Detects associated prices
- Exports results into a CSV file

## Technologies used

- Python
- pdfplumber
- pandas
- re

## Output

A CSV file with columns such as:

- `SAP`
- `Precio`

## Configuration

Before running the script, update:

- `ruta_pdf`
- output file path

## Notes

This script was originally built for local business use and assumes a specific PDF structure.

It may require small adjustments depending on the layout of the source document.

## Why I included this project

This project shows text extraction, pattern matching, and preparation of unstructured business data for analysis.
