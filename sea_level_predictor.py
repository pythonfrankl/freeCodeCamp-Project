import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv("epa-sea-level.csv")

#散点图
plt.figure(figsize=(10,6))
plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'],label='Data Points')

#最佳拟合线
slope,intercept,r_value,p_value,std_err = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
line_eq = slope * df['Year'] + intercept
plt.plot(df['Year'], line_eq, label=f'Overall Trend: y={slope:.2f}x+{intercept:.2f}', color='red')


#2050海平面上升预测
year_2050 = 2050
line_eq_2050 =slope * year_2050 + intercept
plt.axvline(x=year_2050,color='red',linestyle='--',label=f'Prediction for 2050: {line_eq_2050:.2f} inches')

#仅使用2000年后数据算最佳拟合线
df_recent = df[df['Year'] >= 2000]
slope_recent,intercept_recent,r_value_recent,p_value_recent,
std_err_recent = linregress(df_recnet['Year'],df_recnet['CSIRO Adjusted Sea Level'])
line_eq_recent = slope_recent * df_recnet['Year'] + intercept_recent
plt.plot(df_recent['Year'], line_eq_recent, label=f'Trend since 2000: y={slope_recent:.2f}x+{intercept_recent:.2f}', color='blue')

# 预测 2050 年的海平面上升（基于 2000 年以后的趋势）
line_eq_recent_2050 = slope_recent * year_2050 + intercept_recent
plt.axvline(x=year_2050, color='blue', linestyle='--', label=f'Prediction for 2050 (since 2000): {line_eq_recent_2050:.2f} inches')

# 设置图表标题和轴标签
plt.title('Rise in Sea Level')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')

# 添加图例
plt.legend()

# 保存并返回图像
plt.savefig('sea_level_rise.png')
plt.close()
