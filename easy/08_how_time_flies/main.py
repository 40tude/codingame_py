# Your program must print formatted string with
# the number of full years
# and full months (if there are any greater than 0)
# and the total number of days between BEGIN and END dates in dd.mm.yyyy format


# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    os.chdir(Path(__file__).parent)
    sys.stdin = open("input.txt", "r")


# -----------------------------------------------------------------------------
from datetime import date
from dateutil.relativedelta import relativedelta

# dd, mm, yyyy = input().split(".")
# begin = date(int(yyyy), int(mm), int(dd))
# map - apply int to each element et retrounr un iterable, PAS une list
# list - convert iterable to list
# [::-1] - reverse list
# date(*args) - unpack list to arguments
begin = date(*list(map(int, input().split(".")))[::-1])
end = date(*list(map(int, input().split(".")))[::-1])

delta = relativedelta(end, begin)
total_days = (end - begin).days

msg = ""
msg += f"{delta.years} years, " if delta.years > 1 else ("1 year, " if delta.years == 1 else "")
msg += f"{delta.months} months, " if delta.months > 1 else ("1 month, " if delta.months == 1 else "")
msg += f"total {total_days} days" if total_days > 1 else ("total 1 day" if total_days == 1 else "total 0 days")
print(msg)


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()
