# Factor of Safety

def fos_calculator():
  yield_strength = float(input("Yield Strength: "))
  stress = float(input("Applied Stress: "))

  fos = yield_strength / stress

  if fos > 2:
    print("Safe Design")
  else:
    print("Unsafe Design")

if __name__ == "__main__":
    fos_calculator()