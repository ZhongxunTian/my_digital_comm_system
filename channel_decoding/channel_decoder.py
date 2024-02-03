import numpy as np

class ParityCheckDecoder():
    def channel_decode(self, signal):
        return signal

class NoneDecoder():
    def channel_decode(self, signal):
        return signal
    
channel_decoder_dict = {"parity": ParityCheckDecoder,
                        "none": NoneDecoder}

def channel_decoder(channel_decoding_type:str):
    if channel_decoding_type not in channel_decoder_dict:
        raise ValueError("Unsupported channel decoding type")
    return channel_decoder_dict[channel_decoding_type]()