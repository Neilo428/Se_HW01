import matplotlib.pyplot as plt

CATEGORY_NAMES = {
    "food": "Food",
    "tran": "Transport",
    "ent": "Entertainment",
    "oth": "Other",
}


def show_chart(data):
    """依類別加總多筆支出，在同一個視窗即時更新圓餅圖（v3）。

    data: 多筆支出，每筆格式為 [date, amount, category, note]
          所有欄位都是字串，note 可省略。
          資料格式的檢查由 input.py 負責。
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

    labels = [CATEGORY_NAMES.get(c, c) for c in totals]
    # 只有一個類別時，把文字放在圓心
    pct_distance = 0 if len(totals) == 1 else 0.6

    plt.ion()                       # 互動模式：畫圖不會卡住程式
    plt.figure("Expense Chart")     # 固定使用同一個視窗
    plt.clf()                       # 清掉上一次的圖
    plt.pie(totals.values(), labels=labels,
            autopct=make_label, pctdistance=pct_distance)
    plt.title(f"Expenses by Category (Total: {total:.0f})")
    plt.pause(0.1)                  # 讓視窗更新畫面


def keep_chart():
    """輸入結束後呼叫，讓圖表視窗保持開啟，直到使用者關閉。"""
    if plt.get_fignums():
        plt.ioff()
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
    keep_chart()