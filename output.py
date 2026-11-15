import matplotlib.pyplot as plt


def show_chart(data):
    """將一筆支出畫成圓餅圖，扇形內顯示金額與百分比（v1：只處理單筆）。

    data: 一筆支出，格式為 [date, amount, category, note]
          所有欄位都是字串，note 可省略。
    """
    totals = {}
    amount = float(data[1])
    category = data[2]
    totals[category] = totals.get(category, 0) + amount

    total = sum(totals.values())

    def make_label(pct):
        value = total * pct / 100
        return f"{value:.0f}\n({pct:.1f}%)"

    plt.pie(totals.values(), labels=totals.keys(), autopct=make_label)
    plt.show()


if __name__ == "__main__":
    test_data = ["2026-11-10", "130", "food", "早安美之城"]
    show_chart(test_data)