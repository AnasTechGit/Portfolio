import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df_iFIT = pd.read_csv("iFIT_Data.csv")

# Cleaning data
df_iFIT = df_iFIT.dropna()

# Convert the 'Date' column to datetime format
df_iFIT['Date'] = pd.to_datetime(df_iFIT['Date'])

# Format the 'Date' column as day-month-year.
df_iFIT['Date'] = df_iFIT['Date'].dt.strftime('%d-%m-%Y')

print("")
# Calculate the total distance 
total_distance = df_iFIT["Distance(km)"].sum()
print(f"Total distance: {total_distance} km")

# Calculate the average distance 
average_distance = df_iFIT["Distance(km)"].mean()
print(f"Average distance: {average_distance} km")

# Display the variation in distance per week
distance_by_week = df_iFIT.groupby("Week")["Distance(km)"].mean()
distance_variation = distance_by_week.diff()
print("Variation in average distance per week:")
print(distance_variation)


# Calculate the average distance per day of the week
# distance_by_day = df_iFIT.groupby("Day_of_Week")["Distance(km)"].mean()
# print("Average distance per day of the week:")
# print(distance_by_day)

# Calculate the correlation between distance and other variables
correlations = df_iFIT[["Distance(km)", "Calories_Burned(cal)"]].corr()
print("Correlations between distance and Calories_Burned(cal):")
print(correlations)


print("###########################################################")
# Calculate the total distance per week
weekly_distance = df_iFIT.groupby("Week")["Distance(km)"].sum()
print(weekly_distance)

# Check if the total distance per week is greater than 20.5 km
for week, distance in weekly_distance.items():
    if distance > 20.5:
        print(f"For week {week}, I ran more than 20.5 km.")
    else:
        print(f"For week {week}, I didn't run more than 20.5 km.")


# Plot the distance trend over time
plt.plot(df_iFIT["Date"], df_iFIT["Distance(km)"])
plt.xlabel("Date")
plt.ylabel("Distance (km)")
plt.title("Distance Trend")
plt.xticks(rotation=45)
plt.show()