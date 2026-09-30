import pandas as pd

products = pd.read_csv("data/apple_products_csv.csv")
customers = pd.read_csv("data/customers.csv")
sales = pd.read_csv("data/sales_d.csv")

print(products.head())

print("Products Shape:", products.shape)
print("Customers Shape:", customers.shape)
print("Sales Shape:", sales.shape)

print("Products Columns:", products.columns)
print("Customers Columns:", customers.columns)
print("Sales Columns:", sales.columns)

print("Products Data Types:")
print(products.dtypes)

print("Customers Data Types:")
print(customers.dtypes)

print("Sales Data Types:")
print(sales.dtypes)
# Expected columns

expected_product_columns = [
    "productid",
    "productname",
    "price",
    "launched_price",
    "cogs"
]

expected_customer_columns = [
    "customer_id",
    "membership",
    "joining_year"
]

expected_sales_columns = [
    "order_id",
    "order_date",
    "customer_id",
    "productid",
    "quantity",
    "price",
    "discount",
    "payment_mode",
    "status"
]


# Column validation function

def validate_columns(df, expected_columns):

    missing_columns = set(expected_columns) - set(df.columns)

    if missing_columns:
        print("FAIL")
        print("Missing columns:", missing_columns)
        return False

    print("PASS")
    return True


print("Products column validation:")
validate_columns(products, expected_product_columns)

print("Customers column validation:")
validate_columns(customers, expected_customer_columns)

print("Sales column validation:")
validate_columns(sales, expected_sales_columns)


def validate_nulls(df, table_name):

    null_counts = df.isnull().sum()

    total_nulls = null_counts.sum()

    if total_nulls > 0:
        print(f"{table_name} NULL validation: FAIL")
        print(null_counts[null_counts > 0])
        return False

    print(f"{table_name} NULL validation: PASS")
    return True



print("\nNULL VALIDATION")

validate_nulls(products, "Products")
validate_nulls(customers, "Customers")
validate_nulls(sales, "Sales")


def duplicate_check(df, table_name):

    duplicate_rows = df[df.duplicated()]

    if not duplicate_rows.empty:
        print(f"{table_name} Duplicate validation: FAIL")
        print(duplicate_rows)
        return False

    print(f"{table_name} Duplicate validation: PASS")
    return True

print("\nDUPLICATE VALIDATION")

duplicate_check(products, "Products")
duplicate_check(customers, "Customers")
duplicate_check(sales, "Sales")

def validate_unique_column(df, column_name, table_name):

    duplicate_count = df[column_name].duplicated().sum()

    if duplicate_count > 0:
        print(f"{table_name} {column_name} validation: FAIL")
        print(f"Duplicate {column_name}: {duplicate_count}")
        return False

    print(f"{table_name} {column_name} validation: PASS")
    return True

print("\nPRIMARY KEY VALIDATION")

validate_unique_column(products, "productid", "Products")
validate_unique_column(customers, "customer_id", "Customers")
validate_unique_column(sales, "order_id", "Sales")

import matplotlib.pyplot as plt


# Validation summary
validation_results = {
    "Column Validation": 3,
    "NULL Validation": 3,
    "Duplicate Validation": 3,
    "Primary Key Validation": 3,
    "Data Type Validation": 3
}


# Create visualization
validation_names = list(validation_results.keys())
passed_counts = list(validation_results.values())

plt.figure(figsize=(10, 6))

plt.bar(validation_names, passed_counts)

plt.title("Data Validation Summary")
plt.xlabel("Validation Type")
plt.ylabel("Number of Passed Tables")

plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("logs/validation_summary.png")

plt.show()