import math
import numpy as np
from scipy.interpolate import Akima1DInterpolator
from math import log, exp



# Logarithmic transformation: calculate logarithmic values of energy and values
def take_logarithm(energy, values, interpolated_energy):
    """Calculate the logarithm of a set of values."""
    log_energy = [log(i) for i in energy]
    log_values = [log(e) for e in values]
    log_interpolated_energy = log(interpolated_energy)
    return log_energy, log_values, log_interpolated_energy


# Interpolate lineal: takes values: energy, values and interpolated energy, returns interpolated value with the solution
def log_linear_interpolation(log_energy, log_values, log_interpolated_energy):
    """Interpolate the value at the given energy point."""
    log_interpolated_value = np.interp(log_interpolated_energy, log_energy, log_values)
    return log_interpolated_value


# Interpolate akima: takes energy, values and interpolated_energy, returns interpolated_value_akima
def log_akima_interpolation(log_energy, log_values, log_interpolated_energy):
    """Interpolate the value at the given energy point using Akima interpolation."""
    akima_interpolator = Akima1DInterpolator(log_energy, log_values)
    log_interpolated_value_akima = akima_interpolator(log_interpolated_energy)
    return log_interpolated_value_akima

def log_to_value(log_interpolated_value, log_interpolated_value_akima): #function to return values from logarithmic to int
    interpolated_value = math.exp(log_interpolated_value)
    interpolated_value_akima = math.exp(log_interpolated_value_akima)
    return interpolated_value, interpolated_value_akima

def main():
    print('Script interpolator_functions.py')
    # Input data: define some dummy data to test the script
    energy = [1, 2, 3]  # Energy values of the distribution
    values = [10, 20, 30]  # Variable values of the distribution
    interpolated_energy = 1.5  # Energy value to interpolate
    #take logarithms of the data
    log_energy, log_values, log_interpolated_energy = take_logarithm(energy, values, interpolated_energy)
    #log-linear
    log_interpolated_value = log_linear_interpolation(log_energy, log_values, log_interpolated_energy)
    #log-akima
    log_interpolated_value_akima = log_akima_interpolation(log_energy, log_values, log_interpolated_energy)
    #convert to normal values
    interpolated_value, interpolated_value_akima = log_to_value(log_interpolated_value, log_interpolated_value_akima)

    print(f'Energy: {energy}')  #prints values of variables used in functions
    print(f'Values:{values}')
    print(f'Interpolated_energy:{ interpolated_energy }')
    print(f'log_energy:{log_energy}')
    print(f'log_values:{log_values}')
    print(f'log_interpolated_energy:{log_interpolated_energy}')
    print(f'log_interpolated_value:{log_interpolated_value}')
    print(f'log_interpolated_value_akima{log_interpolated_value_akima}')
    print(f'Interpolated value: {interpolated_value}')
    print(f'Interpolated_value (Akima):{interpolated_value_akima}')


def cli():
    # Command Line Interface to get input from the user
    # Step 1: Get input for energy and values from the user
    print('Introduce data for energy (comma-separated, e.g., "1, 2, 3"), then press enter:')
    energy_input = input()

    print('Introduce data for values (comma-separated, e.g., "10, 20, 30"), then press enter:')
    values_input = input()

    # Step 2: Get input for the interpolated energy value
    print('Introduce interpolated energy (a single number, e.g., "1.5"):')
    interpolated_energy = float(input())  # Convert the user input to a float

    # Convert input strings to lists of floats
    energy = [float(i.strip()) for i in energy_input.split(',')]
    values = [float(i.strip()) for i in values_input.split(',')]

    # Step 3: Perform the logarithmic transformation
    log_energy, log_values, log_interpolated_energy = take_logarithm(energy, values, interpolated_energy)

    # Step 4: Perform the interpolations
    log_interpolated_value = log_linear_interpolation(log_energy, log_values, log_interpolated_energy)
    log_interpolated_value_akima = log_akima_interpolation(log_energy, log_values, log_interpolated_energy)

    # Step 5: Convert log-interpolated values to normal values
    interpolated_value, interpolated_value_akima = log_to_value(log_interpolated_value, log_interpolated_value_akima)

    # Step 6: Print the results
    print(f'Log Interpolated Value (Linear): {log_interpolated_value}')
    print(f'Log Interpolated Value (Akima): {log_interpolated_value_akima}')
    print(f'Interpolated Value (Linear): {interpolated_value}')
    print(f'Interpolated Value (Akima): {interpolated_value_akima}')



# main block

if __name__ == "__main__":
    main()
    cli()


