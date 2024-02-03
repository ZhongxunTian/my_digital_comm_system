import numpy as np

class ParityCheckCoder():
    def channel_code(self, signal):
        return signal

class NoneCoder():
    def channel_code(self, signal):
        return signal

channel_coder_dict = {"parity": ParityCheckCoder,
                      "none": NoneCoder}

def channel_coder(channel_coding_type:str):
    if channel_coding_type not in channel_coder_dict:
        raise ValueError("Unsupported channel coding type")
    return channel_coder_dict[channel_coding_type]()