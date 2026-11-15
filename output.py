import matplotlib.pyplot as plt


def show_chart(data):
    """依類別加總多筆支出，畫成圓餅圖，扇形內顯示金額與百分比（v2）。

    data: 多筆支出，每筆格式為 [date, amount, category, note]
          所有欄位都是字串，note 可省略。
    """
    totals = {}
    for record in data:
        amount = float(record[1])
        category = record[2]
        totals[category] = totals.get(category, 0) + amount

    total = sum(totals.values())

    def make_label(pct):
        value = total * pct / 100
        return f"{value:.0f}\n({pct:.1f}%)"

    plt.pie(totals.values(), labels=totals.keys(), autopct=make_label)
    plt.show()


if __name__ == "__main__":
    test_data = [
        ["2026-11-10", "130", "food", "早安美之城"],
        ["2026-11-10", "30", "tran", "公車"],
        ["2026-11-11", "250", "ent", "電影"],
        ["2026-11-11", "95", "food"],
        ["2026-11-12", "60", "tran"],
        ["2026-11-13", "450", "oth", "文具"],
    ]
    show_chart(test_data)