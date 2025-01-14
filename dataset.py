import pandas as pd

# Sample Dataset
data = {
    "text": [
        "Should I go to work today?",
        "Can I take a day off?",
        "Do I need a vacation?",
        "Should I buy a new phone?",
        "Is today a good day to relax?",
        "Should I start a new project?",
        "Should I invest in the stock market?"
    ],
    "category": ["Yes", "Yes", "Maybe", "Maybe", "No", "Yes", "Maybe"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save dataset to CSV for future use
df.to_csv("dataset.csv", index=False)
print("Dataset saved as dataset.csv")
