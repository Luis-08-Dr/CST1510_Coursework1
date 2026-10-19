"""
RECORD CHECK  -  my version
===========================

Name  :  Luis Fernandes
Lane  :  IT      
Date  :  26/09/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#
#    Remember: input() always gives back text.

label = input("Enter the server hostname: ")

first = float(input("Enter storage used in GB: "))
second = float(input("Enter total storage in GB: "))


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.

difference = second - first
percent = (first / second) * 100


# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

print()
print("=" * 44)
print(f"  RECORD CHECK  -  {label}")
print("=" * 44)

print(f"{'Used (GB)':<20}:{first:>12.2f}")
print(f"{'Total (GB)':<20}:{second:>12.2f}")
print(f"{'Free (GB)':<20}:{difference:>+12.2f}")
print(f"{'Percent Used':<20}:{percent:>11.2f} &")


print("=" * 44)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
