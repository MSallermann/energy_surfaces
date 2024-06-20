from energy_surfaces.surfaces import lepshogauss
import numpy as np

esurf = lepshogauss.LepsHOGaussSurface()
x = np.array([2.1, 1.2])

print(f"Energy = {esurf.energy(x)}")
print(f"Gradient = {esurf.gradient(x)}")
print(f"Hessian = {esurf.hessian(x)}")