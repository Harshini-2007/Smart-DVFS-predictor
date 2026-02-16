import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load dataset
d = pd.read_csv("dvfs_dataset.csv")



# Create Next_Load column
d["Next_Load"] = d["CPU_Load_Percent"].shift(-1)

# Remove last row (NaN)
d = d.dropna()

# Define features and target AFTER dropna
X = d[["CPU_Load_Percent"]]
y = d["Next_Load"]

# Train-test split (no shuffle because time series)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predicted_load = model.predict(X_test)

# Create comparison table
'''
result = pd.DataFrame({
    "Actual_Next_Load": y_test.values,
    "Predicted_Next_Load": predicted_load
})

print("\nComparison Table:")
print(result)
'''
# Take only test portion from dataframe
test_data = d.iloc[-len(X_test):].copy()

# Add predicted load column
test_data["Predicted_Load"] = predicted_load

# Calculate temperature rise
test_data["Temp_Rise"] = test_data["Temperature_C"].diff()

# Remove first row (because diff gives NaN)
test_data = test_data.dropna()


predicted_freq = []
current_freq = 1

for i in range(len(test_data)):

    load = test_data["Predicted_Load"].iloc[i]
    rise = test_data["Temp_Rise"].iloc[i]

    # If temperature rising too fast → reduce frequency
    if rise > 3:
        if current_freq > 1:
            current_freq -= 1

    else:
        if load > 75 and current_freq < 3:
            current_freq += 1
        elif load < 40 and current_freq > 1:
            current_freq -= 1

    predicted_freq.append(current_freq)
# Add to table
test_data["Predicted_Freq"]= predicted_freq

freq_compare = pd.DataFrame({
    "Original_Freq": test_data["Frequency_Level"].values,
    "AI_Predicted_Freq": test_data["Predicted_Freq"].values
})

print("\nOriginal vs AI Frequency:")
print(freq_compare)

