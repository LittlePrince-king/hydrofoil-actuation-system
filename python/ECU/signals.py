import math

class SineWave:
    def __init__(self, amplitude=45, offset=90, frequency=0.25):
        self.amplitude = amplitude
        self.offset = offset
        self.frequency = frequency

    def value(self, t):
        return self.offset + self.amplitude * math.sin(2 * math.pi * self.frequency * t)