"""
RECORD CHECK  -  my version
===========================

Name  : Luis Fernandes
Lane  : IT     
Date  : 04/11/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here
def parse_line(raw_line):
    """Cleans and converts a raw IT server record into a dictionary."""

    raw_line = raw_line.strip().lower()
    fields = raw_line.split(",")

    server = fields[0].strip()
    used = int(fields[1].split("=")[1].strip())
    total = int(fields[2].split("=")[1].strip())

    return {"server": server, "used": used, "total": total}

def status_of(used, total):
    """checks server usage and returns its status."""

    percent = (used / total) * 100

    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = [
    "  Srv-01 , used=87 , total=100 ",
    "SRV-02,USED=120,TOTAL=100",
    " srv-03 , Used=45 , Total=100 ",
    "  SRV-04, used=95,total=100 ",
    "Srv-05 , USED=70 , TOTAL=100 "
]


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

flagged = 0

for raw_record in raw_records:
    record = parse_line(raw_record)

    status = status_of(record["used"], record["total"])

    print(record)
    print("Status:", status)
    print()

    if status != "OK":
        flagged += 1

print("Total records:", len(raw_records))
print("Flagged records:", flagged)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
