import matplotlib.pyplot as plt
#Create a dictionary
Programming_language_popularity = {'JavaScript':62.3,'HMTL':52.9,'Python':51,'SQL':51,'TypeScript':38.5}
#Print the dictionary
print(Programming_language_popularity)
#Extract keys and values into separate lists
languages = list(Programming_language_popularity.keys())
percentages = list(Programming_language_popularity.values())
#Create a bar chart
plt.bar(languages, percentages, color='blue')
#Set labels for the axes
plt.xlabel('Languages')
plt.ylabel('Users (percentage)')
#Set the chart title
plt.title('Programming Languages Popularity')
#Display the bar chart
plt.show()
#Define the input language variable
input_language = "JavaScript"
#Print the developer percentage for the specified language
print(f"The percentage of developers who use {input_language} is {Programming_language_popularity[input_language]}%.")
