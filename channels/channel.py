# -*- coding: utf-8 -*-

import numpy as np

class IdealChannel():
    def __init__(self, para):
        pass

    def channel_effect(self, input):
        return input

class AWGNChannel():
    snr_db = 0
    snr_power = 0
    def __init__(self, snr_db):
        self.snr_db = snr_db
        self.snr_power = 10**(self.snr_db / 10)
        
    def channel_effect(self, signal):
        signal_power = np.mean(np.abs(signal)**2)
        noise_power = signal_power / self.snr_power

        noise_real = np.sqrt(noise_power/2)*np.random.randn(*signal.shape)
        noise_img = np.sqrt(noise_power/2)*np.random.randn(*signal.shape)
        noise = noise_real + 1j*noise_img
        return signal + noise
    
channel_dict = {"ideal": IdealChannel,
                "AWGN": AWGNChannel}

def channel(channel_type:str, paras=None):
    if channel_type not in channel_dict:
        raise ValueError("Unsupported channel type")
    return channel_dict[channel_type](paras)