#this conversts mass in kg to energy in joulus
def energy(mass):
    return mass*300_000_000
mass_in_kg = int(input("enter maass in kg"))
energy_in_joulus =energy(mass_in_kg)
print(energy_in_joulus)
