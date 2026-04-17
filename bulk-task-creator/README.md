# Bulk Task Creator

This script creates tasks in bulk in Zendesk Sell using a CSV file with contact IDs.

## What it does

Instead of creating follow-up tasks one by one inside the CRM, this script reads a list of contact IDs from a CSV file and creates the same task for each contact through the Zendesk Sell API.

It also tests the first contact before continuing and asks for manual confirmation before running the full batch.

## Business use case

I built this to reduce repetitive manual work inside the CRM and speed up follow-up execution for large contact lists.

## Main features

- Reads contact IDs from a CSV file
- Removes missing values before processing
- Tests the first contact before the full run
- Requires manual confirmation before continuing
- Creates tasks through the Zendesk Sell API

## Technologies used

- Python
- pandas
- requests

## Expected input

A CSV file containing a `contact_id` column.

Example:

```csv
contact_id
123456789
987654321
456789123
