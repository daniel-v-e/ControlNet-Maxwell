import meep as mp
import numpy as np
import skimage
import vispy

# Simulation cell size
cell_size = mp.Vector3(8, 8, 0)  

# PEC properties
pec_conductivity = 1e7  # high conductivity for PEC
pec = mp.Medium(epsilon=1, D_conductivity=pec_conductivity)  # PEC medium

# PEC object_2D
object_2D = mp.Cylinder(radius=5, material=pec)
# object_2D = mp.Block(mp.Vector3(8, 8, mp.inf), center=mp.Vector3(), material=pec)


# Source
frequency = 2.4e9  # 2.4 GHz
src = [mp.Source(mp.ContinuousSource(frequency=frequency),
                 component=mp.Ex,
                 center=mp.Vector3(0, 0, 0))]

# Simulation
sim = mp.Simulation(
    cell_size  = cell_size,
    geometry   = [object_2D],
    sources    = src,
    resolution = 32
)

# Run simulation for a time to reach steady state
sim.run(until=200)
sim.plot3D()