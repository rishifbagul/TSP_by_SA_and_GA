import math
import random
import matplotlib.pyplot as plt



# x=[38.24,39.57,40.56,36.26,33.48,37.56,38.42,37.52,41.23,41.17,36.08,38.47,38.15,37.51,35.49,39.36,38.09,36.09,40.44,40.33,40.37,37.57]
# y=[20.42,26.15,25.32,23.12,10.54,12.19,13.11,20.44,9.1,13.05,-5.21,15.13,15.35,15.17,14.32,19.56,24.36,23,13.57,14.15,14.23,22.56]

initial_temprature=1000
alpha=0.9992
x=[1,2,3,1,2,3,4,1]
y=[1,1,1,2,2,2,2,4]

class cities():
    def __init__(self,x,y) -> None:
        if len(x)==len(y):
            self.x=x
            self.y=y
            print("%d cities added"%len(x))
        else:
            print("number of element in x and number of element in y doesnot match")
        

    def dist_between_city(self,A,B):
        return math.sqrt((self.x[A]-self.x[B])**2+(self.y[A]-self.y[B])**2)

    def total_route_distance(self,route):
        total_distance=0
        for i in range(0,len(self.x)-1):
            total_distance+=self.dist_between_city(route[i],route[i+1])
        total_distance+=self.dist_between_city(route[len(self.x)-1],route[0])
        return total_distance
    def show_graph(self,l,initial):
        x=[]
        y=[]
        for i in l:
            x.append(self.x[i])
            y.append(self.y[i])
        x.append(self.x[l[0]])
        y.append(self.y[l[0]])
        plt.subplot(1,2,initial)
        plt.plot(x, y, color='green', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=6)
        if initial==2:
            plt.show()

    

class simulated_anneling():
    def __init__(self,initial_temprature,alpha) -> None:
        self.t=initial_temprature
        self.alpha=alpha

    def calculate_new_t(self):
        self.t=self.t*self.alpha
        return self.t
    
    def neighbour_solution(self,solution):
        ret=solution[:]
        A=random.randint(0,len(ret)-1)
        B=random.randint(0,len(ret)-1)
        while A==B:
            B=random.randint(0,len(ret)-1)
        temp=ret[A]
        ret[A]=ret[B]
        ret[B]=temp
        return ret
    
    def selection_probability(self,energy_diffrence):
        if energy_diffrence>=0:
            return 1
        else:
            return math.exp(energy_diffrence/self.t)


#############################______problem setup___________########################

problem=cities(x,y)
SA=simulated_anneling(initial_temprature, alpha)

############____________simulated anneling algorithm as follows_____________##########
solution=list(range(0,len(x)))
random.shuffle(solution)
problem.show_graph(solution,1)
distance=problem.total_route_distance(solution)
best_solution=solution[:]
best_distance=distance
for i in range(10000):
    SA.calculate_new_t()
    new_solution=SA.neighbour_solution(solution)
    new_distance=problem.total_route_distance(new_solution)
    if SA.selection_probability(distance-new_distance)>=random.random():
        solution=new_solution[:]
        distance=new_distance
    if (new_distance < best_distance) :
        best_distance=new_distance
        best_solution=new_solution[:]
        print("new best distance=>",best_distance)

print("best solution is ==>",best_solution)
print("best distance is ==>",best_distance)
problem.show_graph(best_solution,2)

