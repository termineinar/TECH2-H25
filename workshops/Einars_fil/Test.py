#TASK 1: DATA PROCESSING

import pandas as pd
import matplotlib.pyplot as plt

#Step 1: Data preprocessing 
# 1. Read CSV
df = pd.read_csv('Users/einarstorvestre/Documents/Tech_2/TECH2-H25/workshops/Einars_fil/pokemon.csv')

# 2. Ages between 25-89
df = df[(df['age'] >= 25) & (df['age'] <= 89)]

# 3. Creating 'college' column (1 if educ = 3 or 4, else 0)
df['college'] = df['educ'].apply(lambda x: 1 if x in [3, 4] else 0)

# 4. Divide the networth by 1000 (thousands USD)
df['networth'] = df['networth'] / 1000

# 5. Print the number of observations
print("Number of observations in final sample:", len(df))

# Question 2: Average net worth by education 
education_labels = {
    1: 'No high school',
    2: 'High school',
    3: 'Some college',
    4: '4-year college or more'
}
# Compute average net worth by education using pandas
avg_networth = df.groupby('educ')['networth'].mean()

# Print results
print("\nAverage Net Worth by Education (thousands USD):")
for educ, avg in avg_networth.items():
    print(f"{education_labels[educ]}: {avg:.2f}")

# Bar chart (question 2)
plt.figure(figsize=(8,5))
plt.bar([education_labels[i] for i in avg_networth.index], avg_networth.values, color='skyblue', edgecolor='black')
plt.xlabel('Education Level')
plt.ylabel('Average Net Worth (thousands USD)')
plt.title('Average Net Worth by Education Level')
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

#Question 3: Average net worth by survey year 
# Using a loop
years = sorted(df['year'].unique())
avg_networth_by_year = {}

for y in years:
    avg_networth_by_year[y] = df[df['year'] == y]['networth'].mean()

# Print results
print("Average net worth by survey year (thousands USD):")
for y, avg in avg_networth_by_year.items():
    print(f"{y}: {avg:.2f}")

#  Line plot (question 3)
plt.figure(figsize=(9,5))
plt.plot(list(avg_networth_by_year.keys()), list(avg_networth_by_year.values()), marker='o')
plt.xlabel('Survey Year')
plt.ylabel('Average Net Worth (thousands USD)')
plt.title('Evolution of Average Net Worth (1989 - 2022)')
plt.grid(True)
plt.tight_layout()
plt.show()

#Question 4: Compute average net worth by year and college status 
years = sorted(df['year'].unique())
avg_non_college = []
avg_college = []

for y in years:
    avg_non_college.append(df[(df['year'] == y) & (df['college'] == 0)]['networth'].mean())
    avg_college.append(df[(df['year'] == y) & (df['college'] == 1)]['networth'].mean())


#Line plot (question 4)
plt.figure(figsize=(10,6))
plt.plot(years, avg_non_college, marker='o', label='Non-college (college=0)')
plt.plot(years, avg_college, marker='o', label='College (college=1)')
plt.xlabel('Survey Year')
plt.ylabel('Average Net Worth (thousands USD)')
plt.title('Average Net Worth Over Time by College Status (1989 - 2022)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()