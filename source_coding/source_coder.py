# -*- coding: utf-8 -*-

import numpy as np

class ASCIICoder():
    def source_code(self, input:str):
        output = np.array([],dtype="int32")
        for char in input:
            binary_string = format(ord(char), '08b')
            binary_digits = np.array([int(bit) for bit in binary_string])
            output = np.concatenate((output, binary_digits))
        return output
    
source_coder_dict = {"ASCII": ASCIICoder}

def source_coder(source_coding_type:str):
    if source_coding_type not in source_coder_dict:
        raise ValueError("Unsupported source coding type")
    return source_coder_dict[source_coding_type]()