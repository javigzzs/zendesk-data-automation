# Zendesk Data Automation

This repository contains a collection of Python scripts I built to automate CRM workflows and transform business data into analysis-ready datasets.

The focus is on practical, real-world use cases using Zendesk Sell, including bulk operations, data cleaning, and extracting structured information for analysis.

---

## 🚀 Projects Included

### 1. Bulk Task Creator
Creates tasks in bulk in Zendesk Sell from a CSV file with contact IDs.

**What it does:**
- Reads contact IDs from a CSV file  
- Creates tasks via the Zendesk Sell API  
- Includes a validation step before executing the full batch  

**Business value:**
Reduces repetitive manual work and enables faster execution of follow-up campaigns at scale.

---

### 2. Bulk Deal Deletion
Deletes deals in bulk using a CSV file, with validation and confirmation before execution.

**What it does:**
- Reads deal IDs from a CSV  
- Validates input data  
- Displays records before deletion  
- Requires manual confirmation  

**Business value:**
Ensures safe and controlled cleanup of CRM data, reducing duplicates and maintaining data quality.

---

### 3. Deal Stage History Export
Extracts deal stage history from Zendesk Sell and builds a structured dataset with timestamps for each stage transition.

**What it does:**
- Retrieves all deals using pagination  
- Extracts stage history per deal  
- Builds a structured dataset  
- Exports results to CSV  

**Business value:**
Transforms raw CRM activity into analysis-ready data to evaluate pipeline performance, measure time per stage, and identify bottlenecks in the sales funnel.

---

### 4. PDF Price Extractor
Extracts SAP codes and prices from PDF documents and converts them into a structured dataset.

**What it does:**
- Reads PDF files using `pdfplumber`  
- Extracts text page by page  
- Identifies product codes and prices using regex  
- Outputs structured data to CSV  

**Business value:**
Automates manual data extraction from documents, enabling faster reporting and reducing human error.

---

## 🧰 Tech Stack

- Python  
- pandas  
- requests  
- pdfplumber  
- CSV / file processing  

---

## ⚙️ How to Use

These scripts were originally built for internal use, so some configurations are local.

To run them, you will need to:

1. Add your API token for Zendesk Sell  
2. Update file paths (CSV or PDF inputs)  
3. Install required dependencies  

Example:

```bash
pip install pandas requests pdfplumber
```

---
## ⚠️ Disclaimer

These scripts are shared as examples of real-world automation and data workflows.

They may require adjustments depending on:

Zendesk Sell configuration
Custom fields
Data structure

Parts of the implementation were assisted by AI tools and later adapted for practical business use.

## 🎯 Purpose of this Repository

I created this repository to showcase how I approach:

Automating repetitive business processes
Working with APIs and structured data
Cleaning and transforming data for analysis
Building practical solutions that improve efficiency
## 📌 Final Note

This is not a theoretical or academic project.

All scripts were built to solve real operational problems and support decision-making through better data availability.
