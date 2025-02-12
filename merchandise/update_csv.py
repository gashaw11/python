import pandas as pd

# Load the CSV into a DataFrame
df = pd.read_csv("merchandise.csv")

# Dictionary of updates: {Category: New Amount}
updates = {
    "pen": -60.00,
    "tshirt": -35.00,
    "laptop": -100.00
}

# Apply bulk updates where the Category matches
df.loc[df["Item"].isin(updates.keys()), "Quantity"] = df["Item"].map(updates)

# Save back to CSV
df.to_csv("merchandise.csv", index=False)

print("Bulk update completed successfully!")
