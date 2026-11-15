from output import show_chart

CATEGORIES = {"food", "tran", "ent", "oth"}


print("Input format: date, amount, category, note")
print(f"Category:{CATEGORIES}")

data = input("> ").strip().split(",",3)
#print(f"added：{data}")

show_chart(data)

