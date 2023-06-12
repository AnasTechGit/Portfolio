import pandas as pd
import matplotlib.pyplot as plt

df_iFIT = pd.read_csv("iFIT_Data.csv")

# Cleaning data
df_iFIT = df_iFIT.dropna()

# Convert the 'Date' column to datetime format
df_iFIT['Date'] = pd.to_datetime(df_iFIT['Date'])

# Format the 'Date' column to JJ-MM-AA format
df_iFIT['Date'] = df_iFIT['Date'].dt.strftime('%d-%m-%y')

#Extraction data from each column
dates = df_iFIT['Date']
spm = df_iFIT['Strokes_Per_Min']

print("")
# Calculate the average strokes per minute
average_spm = df_iFIT['Strokes_Per_Min'].mean()
print ("Average strokes per minute :", average_spm)

# Create plot
fig, ax = plt.subplots()
ax.plot(dates, spm)
ax.set_xlabel('Date')
ax.set_ylabel('Strokes per minute')
ax.set_title('Strokes per minute over time')
plt.show()