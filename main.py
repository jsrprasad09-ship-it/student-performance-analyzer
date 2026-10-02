import pandas as pd

pd.set_option("display.max_columns", None)

df = pd.read_csv("students.csv")

# Calculate average marks
df["Average"] = df[["Math", "Physics", "Chemistry"]].mean(axis=1).round(2)

# Find highest-performing student
top_student = df[df["Average"] == df["Average"].max()]

# Classify performance
def classify(average):
    if average >= 90:
        return "Excellent"
    elif average >= 80:
        return "Good"
    else:
        return "Needs Improvement"

df["Performance"] = df["Average"].apply(classify)

print("\nStudent Performance:")
print(df)

print("\nTop Student:")
print(top_student)
df.to_csv("results.csv", index=False)