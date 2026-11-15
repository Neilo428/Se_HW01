from output import show_chart

CATEGORIES = {"food", "tran", "ent", "oth"}
data = []

print("Input format: date, amount, category, note (or Enter 'q' to quit)")
print(f"Category:{CATEGORIES}")
while True:
    entry = input("> ").strip().split(",",3)
    
    if entry[0].lower() == "q":
        print("Exit")
        break

    data.append(entry)
    #print(f"added：{entry}")
    #print(f"data：{data}")

    show_chart(data)
