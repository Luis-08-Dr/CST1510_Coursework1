"""
RECORD CHECK  -  my version
===========================

Name  : Luis Fernandes
Lane  : IT      
Date  :14/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(value, limit):
    """Calculates remaining storage, percentage and status."""

    difference = limit - value
    percent = (value / limit) * 100

    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"

    return difference, percent, status

# Printing the report.

def print_report(label, value, limit, difference, percent, status):

    print("------------------------------")
    print("Hostname:", label)
    print("GB Used:", value)
    print("GB Total:", limit)
    print("Remaining GB:", difference)
    print("Usage:", round(percent, 2), "%")
    print("Status:", status)

    #Loads from a text file

def load_records(path):
    """Reading the computer records from a text file."""

    records = []

    with open(path, "r") as file:
        for line in file:
            parts = line.strip().split(",")

            label = parts[0]
            value = int(parts[1])
            limit = int(parts[2])

            records.append({
                "label": label,
                "value": value,
                "limit": limit
            })

    return records


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

# load records from records.txt
records = load_records('Week 04 - Lists, Dictionaries and Files/LAB/records.txt')


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here

# check and print each computer record
for record in records:

    difference, percent, status = check_record(
        record["value"], record["limit"]
    )

    print_report(
        record["label"],
        record["value"],
        record["limit"],
        difference,
        percent,
        status
    )


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
