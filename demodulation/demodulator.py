# -*- coding: utf-8 -*-

import numpy as np

class QPSKDeodulator():
    def demodulate(self, signal):
        # 判断数据长度是否为2的倍数，如果不是2的倍数在最后补0
        if len(signal) % 2 != 0:
            signal = np.append(signal,0)

        constellation = {-1-1j: [0, 0],
                         -1+1j: [0, 1],
                         1-1j: [1, 0],
                         1+1j: [1, 1]}
        output = np.array([],dtype=np.int32)
        for symbol in signal:
            closest_point = min(constellation.keys(), key=lambda x: abs(x-symbol))
            output = np.append(output,constellation[closest_point])
        return output
    
class NoneDeodulator():
    def demodulate(self, signal):
        return signal


demodulator_dict = {"QPSK": QPSKDeodulator,
                    "none": NoneDeodulator}

def demodulator(demodulation_type:str):
    if demodulation_type not in demodulator_dict:
        raise ValueError("Unsupported demodulation type")
    return demodulator_dict[demodulation_type]()