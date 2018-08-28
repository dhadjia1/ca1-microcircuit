' Author: Darian Hadjiabadi '


import numpy as np
from neuron import h, gui

class StimCell(object):

    def __init__(self):
        self.prelist   = []
        self.all        = None
        self.soma       = None
        self.stim       = None

        self.init()

    def init(self):
        self.topol()
        self.biophys()

    def topol(self):
        self.soma = h.Section(name='soma', cell=self)

    def biophys(self):
        self.stim          = h.RegnStim(self.soma(0.5))
        self.stim.number   = 10000
        self.stim.start    = 0
        self.stim.interval = 25
        self.stim.noise    = 0
        

