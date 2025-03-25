# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
# Total population
N=10000
# Initial susceptible population
S=N-1
# Initial infected population
I=1
# Initial rehabilitation population
R=0
# Define beta and gamma
beta=0.3
gamma=0.05
# Create an empty list to store the S, I, and R values for each point in time
S_list = [S]
I_list = [I]
R_list = [R]
# 1000 point time loop
for t in range(1000):
  # Calculate the current infected
  IR=I/N
  # Calculate the probability that a susceptible person will be infected
  IP=beta*IR
  # Randomly select susceptible people to become infected, NI means new infections
  NI=np.random.choice(range(2), size=S, p=[1-IP,IP]).sum()
  # Infected persons were randomly selected to become recovered, NR means new recoveries
  NR=np.random.choice(range(2), size=I, p=[1-gamma,gamma]).sum()
  # Update status
  S=S-NI
  I=I+NI-NR
  R=R+NR
  # Records the S, I, and R values of the current point in time
  S_list.append(S)
  I_list.append(I)
  R_list.append(R)
  # If all infected people recover, end the cycle early
  if I==0:
    break
# Set the chart size and resolution
plt.figure(figsize=(6,4) , dpi =150)
# Plot the change curve of S, I and R
plt.plot(S_list, label='Susceptible')
plt.plot(I_list, label='Infected')
plt.plot(R_list, label='Recovered')
# Set the horizontal and vertical headings of the chart and the general headings
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR model')
plt.legend()
# Show the chart
plt.show()
# Save the chart
plt.savefig('SIR_model.png', type='png')

