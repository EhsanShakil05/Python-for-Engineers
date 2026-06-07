from reynolds_number import reynolds_calculator
from beam_stress import beam_stress_calculator
from factor_of_safety import fos_calculator
from spring_force import spring_force_calculator
from pump_power import calculate_pump_power
from csv_stress_analysis import csv_stress_analysis


def main():
    while True:
        print("\nEngineering Calculator Suite")
        print("1. Reynolds Number Calculator")
        print("2. Beam Stress Calculator")
        print("3. Factor of Safety Calculator")
        print("4. Spring Force Calculator")
        print("5. Pump Power Calculator")
        print("6. CSV Stress Analysis")
        print("7. Exit")

        choice = input("Choose Calculator: ")

        if choice == "1":
            reynolds_calculator()

        elif choice == "2":
            beam_stress_calculator()

        elif choice == "3":
            fos_calculator()

        elif choice == "4":
            spring_force_calculator()

        elif choice == "5":
            calculate_pump_power()

        elif choice == "6":
            csv_stress_analysis()

        elif choice == "7":
            print("Exiting Engineering Calculator Suite.")
            break

        else:
            print("Invalid choice. Please select 1 to 7.")


main()