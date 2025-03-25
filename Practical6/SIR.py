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
  # Randomly select susceptible people to become infected
  np
