import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#1a
df = pd.read_csv("land.csv")

df = df[['dt', 'AverageTemperature', 'State']]

df['dt'] = pd.to_datetime(df['dt'])
df = df[df['dt'].dt.year > 2000]

states_of_interest = ['Wyoming', 'Nebraska', 'South Dakota']
df = df[df['State'].isin(states_of_interest)]

print(df.head())

#1b
avg_temp_by_date = df.groupby('dt')['AverageTemperature'].mean().reset_index()


avg_temp_by_date.rename(columns={'AverageTemperature': 'AverageTemperatureAcrossStates'}, inplace=True)


print(avg_temp_by_date.head())

#1c
plt.figure(figsize=(10, 6))
plt.plot(avg_temp_by_date['dt'], avg_temp_by_date['AverageTemperatureAcrossStates'], label='Average Temperature')


plt.title('Average Temperature Over Time (Wyoming, Nebraska, South Dakota)', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Average Temperature (°C)', fontsize=12)
plt.legend()
plt.grid(True)


plt.tight_layout()
plt.show()


#1d
avg_temp_by_date['numerical_date'] = avg_temp_by_date['dt'].dt.year + (avg_temp_by_date['dt'].dt.month - 1) / 12
print(avg_temp_by_date.head())


#1e
def sinusoidal_model(x, A, B, C, D):
    return A * np.sin(B * x + C) + D


A_guess = avg_temp_by_date['AverageTemperatureAcrossStates'].std()
B_guess = 2 * np.pi / 1  # Assuming a period of 1 year
C_guess = 0
D_guess = avg_temp_by_date['AverageTemperatureAcrossStates'].mean()
initial_guesses = [A_guess, B_guess, C_guess, D_guess]
print("Initial parameter guesses:", initial_guesses)

#1f
x_data = avg_temp_by_date['numerical_date'].values
y_data = avg_temp_by_date['AverageTemperatureAcrossStates'].values

params, covariance = curve_fit(sinusoidal_model, x_data, y_data, p0=initial_guesses)
print("Fitted parameters:", params)
print("Covariance matrix:", covariance)

#1g
x_fit = np.linspace(x_data.min(), x_data.max(), 500)
y_fit = sinusoidal_model(x_fit, *params)


plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, label='Original Data', color='blue', alpha=0.5)
plt.plot(x_fit, y_fit, label='Fitted Curve', color='red')

plt.title('Curve Fit: Average Temperature Over Time', fontsize=16)
plt.xlabel('Numerical Date', fontsize=12)
plt.ylabel('Average Temperature (°C)', fontsize=12)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()


#1h
errors = np.sqrt(np.diag(covariance))

for i, (param, error) in enumerate(zip(params, errors)):
    print(f"Parameter {i+1}: {param:.4f} ± {error:.4f}")


#1i
A, B, C, D = params

# Print the final equation
print(f"\nFinal equation: y = {A:.4f} * sin({B:.4f} * x + {C:.4f}) + {D:.4f}")


