# Deal Stage History Export

This script extracts deal stage history from Zendesk Sell and exports it into a structured CSV file.

## What it does

The script first retrieves all deal IDs from Zendesk Sell using pagination. Then, for each deal, it requests the stage history and stores the results in a flat dataset.

The output includes timestamps for stage transitions and can be used for further analysis in Excel, Power BI, or Python.

## Business use case

CRM systems often contain pipeline activity, but not always in a format that is easy to analyze directly.

I built this script to transform raw CRM activity into analysis-ready data that can be used to evaluate pipeline performance, measure time spent per stage, and identify bottlenecks in the sales funnel.

## Main features

- Retrieves all deal IDs using pagination
- Iterates through each deal automatically
- Extracts stage history per deal
- Builds a structured dataset
- Exports results to CSV

## Technologies used

- Python
- requests
- csv
- time

## Output

The script generates a CSV file named:

```text
historial_fases_zendesk.csv
```

With columns such as:
- deal_id
- stage_id
- stage_name
- entered_at
- exited_at

## Possible analytical uses
- Funnel conversion analysis
- Time spent per stage
- Sales pipeline bottleneck detection
- CRM process audits

## Configuration
Before running the script, update:
- ACCESS_TOKEN
## Notes

This script was originally built for internal analytical use and exports the results locally as a CSV file.

Why I included this project

This project is especially relevant for analytics roles because it converts operational CRM data into a dataset that can be directly used for reporting and performance analysis.
