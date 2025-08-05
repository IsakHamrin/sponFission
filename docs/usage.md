
#### `usage.md`
```markdown
# Usage Example

```python
import sponFission as sf

uo2 = sf.Material()
uo2.add_nuclide('U235', 0.04)
uo2.add_nuclide('U238', 0.96)
uo2.add_nuclide('O16', 2.0)
uo2.set_density(10.5, 'g/cm3')
uo2.set_volume(1.0)  # in cm³

rate = uo2.get_sf()
print("Spontaneous fission rate:", rate, "fissions/s")
