# SE_Assignment1 記帳軟體

以 Python 撰寫的簡易記帳工具：在終端機輸入支出，程式會依類別即時繪製圓餅圖。

## 環境需求
- Python 3.9 以上
- matplotlib

## 安裝說明
```
git clone https://github.com/Neilo428/Se_HW01.git
cd Se_HW01
pip install matplotlib
```

## 執行程式
```
python input.py
```
每輸入一筆支出，圓餅圖就會在同一個視窗即時更新；輸入 `q` 結束後，圖表視窗會保留，關閉視窗即結束程式。

也可以單獨執行 `python output.py`，用內建的測試資料顯示圓餅圖。

## input.py

### 輸入範例
```
Input format: date, amount, category, note (or Enter 'q' to quit)
Example: 2026-11-15,130,food,breakfast
Category:{'tran', 'ent', 'food', 'oth'}
> 2026-11-15,130,food,breakfast
```

### 輸入格式
- 日期 date：YYYY-MM-DD
- 金額 amount：非 0 正整數
- 項目 category：
    - tran：交通 transport
    - ent：娛樂 entertainment
    - food：食物 food
    - oth：其他 other
- 備註 note：可省略

> 各欄位之間需用逗號隔開

### 錯誤輸入
以下情況會顯示錯誤訊息，並略過該筆資料：
- 日期、金額、項目不符合格式
- 未用逗號隔開
- 缺少日期、金額、項目

## output.py

- `show_chart(data)`：根據讀進的資料繪製圓餅圖，每次呼叫都會即時更新同一個視窗
- `keep_chart()`：輸入結束後，讓圖表視窗保持開啟
- 圓餅圖會顯示類別全名、金額、百分比，以及標題總金額

### 輸入以下資料後的結果
```
2026-11-15,130,food
2026-11-15,540,ent
2026-11-15,540,oth
```

![圓餅圖範例](images/piechart.png)

## Demo 影片
[觀看 Demo 影片](https://youtu.be/ZrfomheRtlI)

## 分工
- Ernie777：`input.py`（支出輸入與防呆檢查）
- Neilo428：`output.py`（圓餅圖繪製與即時更新）