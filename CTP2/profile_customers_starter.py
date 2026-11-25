"""CTP 2 - Exercise 1 STARTER: profile customers.csv with pandas.
Run from the 02_CTP2 folder:  python profile_customers_starter.py
Goal: measure at least 8 rules (2 per dimension) and copy the numbers into quality_scorecard_EX1.csv
"""
import datetime
from traceback import print_tb

import pandas as pd

df = pd.read_csv("../shopfast-kit/data/customers.csv", dtype=str)   # dtype=str: keep the raw text (e.g. 01300)
n = len(df)
print("Rows:", n)
print(df.head())

# --- Completeness: how many empty values per column? ---
print("\nEmpty values per column:\n", df.isna().sum())

# --- Uniqueness: is customer_id unique? ---
print("\nDuplicated customer_id rows:", df["customer_id"].duplicated(keep=False).sum())

# TODO 1 (Uniqueness): normalise email (strip + lower case) and count people registered twice
print("TODO 1")
df["email"] = df["email"].str.strip().str.lower()
f1 = df["email"].duplicated().sum()
print(f1)
print()

# TODO 2 (Validity): count emails that do not match the regex  ^[^@\s]+@[^@\s]+\.[a-zA-Z]{2,}$   (hint: .str.match)
print("TODO 2")
f2 = (~df["email"].str.match(r'^[^@\s]+@[^@\s]+\.[a-zA-Z]{2,}$')).sum()
print(f2)
print()

# TODO 3 (Consistency): list the distinct values of country with value_counts() - how many spellings for 4 countries?
print("TODO 3")
print(df["country"].value_counts())
print()
print(df["country"].nunique())
print()

# TODO 4 (Consistency): count signup_date values that are NOT in the format YYYY-MM-DD
print("TODO 4")
f4 = (~df["signup_date"].str.contains(r"\d{4}-\d{2}-\d{2}")).sum()
print(f4)
print()

# TODO 5 (Validity): loyalty_tier values outside bronze / silver / gold / platinum
print("TODO 5")
tiers = ["bronze","silver","gold","platinum"]
print(df["loyalty_tier"].value_counts())
f5 = (~df["loyalty_tier"].isin(tiers)).sum()
print(f5)
print()

# TODO 6 (Accuracy): birth_dates in the future or before 1906 (convert the ISO ones with pd.to_datetime)
print("TODO 6")
df["birth_date"] = pd.to_datetime(df["birth_date"],errors="coerce")
today=pd.Timestamp.today()
past=pd.Timestamp("1906-01-01")
f61=(df["birth_date"]>today).sum()
f62=(df["birth_date"]<past).sum()
print(f61)
print(f62)
print()


# TODO 7 (Validity): French postal codes that do not have 5 digits
print("TODO 7")
france = ["FR","France","fr","france","FRA"]
f7 = (df["country"].str.strip().isin(france) & (~df["postal_code"].str.contains(r"\d{5}"))).sum()
print(f7)
print()

# Bonus: compute score_pct = 100 * (1 - failing_rows / n) for each rule
print("pct 1 ",100 * (1-f1/n))
print("pct 2 ",100 * (1-f2/n))
print("pct 4 ",100 * (1-f4/n))
print("pct 5 ",100 * (1-f5/n))
print("pct 6.1 ", 100 * (1-f61/n))
print("pct 6.2 ", 100 * (1-f62/n))
print("pct 7 ",100 * (1-f7/n))
