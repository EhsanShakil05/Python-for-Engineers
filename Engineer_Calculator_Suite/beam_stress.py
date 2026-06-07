# Beam Stress

def beam_stress_calculator():
  force = float(input("Enter force: "))
  area = float(input("Enter area: "))
  stress = force / area
  print("Stress = ", stress)

if __name__ == "__main__":
    beam_stress_calculator()