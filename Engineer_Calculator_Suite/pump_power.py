# Pump Power Calculator
# P = Q * H * ρ * g

density = 1000  # kg/m³ (density of water)
gravity = 9.81  # m/s² (acceleration due to gravity)

def calculate_pump_power():
    flowrate = float(input("Enter the flow rate in cubic meters per second (m³/s): "))
    head = float(input("Enter the head in meters (m): "))
    power = flowrate * head * density * gravity
    print("The required pump power is: " + str(power) + " watts (W)")

if __name__ == "__main__":
    calculate_pump_power()