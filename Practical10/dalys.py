import os # File/folder operations
import pandas as pd # Processing tabular data (DataFrame)
import matplotlib.pyplot as plt # Data visualization
import numpy as np # Numerical operations

# Import the required libraries
os.chdir("C:/Users/27661/Downloads") # Change working directory to the specified path
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv") # Read the CSV file into a DataFrame

# Display the "Year" column in the first 10 rows
print('The years of the first 10 rows:')
print(dalys_data.iloc[0:10, 2]) # Display the first 10 rows of the third column (index 2) of the DataFrame

# Find the data of Afghanistan in the 10th row (index starts from 0)
afghanistan_data = dalys_data[dalys_data["Entity"] == "Afghanistan"] # Filter the DataFrame to include only rows where the "Entity" column is "Afghanistan"
print("The year of the tenth row of Afghanistan：", afghanistan_data.iloc[9, 2]) # Display the year of the tenth row of the filtered DataFrame
print("The dalys of the tenth row of Afghanistan：", afghanistan_data.iloc[9, 3]) # Display the DALYs of the tenth row of the filtered DataFrame

# Use Boolean filtering to identify the DALYs of all countries in 1990s
dalys_1990 = dalys_data.loc[dalys_data["Year"] == 1990, "DALYs"] # Filter the DataFrame to include only rows where the "Year" column is 1990 and select the "DALYs" column
print("DALYs in 1990s：")
print(dalys_1990) # Display the DALYs in 1990s

# caculate the mean of DALYs for the UK and France
uk = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["DALYs", "Year"]] # Filter the DataFrame to include only rows where the "Entity" column is "United Kingdom" and select the "DALYs" and "Year" columns
fr = dalys_data.loc[dalys_data["Entity"] == "France", ["DALYs", "Year"]] # Filter the DataFrame to include only rows where the "Entity" column is "France" and select the "DALYs" and "Year" columns
uk_mean = uk["DALYs"].mean() # Calculate the mean of the "DALYs" column for the United Kingdom
fr_mean = fr["DALYs"].mean() # Calculate the mean of the "DALYs" column for France

# Print the mean of DALYs for the UK and France
if uk_mean > fr_mean:
    print("The average DALYs in the United Kingdom is higher than that in France")
else:
    print("The average DALYs in France is higher than or equal to that in the United Kingdom")

# Plot the DALYs of the UK and France
plt.figure('Plot-DALYs of the UK and France',figsize=(10, 5)) # Set the figure size
plt.plot(uk["Year"], uk["DALYs"], 'b+') # Plot the DALYs of the United Kingdom with blue plus markers
plt.xticks(uk["Year"], rotation=-90) # Set the x-ticks to the years of the United Kingdom and rotate them by -90 degrees
plt.xlabel("Year") # Set the x-axis label to "Year"
plt.ylabel("DALYs") # Set the y-axis label to "DALYs"
plt.title("DALYs Over Time in the United Kingdom") # Set the title of the plot to "DALYs Over Time in the United Kingdom"
plt.tight_layout() # Adjust the layout to fit the figure size
plt.show() # Show the plot

# address the question of 'Plot a boxplot of DALYs across countries in 1990.'
dalys_1990 = dalys_data[dalys_data["Year"] == 1990] # Filter the DataFrame to include only rows where the "Year" column is 1990
plt.figure('Boxplot-DALYs across countries in 1990s',figsize=(10, 5)) # Set the figure size
plt.boxplot(dalys_1990["DALYs"],labels=['Countries']) # Create a boxplot of the "DALYs" column for the year 1990 with horizontal orientation
plt.title("Boxplot of DALYs Across Countries in 1990") # Set the title of the plot to "Boxplot of DALYs Across Countries in 1990"
plt.ylabel("DALYs") # Set the y-axis label to "DALYs"
plt.grid(True) # Add a grid to the plot
plt.tight_layout() # Adjust the layout to fit the figure size
plt.show() # Show the plot

