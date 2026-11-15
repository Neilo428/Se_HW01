from output import show_chart, keep_chart
from datetime import datetime

CATEGORIES = {"food", "tran", "ent", "oth"}
data = []

def check(entry):
    
    if len(entry) < 3:
        print("INPUT ERROR")
        return False

    date_str, amount_str, category = entry[0], entry[1], entry[2].lower()
    note = entry[3] if len(entry) == 4 else ""

    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("DATE ERROR")
        return False

    if not amount_str.isdigit():
        print("AMOUNT ERROR")
        return False

    if category not in CATEGORIES:
        print("CATEGORY ERROR")
        return False

    return True

print("Input format: date, amount, category, note (or Enter 'q' to quit)")
print(f"Category:{CATEGORIES}")
while True:
    entry = input("> ").strip().split(",",3)
    
    if entry[0].lower() == "q":
        print("Exit")
        break

    if not check(entry):
        continue

    data.append(entry)
    #print(f"added：{entry}")
    #print(f"data：{data}")

    show_chart(data)
keep_chart()  