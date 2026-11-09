"""
RECORD CHECK  -  my version
===========================

Name  : Luis Fernandes
Lane  : IT      
Date  : 28/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

df = pd.read_csv(r"C:\Users\luisf\OneDrive - Middlesex University\CST1510_Coursework1\Week 06 - Pandas\LAB\it_records.csv")


# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

df["percent"] = (df["used_gb"] / df["total_gb"]) * 100

# adding status column

df["status"] = df["percent"].apply(
    lambda x: "OVER LIMIT" if x >= 100 else "WARNING" if x >= 90 else "OK"
)


# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.

print(df)

print("\nRecords needing attention:")
print(df[df["status"] != "OK"])

print("\nCount per status:")
print(df.groupby("status").size())

df.to_csv("it_records_report.csv", index=False)

# Bar Chart
df["status"].value_counts().plot(kind="bar")

plt.title("IT Storage Status Counts")
plt.xlabel("Status")
plt.ylabel("Number of Servers")
plt.tight_layout()

plt.savefig("it_satus_counts.png")
plt.show



# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
