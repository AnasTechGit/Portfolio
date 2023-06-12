import matplotlib.pyplot as plt
import pandas as pd

df_iFIT = pd.read_csv("iFIT_Data.csv")

# Convert the 'Date' column to datetime format
df_iFIT['Date'] = pd.to_datetime(df_iFIT['Date'])

#  Format the 'Date' column as day-month-year
df_iFIT['Date'] = df_iFIT['Date'].dt.strftime('%d-%m-%Y')

# Extract data
dates = df_iFIT['Date']
calories = df_iFIT['Calories_Burned(cal)']

# Descriptive statistics
mean_calories = calories.mean()
median_calories = calories.median()
std_calories = calories.std()

print("######################################################")
print("Descriptive statistics of Calories_Burned(cal)")
print("Average :", mean_calories)
print("Median :", median_calories)
print("Standard deviation :", std_calories)
print("######################################################")

# Calculating the total number of calories burned per week
weekly_calories = df_iFIT.groupby('Week')['Calories_Burned(cal)'].sum()

# Displaying the total number of calories burned per week
print("Total calories burned per week:")
print(weekly_calories)

# Calculating total calories burned(5 weeks)
total_calories = calories.sum()
print("Total calories burned :", total_calories)

print("##### Plot ####")
# Creating the histogram chart
plt.bar(dates, calories)
plt.xlabel('Date')
plt.ylabel('Calories_Burned(cal)')
plt.title('Calories Burned Per Date')

# Adjusting the y-axis range between 400 and 450"
plt.ylim(400, 450)

plt.show()