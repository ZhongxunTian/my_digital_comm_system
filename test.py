import numpy as np
from source_coding.source_coder import source_coder

binary_string = "0"
bit_array = np.array([int(bit) for bit in binary_string])

print(bit_array)

print(source_coder("ASCII").source_code(binary_string))


string = "Hello"
ascii_values = [ord(char) for char in string]

print(ascii_values)

from utils.bit_error_rate import bit_error_rate
tx_signal = np.array([1,0,1,0,0,1,1])
rx_signal = np.array([1,0,0,0,1,1,1])
print("BER = ", bit_error_rate(tx_signal,rx_signal))