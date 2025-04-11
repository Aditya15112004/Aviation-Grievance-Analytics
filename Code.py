'''
Name: Aditya Kumar
Sec: K23EV
Group: 02
Roll No.: 53
'''


#1. Bar Chart – Top 10 Airlines with Most Grievances
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("aviation-grievance-date.csv")

airline_data = df.groupby('subcategory')['totalReceived'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 5))
airline_data.plot(kind='bar', color='skyblue')
plt.title("Top 10 Airlines with Most Grievances")
plt.xlabel("Airline")
plt.ylabel("Total Grievances")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#2. Pie Chart – Grievances by Type
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("aviation-grievance-date.csv")

type_data = df.groupby('type')['totalReceived'].sum().sort_values(ascending=False).head(10)  # Top 10 types

plt.figure(figsize=(8, 8))
plt.pie(type_data, labels=type_data.index, autopct='%1.1f%%', startangle=140)
plt.title("Grievances by Type (Top 10)")
plt.axis('equal')
plt.show()


#3. Scatter Plot – Total Grievances vs With Feedback
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("aviation-grievance-date.csv")

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='totalReceived', y='grievancesWithFeedback', hue='category')
plt.title("Total Grievances vs Feedback Received")
plt.xlabel("Total Grievances")
plt.ylabel("With Feedback")
plt.show()


#4. Seaborn Count Plot – Complaint Types Frequency
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("aviation-grievance-date.csv")

top_types = df['type'].value_counts().nlargest(10).index

plt.figure(figsize=(10, 5))
sns.countplot(data=df[df['type'].isin(top_types)], y='type', order=top_types)
plt.title("Top Complaint Types")
plt.xlabel("Count")
plt.ylabel("Type")
plt.tight_layout()
plt.show()


#5. Line Plot – Escalated vs Non-Escalated
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("aviation-grievance-date.csv")

# Calculate total active grievances and get top 10 subcategories
df['totalActive'] = df['activeGrievancesWithEscalation'] + df['activeGrievancesWithoutEscalation']
top_df = df.sort_values(by='totalActive', ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.plot(top_df['subcategory'], top_df['activeGrievancesWithEscalation'], label='With Escalation', color='red', marker='o')
plt.plot(top_df['subcategory'], top_df['activeGrievancesWithoutEscalation'], label='Without Escalation', color='green', marker='o')
plt.title("Escalated vs Non-Escalated Grievances (Top 10 Subcategories)")
plt.xlabel("Subcategory")
plt.ylabel("Active Grievances")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()









































































































































































