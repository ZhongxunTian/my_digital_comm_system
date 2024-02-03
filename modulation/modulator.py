# -*- coding: utf-8 -*-

import numpy as np

class QPSKModulator():
    def modulate(self, signal):
        # 判断数据长度是否为2的倍数，如果不是2的倍数在最后补0
        if len(signal) % 2 != 0:
            signal = np.append(signal,0)

        constellation = {"[0 0]": -1-1j,
                         "[0 1]": -1+1j,
                         "[1 0]": 1-1j,
                         "[1 1]": 1+1j}
        modulation_symbols = np.array([signal[i:i+2] for i in range(0, len(signal),2)])
        output = np.array([constellation[str(symbol)] for symbol in modulation_symbols])
        return output

class NoneModulator():
    def modulate(self, signal):
        return signal

modulator_dict = {"QPSK": QPSKModulator,
                  "none": NoneModulator}

def modulator(modulation_type:str):
    if modulation_type not in modulator_dict:
        raise ValueError("Unsupported modulation type")
    return modulator_dict[modulation_type]()