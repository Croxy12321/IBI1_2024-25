# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
# Define the vaccination rates
VR = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
# Total population
N = 10000
# Define beta and gamma
beta = 0.3
gamma = 0.05
# Store the transfer of each simulation
results = {}
# Loop over each vaccination rate
for rate in VR:
    # Define the number of people vaccinated
    V = int(N * rate)
    # Initial susceptible population
    if (N - V) == 0:
        S = 0
    else:
        S = N - 1 - V
    # Initial infected population
    if (N - V) == 0:
        I = 0
    else:
        I = 1
    # Initial recovered population
    R = 0
    # Create lists to store S, I, and R values over time
    S_list = [S]
    I_list = [I]
    R_list = [R]
    # 1000 time point loop
    for t in range(1000):
        # Calculate the current proportion of infected people
        if (N - V) == 0:
            IR = 0
        else:
            IR = I / (N - V)
        # Calculate the infection probability
        IP = beta * IR
        # Randomly select susceptible individuals to become infected
        NI = np.random.choice([0, 1], size=S, p=[1 - IP, IP]).sum()
        # Randomly select infected individuals to recover
        NR = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma]).sum()
        # Update status
        if (N - V) == 0:
            S = 0
            I = 0
        else:
            S = S - NI
            I = I + NI - NR
        R = R + NR
        # Record the S, I, and R values of the current time point
        S_list.append(S)
        I_list.append(I)
        R_list.append(R)
    # Store the results for this vaccination rate
    results[rate] = I_list
# Set the chart size and resolution
plt.figure(figsize=(10, 6), dpi=150)
# Plot the results for each vaccination rate
for rate in VR:
    plt.plot(results[rate], label=f'Vaccination Rate {rate:.0%}')
# Set the horizontal and vertical headings of the chart and the general headings
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR model with different vaccination rates')
plt.legend()
# Show the chart
plt.show()
# Save the chart
plt.savefig('SIR model with different vaccination rates_model.png', type='png')