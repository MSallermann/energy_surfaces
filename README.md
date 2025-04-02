# Energy_surfaces
Some energy surfaces. Implemented in python with numba JIT

# Installation

```bash
pip install .
```

# Minimum working example
```python
from energy_surfaces.surfaces import lepshogauss
import numpy as np

esurf = lepshogauss.LepsHOGaussSurface()
x = np.array([2.1, 1.2])

print(f"Energy = {esurf.energy(x)}")
print(f"Gradient = {esurf.gradient(x)}")
print(f"Hessian = {esurf.hessian(x)}")
```