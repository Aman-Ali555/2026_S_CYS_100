import periodictable

h = periodictable.elements.symbol('H').mass
o = periodictable.elements.symbol('O').mass
water_mass = (2 * h) + o
print(f"Molar Mass: {water_mass:.2f} g/mol")