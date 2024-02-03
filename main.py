# -*- coding: utf-8 -*-

import numpy as np
from source_coding.source_coder import source_coder
from channel_coding.channel_coder import channel_coder
from modulation.modulator import modulator
from channels.channel import channel
from demodulation.demodulator import demodulator
from channel_decoding.channel_decoder import channel_decoder
from source_decoding.source_decoder import source_decoder

# comm_process = [source_code, channel_code, modulate, channel, demodulate, channel_decode, source_decode]

source_code = source_coder("ASCII").source_code
channel_code = channel_coder("none").channel_code
modulate = modulator("QPSK").modulate
channel_effect = channel("AWGN",30).channel_effect
demodulate = demodulator("QPSK").demodulate
channel_decode = channel_decoder("none").channel_decode
source_decode = source_decoder("ASCII").source_decode

comm_process = [source_code, channel_code, modulate, channel_effect, demodulate, channel_decode, source_decode]
# source = np.array([1,0,1,0,0,1])
source = "Hello world!"
print("source = ", source)
output = source

for process in comm_process:
    output = process(output)
    print(process.__name__," = ",output)

print("output = ",output)

