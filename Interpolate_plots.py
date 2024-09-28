import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Load your data from a CSV file
# Assuming the data is stored in a CSV file with no header
print("Keep the file and .csv file in same folder")
file_name = input('Enter the file name - ')
df = pd.read_csv(file_name, header=None)

# Extract the first and second columns
x_data = df[0].values  # First column
y_data = df[1].values  # Second column

# Number of Equidistant points you want
inter_points = int(input("Enter the number of points, the more the better - "))

# Generate 100 equidistant points between the minimum and maximum of the first column
x_min = np.min(x_data)
x_max = np.max(x_data)
equidistant_x = np.linspace(x_min, x_max, inter_points)

# Interpolate the second column values at these equidistant points
interpolator = interp1d(x_data, y_data, kind='linear', fill_value="extrapolate")
equidistant_y = interpolator(equidistant_x)

# Save the interpolated data to a CSV file
interpolated_df = pd.DataFrame({
    'X': equidistant_x,
    'Y': equidistant_y
})
interpolated_df.to_csv('interpolated_data.csv', index=False)

# Plot the original data (real data)
plt.scatter(x_data, y_data, color='blue', label='Real Data', alpha=0.5)

# Plot the interpolated data
plt.plot(equidistant_x, equidistant_y, color='red', label='Interpolated Data', marker='o')

# Add labels and legend
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Real vs Interpolated Data')

# Show the plot
plt.show()
