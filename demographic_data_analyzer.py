import pandas as pd
df = pd.read_csv('https://archive.ics.uci.edu/ml')
#Problem 1
race_counts = df['race'].value_counts()
#P2
average_age_men = df[df['sex'] == 'Male']['age'].mean()
#P3
bachelors_Percentage = (df['education'] == 'Bachelors').mean() * 100
#P4
advanced_education = df['education'].isin(['Bachelors','Masters','Doctorate'])
advanced_education_over_50k = ((df['salary'] == '>50K') & advanced_education.mean()) * 100
#P5
non_advanced_education = ~advanced_education
non_advanced_education_over_50k = ((df['salary'] == '>50k')&non_advanced_education).mean() * 100
#P6
min_hours_per_week = df['hour-per-week'].min()
#P7
min_hours_over_50k = ((df['hour-per-week'] == min_hours_per_week) & (df['salary'] == '>50k')).mean() * 100
#P8
country_over_50k = df.groupby('native-country')['salary'].apply(lambda x:(x == '>50K')).mean().sort_values(ascending=False)
country_with_highest_50k = country_over_50k.idxmax()
highest_percentage = country_over_50k.max() * 100
#P9
india_earn_over_50k = df[(df['native-country'] == 'India') & (df['salary'] == '>50k')]
most_popular_occupation = india_earn_over_50k['occupation'].mode()[0]

#result
average_age_men = round(average_age_men,1)
bachelors_Percentage = round(bachelors_Percentage,1)
advanced_education_over_50k = round(advanced_education_over_50k,1)
non_advanced_education_over_50k = round(non_advanced_education_over_50k,1)
min_hours_over_50k = round(min_hours_over_50k,1)
highest_percentage = round(highest_percentage,1)

#输出结果
print(race_counts)
print(f"Average age of men: {average_age_men}")
print(f"Percentage with Bachelor's degree: {bachelors_percentage}%")
print(f"Percentage of advanced education earning >50K: {advanced_education_over_50k}%")
print(f"Percentage of non-advanced education earning >50K: {non_advanced_education_over_50k}%")
print(f"Minimum hours per week: {min_hours_per_week}")
print(f"Percentage earning >50K with minimum hours: {min_hours_over_50k}%")
print(f"Country with highest >50K percentage: {country_with_highest_50k} ({highest_percentage}%)")
print(f"Most popular occupation for >50K earners in India: {most_popular_occupation}")
