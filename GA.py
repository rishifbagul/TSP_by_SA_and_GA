import math
import random
import matplotlib.pyplot as plt



x=[38.24,39.57,40.56,36.26,33.48,37.56,38.42,37.52,41.23,41.17,36.08,38.47,38.15,37.51,35.49,39.36,38.09,36.09,40.44,40.33,40.37,37.57]
y=[20.42,26.15,25.32,23.12,10.54,12.19,13.11,20.44,9.1,13.05,-5.21,15.13,15.35,15.17,14.32,19.56,24.36,23,13.57,14.15,14.23,22.56]

# x=[1,2,3,4,5,1,2,3,4,5]
# y=[1,1,1,1,1,2,2,2,2,2]

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
    
    def calculate_distance_for_all_population(self,population):
        ret=[]
        for i in population:
            ret.append(self.total_route_distance(i))
        return ret
    
    def show_graph(self,r,c,l,f):
        x=[]
        y=[]
        for j,ele in enumerate(l):
            for i in ele:
                x.append(self.x[i])
                y.append(self.y[i])
            x.append(self.x[ele[0]])
            y.append(self.y[ele[0]])
            plt.subplot(r,c,j+1)
            plt.plot(x, y, color='green', linewidth = 1,
            marker='o', markerfacecolor='blue', markersize=5)
            plt.title(str(j+1)+" => "+str(round(f[j],2)))
            x=[]
            y=[]
        plt.show()

    def show_single_graph(self,l):
        x=[]
        y=[]
        for i in l:
            x.append(self.x[i])
            y.append(self.y[i])
        x.append(self.x[l[0]])
        y.append(self.y[l[0]])
        plt.plot(x, y, color='green', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=6)
        plt.title("best fitness=> "+str(round(self.total_route_distance(l),2)))
        plt.show()



class genetic_algorithm():
    def __init__(self,number_of_cities) -> None:
        self.city_length=number_of_cities
        

    def initialise_population(self,number_of_population):
        ret=list()
        temp_list=list(range(self.city_length))
        for i in range(number_of_population):
            random.shuffle(temp_list)
            while temp_list in ret:
                random.shuffle(temp_list)
            ret.append(temp_list[:])
        return ret
            
    def select_two_parents_basedon_tournament(self,fitness_value_list):
        ret_a=0
        ret_b=0
        a=random.randint(0,len(fitness_value_list)-1)
        b=random.randint(0,len(fitness_value_list)-1)
        # while a==b:
        #     b=random.randint(0,len(fitness_value_list)-1)
        ret_a= a if fitness_value_list[a]<fitness_value_list[b] else b
        ret_b=ret_a
        while ret_a==ret_b:
            a=random.randint(0,len(fitness_value_list)-1)
            b=random.randint(0,len(fitness_value_list)-1)
            # while a==b:
            #     b=random.randint(0,len(fitness_value_list)-1)
            ret_b= a if fitness_value_list[a]<fitness_value_list[b] else b

        return ret_a,ret_b
        
    def breed_two_parents(self,a,b):
        cross_over_point_A=random.randint(0,self.city_length)
        cross_over_point_B=random.randint(0,self.city_length)
        while cross_over_point_A==cross_over_point_B:
            cross_over_point_B=random.randint(0,self.city_length)

        if cross_over_point_A>cross_over_point_B:
            temp=cross_over_point_A
            cross_over_point_A=cross_over_point_B
            cross_over_point_B=temp
        A=list(-1 for i in range(self.city_length))
        B=list(-1 for i in range(self.city_length))
        A[cross_over_point_A:cross_over_point_B]=b[cross_over_point_A:cross_over_point_B]
        B[cross_over_point_A:cross_over_point_B]=a[cross_over_point_A:cross_over_point_B]
        for i in range(len(a)):
            A[i]=a[i] if A[i]==-1 and a[i] not in A else A[i]
            B[i]=b[i] if B[i]==-1 and b[i] not in B else B[i]
        for i in range(len(a)):
            if A[i]==-1:
                for j in range(len(a)):
                    if a[j] not in A:
                        A[i]=a[j]
                        break
            if B[i]==-1:
                for j in range(len(a)):
                    if b[j] not in B:
                        B[i]=b[j]
                        break
        return A,B
    
    def mutation(self,solution):
        ret=solution[:]
        A=random.randint(0,len(ret)-1)
        B=random.randint(0,len(ret)-1)
        while A==B:
            B=random.randint(0,len(ret)-1)
        temp=ret[A]
        ret[A]=ret[B]
        ret[B]=temp
        return ret
        



    def reproduction(self,total_population,total_fitness,generation_size,percentage_of_selection):
        ret_pop=list()
        ret_fit=list()
        for i in range(int(generation_size*percentage_of_selection)):
            j=total_fitness.index(min(total_fitness))
            if total_population[j] not in ret_pop:
                ret_pop.append(total_population[j][:])
                ret_fit.append(total_fitness[j])
            total_fitness.pop(j)
            total_population.pop(j)
        while len(ret_fit)<generation_size:
            j=random.randint(0,len(total_fitness)-1)
            if total_population[j] not in ret_pop:
                ret_pop.append(total_population[j][:])
                ret_fit.append(total_fitness[j])
            total_fitness.pop(j)
            total_population.pop(j)
        
        return ret_pop,ret_fit


#############___________________ ALgorithm parameters ________________############
population_size=30
no_of_runs=int(10000/population_size)

#############______________________ problem setup ____________________############
problem=cities(x,y)
GA=genetic_algorithm(len(x))


#############___________________ Genetic Algorithm Implimentation ________________############
population=GA.initialise_population(population_size)
population_fitness=problem.calculate_distance_for_all_population(population)
# problem.show_graph(2,1,population,population_fitness)
new_population=list()
new_population_fitness=list()

for i in range(no_of_runs):
    for j in range(int(population_size/2)):
        a,b=GA.select_two_parents_basedon_tournament(population_fitness)
        A,B=GA.breed_two_parents(population[a],population[b])
        new_population.append(GA.mutation(A))
        new_population.append(GA.mutation(B))
    new_population_fitness=problem.calculate_distance_for_all_population(new_population)
    new_population=new_population+population
    new_population_fitness=new_population_fitness+population_fitness
    population,population_fitness=GA.reproduction(new_population,new_population_fitness,population_size,0.8)
    new_population=[]

print("best distance is=>",population_fitness[0])
print("best soultion is=>",population[0])
problem.show_graph(5,6,population,population_fitness)
problem.show_single_graph(population[0])
