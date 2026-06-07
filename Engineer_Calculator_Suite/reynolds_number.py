#Reynolds Number

def reynolds_calculator():
  density = float(input("Density (kg/m^3): "))
  velocity = float(input("Velocity (m/s): "))
  diameter = float(input("Diameter (m): "))
  viscosity = float(input("Viscosity (Pa.s): "))

  Re = (density * velocity * diameter) / viscosity

  print("Reynolds Number = ", Re)

  if Re < 2300:
    print("Laminar Flow")
  elif Re < 4000:
    print("Transition Flow")
  else:
    print("Turbulent Flow")

if __name__ == "__main__":
    reynolds_calculator()