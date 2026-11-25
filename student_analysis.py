import pandas as pd
import matplotlib.pyplot as plt

# load the data
df = pd.read_csv("StudentsPerformance.csv")
print(df.head())
print(df.shape)

subjects = ["math score", "reading score", "writing score"]

print("Missing values:")
print(df.isnull().sum())

for sub in subjects:
    df[sub] = df[sub].fillna(df[sub].mean())

print("Average marks:")
print(df[subjects].mean())

print("Highest marks:")
print(df[subjects].max())
print("Lowest marks:")
print(df[subjects].min())

df["average"] = df[subjects].mean(axis=1)

top = df["average"].idxmax()
low = df["average"].idxmin()
print("Top student row:", top, "->", round(df["average"][top], 2))
print("Lowest student row:", low, "->", round(df["average"][low], 2))

df["result"] = df["average"].apply(lambda x: "Pass" if x >= 40 else "Fail")
print(df["result"].value_counts())

print("Hardest subject:", df[subjects].mean().idxmin())
print(df.groupby("test preparation course")["average"].mean())
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

df[subjects].mean().plot(kind="bar", ax=axes[0, 0], title="Average Marks per Subject")
axes[0, 1].hist(df["average"], bins=10)
axes[0, 1].set_title("Student Average Marks")
df["result"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=axes[1, 0], title="Pass vs Fail")
df.groupby("test preparation course")["average"].mean().plot(kind="bar", ax=axes[1, 1], title="Test Prep vs Average")

plt.tight_layout()
plt.savefig("all_charts.png")

print("Done, charts saved.")
