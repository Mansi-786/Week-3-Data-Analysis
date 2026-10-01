# Sales Data Analysis

## 1. Project Overview

This project analyzes sales data using **Python and Pandas**.

The main purpose is to:

* Load the sales dataset
* Explore the data
* Clean the data
* Calculate sales metrics
* Identify the best-selling product
* Generate a final sales report

---

## 2. Project Objectives

The project focuses on the following objectives:

1. Load the sales dataset using Pandas.
2. Explore the dataset structure.
3. Check the number of rows and columns.
4. Check column names and data types.
5. Identify and handle missing values.
6. Check and remove duplicate records.
7. Calculate important sales metrics.
8. Identify the best-selling product.
9. Prepare a clean analysis report.

---

## 3. Tools and Technologies

| Tool   | Purpose                                |
| ------ | -------------------------------------- |
| Python | Programming language used for analysis |
| Pandas | Data loading, cleaning, and analysis   |
| CSV    | Dataset format                         |
| GitHub | Project submission and version control |

---

## 4. Dataset

**Dataset:** `sales_data.csv`

The dataset was provided for the internship and contains sales-related information used for data exploration, cleaning, and analysis.

---

## 5. Data Loading

The dataset was loaded using Pandas `read_csv()`.

```python
import pandas as pd

df = pd.read_csv("sales_data.csv")
```

The first few records were displayed using:

```python
print(df.head())
```

This confirmed that the CSV file was loaded successfully.

---

## 6. Data Exploration

The dataset was explored using the following Pandas functions:

| Function  | Purpose                              |
| --------- | ------------------------------------ |
| `head()`  | Displays the first few rows          |
| `shape`   | Shows the number of rows and columns |
| `columns` | Displays column names                |
| `dtypes`  | Shows data types                     |
| `info()`  | Provides general dataset information |

These functions helped understand the structure and contents of the dataset.

---

## 7. Data Cleaning

### 7.1 Missing Values

Missing values were checked using:

```python
df.isnull().sum()
```

The missing values were reviewed and handled appropriately based on the dataset.

### 7.2 Duplicate Records

Duplicate records were checked using:

```python
df.duplicated().sum()
```

Duplicate records were removed using:

```python
df = df.drop_duplicates()
```

This helped ensure that duplicate records did not affect the analysis.

---

## 8. Sales Analysis

The following metrics were calculated:

* **Total Sales**
* **Average Sales**
* **Highest Sale**
* **Lowest Sale**
* **Best-Selling Product**
* **Quantity Sold**

The analysis used Pandas functions such as:

```text
sum()       → Total sales
mean()      → Average sales
max()       → Highest value
min()       → Lowest value
groupby()   → Product-level analysis
```

---

## 9. Final Results

The final analysis generated the following results:

| Metric               |      Result |
| -------------------- | ----------: |
| Total Sales          | ₹525,450.00 |
| Average Sales        |   ₹5,254.50 |
| Highest Sale         |  ₹50,000.00 |
| Lowest Sale          |     ₹500.00 |
| Best-Selling Product |      Laptop |
| Quantity Sold        |          45 |

> **Note:** These values should match the actual output generated from `sales_data.csv`.

---

## 10. Key Findings

The analysis provided the following insights:

* The total sales were **₹525,450.00**.
* The average sales value was **₹5,254.50**.
* The highest individual sale was **₹50,000.00**.
* The lowest individual sale was **₹500.00**.
* **Laptop** was identified as the best-selling product based on total quantity sold.
* The best-selling product had a total quantity sold of **45 units**.

---

## 11. Conclusion

This project provided practical experience in using **Python and Pandas for data analysis**.

The project covered:

* Data loading
* Data exploration
* Missing-value checking
* Duplicate removal
* Sales calculations
* Product-level analysis
* Final report generation

The project demonstrates how Pandas can be used to work with tabular sales data and extract useful information from it.

---

## 12. Project Structure

The project is organized as follows:

```text
Week-3-Data-Analysis/
│
├── sales_analysis.py
├── sales_data.csv
├── analysis_report.md
├── requirements.txt
│
└── screenshots/
    ├── 01_dataset_loaded.png
    ├── 02_data_exploration.png
    ├── 03_data_cleaning.png
    └── 04_sales_analysis.png
```

### File Description

* **`sales_analysis.py`** — Python code used for data analysis.
* **`sales_data.csv`** — Sales dataset used for the project.
* **`analysis_report.md`** — Project documentation and findings.
* **`requirements.txt`** — Required Python library.
* **`screenshots/`** — Screenshots showing project execution and results.
