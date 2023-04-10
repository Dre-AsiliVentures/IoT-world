import numpy as np
import pandas as pd

# Define mean and standard deviation values for each crop
yield_mean = {'corn': 150, 'wheat': 75, 'soybeans': 120, 'potatoes': 250, 'tomatoes': 200}
yield_std = {'corn': 20, 'wheat': 10, 'soybeans': 15, 'potatoes': 30, 'tomatoes': 25}
fertilizer_mean = {'corn': 20, 'wheat': 10, 'soybeans': 15, 'potatoes': 30, 'tomatoes': 25}
fertilizer_std = {'corn': 2, 'wheat': 1, 'soybeans': 1.5, 'potatoes': 3, 'tomatoes': 2.5}

# Define an empty DataFrame for crop data
crop_data = pd.DataFrame()

# Generate synthetic crop data
n_crops = 100
crops = list(yield_mean.keys())

np.random.seed(42)

# Generate a random crop for each row in the DataFrame
crop_data['crop'] = np.random.choice(crops, size=n_crops)

# Update the 'yield' column
yield_values = []
for c in crop_data['crop']:
    yield_values.append(np.random.normal(yield_mean[c], yield_std[c]))
crop_data['yield'] = yield_values

# Update the 'fertilizer' column
fertilizer_values = []
for c in crop_data['crop']:
    fertilizer_values.append(np.random.normal(fertilizer_mean[c], fertilizer_std[c]))
crop_data['fertilizer'] = fertilizer_values
# save the updated crop data to a CSV file
crop_data.to_csv('crop_data.csv', index=False)
print(crop_data.head())
