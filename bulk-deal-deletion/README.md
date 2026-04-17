# Bulk Deal Deletion

This script deletes deals in bulk in Zendesk Sell using a CSV file with deal IDs.

## What it does

The script reads deal IDs from a CSV file, validates the input, shows the records that will be affected, and asks for explicit confirmation before deleting the deals through the Zendesk Sell API.

## Business use case

I built this to help clean CRM data in bulk when duplicate, invalid, or obsolete deals needed to be removed safely.

## Main features

- Reads deal IDs from a CSV file
- Validates that the required column exists
- Filters invalid or empty values
- Displays the deals that will be deleted
- Requires manual confirmation before execution
- Deletes deals through the Zendesk Sell API

## Technologies used

- Python
- requests
- csv
- os

## Expected input

A CSV file containing a column named:

```text
ID del trato
```

Configuration

Before running the script, update:
- API_TOKEN
- CSV_PATH

## Safety note

This operation cannot be undone.

The script includes a confirmation step before deletion to reduce operational risk.

## Notes

This script was originally built for internal operational use, so it relies on local configuration such as file paths and API credentials.

## Why I included this project

This project shows practical CRM maintenance, validation logic, and controlled execution for sensitive bulk data operations.
