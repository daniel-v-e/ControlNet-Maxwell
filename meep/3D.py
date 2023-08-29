import meep as mp

# Simulation cell size
cell_size = mp.Vector3(8, 8, 8)

# PEC properties
pec_conductivity = 1e7  
pec = mp.Medium(epsilon=1, D_conductivity=pec_conductivity)  

# PEC object_3D
# object_3D = mp.Block(mp.Vector3(5, 5, 5), center=mp.Vector3(), material=pec)
object_3D = mp.Cylinder(radius=5, material=pec)

# Source
frequency = 2.4e9  
src = [mp.Source(
    src       = mp.ContinuousSource(frequency=frequency),
    component = mp.Ex,
    center    = mp.Vector3(0, 0, 0)
)]

# Simulation
sim = mp.Simulation(
    cell_size  = cell_size,
    geometry   = [object_3D],
    sources    = src,
    resolution = 16
)

# Run simulation for a time to reach steady state
sim.run(until=100)

# # Calculate E-field
# E_field = sim.get_array(center=mp.Vector3(), size=cell_size, component=mp.Ex)
sim.plot3D()