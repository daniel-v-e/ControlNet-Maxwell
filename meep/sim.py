import meep as mp
import matplotlib.pyplot as plt
import numpy as np

# Simulation cell size
cell_size = mp.Vector3(1, 1, 0)

# PEC properties
pec_conductivity = 1e7  
pec = mp.Medium(epsilon=1, D_conductivity=pec_conductivity)  

# PEC circle
circle = mp.Cylinder(radius=0.5, material=pec)

# Source
frequency = 2.4e9  
src = [mp.Source(mp.ContinuousSource(frequency=frequency),
                 component=mp.Ex,
                 center=mp.Vector3(0, 0, 0))]

# Simulation
sim = mp.Simulation(cell_size=cell_size,
                    geometry=[circle],
                    sources=src,
                    resolution=256)

# Run simulation for a time to reach steady state
sim.run(until=200) 

# Calculate E-field and J-field
E_field = sim.get_array(center=mp.Vector3(), size=cell_size, component=mp.Ex)
# J_field = sim.get_array(center=mp.Vector3(), size=cell_size, component=mp.Jx)

# Visualize the structure
eps_data = sim.get_array(center=mp.Vector3(), size=cell_size, component=mp.Dielectric)
plt.figure(figsize=(6,6))
plt.imshow(eps_data.transpose(), interpolation='spline36', cmap='inferno')
plt.axis('off')
plt.title('Structure')
plt.show()

# Visualize E-field
plt.figure(figsize=(6,6))
plt.imshow(E_field.transpose(), interpolation='spline36', cmap='RdBu')
plt.axis('off')
plt.title('E-field')
plt.colorbar()
plt.show()

# # Visualize J-field
# plt.figure(figsize=(6,6))
# plt.imshow(J_field.transpose(), interpolation='spline36', cmap='RdBu')
# plt.axis('off')
# plt.title('J-field')
# plt.colorbar()
# plt.show()
