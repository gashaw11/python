import pandas as pd

# Load the CSV into a DataFrame
df = pd.read_csv("budget.csv")

# Dictionary of updates: {Category: New Amount}
updates = {
    "Groceries": -60.00,
    "Transport": -35.00,
    "Shopping": -100.00
}

# Apply bulk updates where the Category matches
df.loc[df["Category"].isin(updates.keys()), "Amount"] = df["Category"].map(updates)

# Save back to CSV
df.to_csv("budget.csv", index=False)

print("Bulk update completed successfully!")
