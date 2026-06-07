# Spring Force Calculator
# F = kx

import numpy as np
import matplotlib.pyplot as plt

def spring_force_calculator():
    k = float(input("Enter the spring constant (N/m): "))

    x = np.linspace(0,0.05,100)

    F = k*x

    print(F)

    plt.plot(x, F)

    plt.xlabel('Displacement (m)')
    plt.ylabel('Force (N)')
    plt.title('Spring Force vs Displacement')

    plt.grid(True)

    plt.show()

    displacement = float(input("Enter the displacement to find the force: "))
    force = k * displacement
    print(f"The force at a displacement of {displacement} (m) is {force} (N).")

if __name__ == "__main__":
    spring_force_calculator()