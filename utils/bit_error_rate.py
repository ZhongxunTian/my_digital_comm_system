import numpy as np

def bit_error_rate(tx_signal, rx_signal):
    if len(tx_signal) != len(rx_signal):
        raise("error: tx_signal and rx_signal have different length")
    num_errors = np.sum(tx_signal != rx_signal)
    return num_errors/len(tx_signal)