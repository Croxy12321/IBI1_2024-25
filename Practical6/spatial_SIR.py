# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
# Total population in a 100x100 grid
N = 10000
grid_size = 100
# Initialize the population array: 0 for susceptible, 1 for infected, 2 for recovered
population = np.zeros((grid_size, grid_size))
# Randomly select one person to be infected initially
outbreak = np.random.choice(range(grid_size), 2)
population[outbreak[0], outbreak[1]] = 1
# Define beta (infection probability) and gamma (recovery probability)
beta = 0.3
gamma = 0.05
# Create a list to store the population state at each time point
population_history = [population.copy()]
# 100 time point loop
for t in range(100):
    # Find all infected individuals
    infected_indices = np.where(population == 1)
    # For each infected individual, infect their neighbors with probability beta
    for i in range(len(infected_indices[0])):
        x = infected_indices[0][i]
        y = infected_indices[1][i]
        # Check all 8 neighbors
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # Skip the current cell
                nx=x+dx 
                ny=y+dy
                # Check if the neighbor is within bounds and susceptible
                if 0 <= nx < grid_size and 0 <= ny < grid_size:
                    if population[nx, ny] == 0:
                        # Infect the neighbor with probability beta
                        if np.random.rand() < beta:
                            population[nx, ny] = 1
    # Allow infected individuals to recover with probability gamma
    for x in range(grid_size):
        for y in range(grid_size):
            if population[x, y] == 1:
                if np.random.rand() < gamma:
                    population[x, y] = 2
    # Store the current population state
    population_history.append(population.copy())
fig, axes = plt.subplots(2, 2, figsize=(10, 8), dpi=150)
times = [0, 10, 50, 99]
# Per subgraph
for i in range(4):
    ax = axes[i // 2, i % 2]  # Calculates the position of the current subgraph
    time = times[i]
    ax.imshow(population_history[time], cmap='viridis', interpolation='nearest')
    ax.set_title(f'Time {time}')
    ax.axis('off')
plt.tight_layout()
plt.show()
# Save the plot
plt.savefig('spatial_SIR_model.png', type='png')