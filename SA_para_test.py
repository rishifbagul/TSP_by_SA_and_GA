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
sa=simulated_anneling(144,0.9970)
for i in range(10000):
    t.append(sa.calculate_new_t())
    x.append(sa.selection_probability(-10))
plt.subplot(2,2,1)
plt.plot(x)
plt.title("c=0.9970")

x=[]
t=[]
sa=simulated_anneling(144,0.9980)
for i in range(10000):
    t.append(sa.calculate_new_t())
    x.append(sa.selection_probability(-10))
plt.subplot(2,2,2)
plt.plot(x)
plt.title("c=0.9980")

x=[]
t=[]
sa=simulated_anneling(144,0.9990)
for i in range(10000):
    t.append(sa.calculate_new_t())
    x.append(sa.selection_probability(-10))
plt.subplot(2,2,3)
plt.plot(x)
plt.title("c=0.9990")

x=[]
t=[]
sa=simulated_anneling(144,0.9995)
for i in range(10000):
    t.append(sa.calculate_new_t())
    x.append(sa.selection_probability(-50))
plt.subplot(2,2,4)
plt.plot(x)
plt.title("c=0.9995")
# plt.plot(t)
plt.show()
