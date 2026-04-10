import pandas as pd
import matplotlib.pyplot as plt

#データの読み込み
df_clean = pd.read_csv('online_retail_cleaned.csv')

#日付型の変換
df_clean['InvoiceDate'] = pd.to_datetime(df_clean['InvoiceDate'], dayfirst=True)



#----国別売上ランキング----

#国ごとに売り上げを集計
country_sales = df_clean.groupby('Country')['TotalSales'].sum().reset_index()

#国別売上ランキング（降順）
country_sales_ranking = country_sales.sort_values(by = 'TotalSales', ascending = False)

print("\n---国別売上ランキング---")
print(country_sales_ranking)

#売上の何%がイギリスか計算
total_revenue = country_sales_ranking['TotalSales'].sum()
uk_revenue = country_sales_ranking[country_sales_ranking['Country'] == 'United Kingdom'] ['TotalSales'].values[0]
uk_ratio = (uk_revenue / total_revenue) * 100

print (f"\nイギリスの売り上げシェア：{uk_ratio:.2f}%")

#グラフの作成
#グラフのサイズ
plt.figure(figsize=(12, 6))

#棒グラフ
#x軸に国名、y軸に売り上げ合計
graph = country_sales_ranking
plt.bar(graph['Country'], graph['TotalSales'], color='skyblue')

#タイトル・ラベル
plt.title('Revenue Ranking', fontsize=15)
plt.xlabel('Country')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)

#表示
plt.tight_layout()
plt.show()



#----月別売り上げ推移----

#日付から年月の列を作る
df_clean['YearMonth'] = df_clean['InvoiceDate'].dt.to_period('M')

#年月ごとに売り上げを合計する
monthly_sales = df_clean.groupby('YearMonth')['TotalSales'].sum().reset_index()

#年月を文字列に変換
monthly_sales['YearMonth'] = monthly_sales['YearMonth'].astype(str)

print("\n---月別売上の推移--")
print(monthly_sales)

#グラフ
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales['YearMonth'], monthly_sales['TotalSales'], marker='o', linestyle='-', color='orange')

plt.title('Monthly Sales Trend', fontsize=15)
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()



#----商品別売り上げランキング----

#商品別に売上金額を合計
product_sales = df_clean.groupby('Description')['TotalSales'].sum().reset_index()

#売上高い順に並べる
product_ranking = product_sales.sort_values(by='TotalSales', ascending=False)

#Top30のみにする（件数が多いため）
product_ranking_top30 = product_ranking.head(30)

#売上ランキング表示
print("\n---商品別売り上げ---")
print(product_ranking_top30)

#グラフ
plt.figure(figsize=(12, 8))
plt.barh(product_ranking_top30['Description'], product_ranking_top30['TotalSales'], color='teal')

plt.title('Sales Products Ranking Top30', fontsize=15)
plt.xlabel('Total Sales')
plt.ylabel('Description')
plt.gca().invert_yaxis()

plt.tight_layout()
plt.show()