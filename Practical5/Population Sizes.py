import matplotlib.pyplot as plt
#creat dictionary
population_data = {"UK": [57.11, 3.13, 1.91, 5.45],"Zhejiang neighbouring provinces": [65.77, 41.88, 45.28, 61.27, 85.15]}
#sort data
sorted_uk = sorted(population_data["UK"])
sorted_zhejiang = sorted(population_data["Zhejiang neighbouring provinces"])
#print sorted data
print("Sorted UK populations:", sorted_uk)
print("Sorted Zhejiang neighbouring provinces populations:", sorted_zhejiang)
#creat the first pie chart
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1) 
plt.pie(sorted_uk, labels=['England', 'Scotland', 'Wales', 'Northern Ireland'], autopct='%1.1f%%',shadow=False, startangle=140)
plt.title('Population Distribution in UK')
#creat another pie chart
plt.subplot(1, 2, 2)  
plt.pie(sorted_zhejiang, labels=['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu'],colors=['pink','lightpink','hotpink','mediumvioletred','lavenderblush'], autopct='%1.1f%%',shadow=False, startangle=140)
plt.title('Population Distribution in Zhejiang Neighbouring Provinces')
plt.show()
