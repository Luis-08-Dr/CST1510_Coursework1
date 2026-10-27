"""
RECORD CHECK  -  my version
===========================

Name  : Luis Fernandes
Lane  : IT      
Date  : 21/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here
class Record:
    """Represent an IT server's storage usage and limit."""

    def __init__(self, label, value, limit):
        """Store the hostname, storage used, and storage limit."""
        self.label = label
        self.value = float(value)
        self.limit = float(limit)

    def status(self):
        """Return the storage status based on the percentage of the limit"""
        percentage = (self.value / self.limit) * 100

        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"

# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

def load_records(path):
    """Read IT storage records from a file and return Record objects."""
    records = []   

    with open(path, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue
            label, value, limit = line.split(",")

            record = Record(label, value, limit)
            records.append(record)
    return records

records = load_records("Week 05 - Classes and Objects/LAB/it_records.txt")


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)
over_limit_count = 0

for record in records:
    status = record.status()

    if status == "OVER LIMIT":
        over_limit_count += 1


    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f" Hostname  : {record.label}")
    print(f"  GB used  : {record.value:g}")
    print(f"  GB total  : {record.limit:g}")
    print(f"  Status  : {status}")


    print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
