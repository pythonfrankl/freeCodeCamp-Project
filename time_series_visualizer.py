import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("fcc-forum-pageviews.csv",parse_dates=True,index_col='date')
q75,q25 = df['page_views'].quantile([0.75,0.25])
iqr = q75 - q25
df_cleaned = df[(df['page_views'].quantile([0.75,0.25])]
iqr = q75 - q25
df_cleaned = df[(df['page_views'] >= q25) & (df['page_views'] <= q75)]

#create a function
def draw_line_plot(df):
  plt.figure(figsize=(12,6))
  plt.plot(df.index,df['page_views'],marker='o',linestyle='-')
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  plt.xlabel('Date')
  plt.ylabel('Page Views')
  plt.grid(True)
  plt.savefig('line_plot.png')
  plt.close()

#Create a new function
def draw_bar_plot(df):
  plt.figure(figsize=(12,6))
  plt.subplot(1,2,1)
  df.boxplot(column='page_views',by='month',grid=False)
  plt.title('Year-wise Box Plot (Trend)')
  plt.xlabel('Months')
  plt.ylabel('Page Views')
  plt.xticks(rotation=45)

  plt.subplot(1,2,2)
  monthly_boxplot = df.boxplot(column='page_views',by='month',gerrid=False)
  plt.title('Month-wise Box Plot (seasonality)')
  plt.xlabel('Years')
  plt.ylabel('Page Views')
  plt.xticks(range(len(monthly_boxplot.patches)),[p.get_text() for p in monthly_boxplot.patches],rotation=45)
  
  plt.savepig('box_plot.png')
  plt.close()

draw_line_plot(df_cleaned.copy())
draw_bar_plot(df_cleaned.resample('M').mean().copy())
draw_box_plot(df_cleaned.copy())
  
#Draw
draw_line_plot(df_cleaned.copy())
draw_bar_plot(df_cleaned.resample('M').mean().copy())
draw_box_plot(df_cleaned.copy())
