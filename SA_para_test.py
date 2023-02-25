import matplotlib.pyplot as plt
import math

class simulated_anneling():
    def __init__(self,initial_temprature,alpha) -> None:
        self.t=initial_temprature
        self.alpha=alpha

    def calculate_new_t(self):
        self.t=self.t*self.alpha
        return self.t
    
    def selection_probability(self,energy_diffrence):
        if energy_diffrence>=0:
            return 1
        else:
            return math.exp(energy_diffrence/self.t)
x=[]
t=[]
sa=simulated_anneling(1000,0.9992)
for i in range(10000):
    t.append(sa.calculate_new_t())
    x.append(sa.selection_probability(-10))
    
plt.plot(x)
# plt.plot(t)
plt.show()
