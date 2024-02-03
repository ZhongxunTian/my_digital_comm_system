# -*- coding: utf-8 -*-

import numpy as np

class ASCIIDecoder():
    def source_decode(self, input):
        output = ""
        for i in range(0, len(input),8):
            byte_bits = input[i:i+8]
            byte_value = int("".join(str(bit) for bit in byte_bits), 2)
            char = chr(byte_value)
            output += char
        return output
    
source_decoder_dict = {"ASCII": ASCIIDecoder}

def source_decoder(source_decoding_type:str):
    if source_decoding_type not in source_decoder_dict:
        raise ValueError("Unsupported source decoding type")
    return source_decoder_dict[source_decoding_type]()