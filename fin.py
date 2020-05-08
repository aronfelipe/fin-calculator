import math
import numpy as np
import matplotlib.pyplot as plt

class PipeCalc:

    def __init__(self):
        self.t_amb = 300 # Temperatura ambiente [K]
        self.t_base = 350 # Temperatura da base  [K]
        self.length = 0.3 # Comprimento da aleta [m]
        self.a = 0.0009 # Área da seção transversal da aleta [m²]
        self.p = 0.12 # Perímetro da aleta [m]
        self.k = 200 # Condutividade térmica do alumínio [W/mK]
        self.h = 15 # Coeficiente de troca por convecção [W/m²K]

    def calculate_m(self):
        return math.sqrt((self.h * self.p) / (self.k * self.a))
    
    def heat_balance(self, x):
        first = math.cosh((self.calculate_m() * (self.length - x)))
        second = (self.h/(self.calculate_m() * self.k)) * math.sinh((self.calculate_m() * (self.length - x)))
        third = math.cosh(self.calculate_m() * self.length)
        four = (self.h/(self.calculate_m() * self.k))*math.sinh((self.calculate_m() * self.length))
        return ((first + second) / (third + four))
    
    def simulate(self):
        typ = 'x'
        col = 'black'

        list_temperature = []
        list_x = np.arange(0, self.length, self.length/60)
        for i in list_x:
            list_temperature.append(self.heat_balance(i) * (self.t_base-self.t_amb) + self.t_amb)
        
        plt.plot(list_x, list_temperature, c=col, marker=typ)
        plt.title('Temperature decrease in a fin', fontsize=20, )
        plt.xlabel('Distance (m)', fontsize=20)
        plt.ylabel('Average Temperature (K)', fontsize=20)
        plt.show()

pipe = PipeCalc()
pipe.simulate()
