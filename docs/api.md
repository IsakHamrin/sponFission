
#### `api.md`
```markdown
# API Reference

## `Material` class

### `add_nuclide(name, fraction)`
Adds a nuclide to the material by name and fraction or number density.

### `set_density(density, unit='g/cm3')`
Sets the density of the material. Default unit is `g/cm3`.

### `set_volume(volume, unit='cm3')`
Sets the volume of the material.

### `set_absolute(absolute)`
Sets whether to interpret the added values as number densities instead of fractions.

### `get_sf()`
Returns the spontaneous fission rate in fissions/s or fissions/s/cm³.
