import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#import
df = pd.csv.read_csv('medical_examination.csv')
#Create column in the df variable
df['overweight'] = df['weight'] / ((df['height']/100) ** 2) > 25
#Normalize data
df['cholesterol'] = df['cholestreol'].apply(lambda x: 0 if x ==1 else 1)
df['gluc'] = df['gluc'].apply(lambda x:0 if x == 1 else 1)
#Draw the Categorical Plot
def draw_cat_plot():
  df_cat = pd.melt(df,id_vars=['cardio'],value_vars=['cholesterol','gluc','smoke','alco','active','overweight'],var_name='category',value_name='value')
  df_cat = df_cat.groupby(['cardio','category','value']).size().unstack(fill_value=0)
  #Convert the data and create a chart
  fig = sns.catplot(data=df_cat.reset_index(),kind='bar',col='category',col_wrap=3,sharex=False,sharey=False,height=4,aspect=1)
  return fig
#get the figure and store it
fig = draw_cat_plot()

plt.show()
fig.savefig('catplot.png')
#draw the heat Map
def draw_heat_map():
  df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]
  corr = df_heat.corr()
  mask = np.triu(np.ones_like(corr,dtype=bool))
  fig,ax = plt.subplots(figsize=(11,9))
  sns.heatmap(corr,mask=mask,cmap='coolwarm',vmax=.3,center=0,annot=True,fmt='.2f',square=True,linewidths=.5,cbar_kws={"shrink": .5})
  return fig

fig = draw_heat_map()
plt.show()
fig.savefig('heatmap.png')

if __name__ == "__main__":
  print()
