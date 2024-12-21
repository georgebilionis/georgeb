import pandas as pd

#1.1
df = pd.read_csv("global.csv", encoding="ISO-8859-1")


print(df)


#1.2
df['PM25_Value'] = df['FactValueNumeric']


print(df[['FactValueNumeric', 'PM25_Value']])


#1.3
average_pm25 = df.groupby('ParentLocation')['PM25_Value'].mean().reset_index()


average_pm25.rename(columns={'PM25_Value': 'Average_PM25'}, inplace=True)


df = df.merge(average_pm25, on='ParentLocation', how='left')


print(df[['Location', 'ParentLocation', 'PM25_Value', 'Average_PM25']])


#1.4
max_avg = average_pm25.loc[average_pm25['Average_PM25'].idxmax()]


print(f"The continent with the highest average PM2.5 is {max_avg['ParentLocation']} with an average value of {max_avg['Average_PM25']}.")
#It is not that surprising since its known that areas of high population and industrialization like Asia have a higher PM2.5 concentration


