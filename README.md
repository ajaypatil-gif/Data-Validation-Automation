# Data Validation Automation

A Python-based data validation project integrated with GitHub Actions to automatically validate CSV data whenever changes are pushed to the repository or a pull request is created.

The project performs data quality checks on Products, Customers, and Sales datasets and generates validation logs that can be stored as GitHub Actions artifacts.

---

## Project Overview

This project demonstrates how Data Quality and CI automation can be implemented using Python, Pandas, and GitHub Actions.

The pipeline reads three CSV datasets:

- Products
- Customers
- Sales

It performs multiple validation checks and executes automatically through GitHub Actions.

---

## Architecture

```text
                 Developer
                    |
                    | git push / Pull Request
                    v
              GitHub Repository
                    |
                    v
            GitHub Actions CI
                    |
          +---------+---------+
          |                   |
          v                   v
    Setup Python        Install Dependencies
          |                   |
          +---------+---------+
                    |
                    v
             Data Validation
                    |
        +-----------+-----------+
        |           |           |
        v           v           v
    Products    Customers     Sales
        |           |           |
        +-----------+-----------+
                    |
                    v
             Validation Logs
                    |
                    v
             GitHub Artifact
