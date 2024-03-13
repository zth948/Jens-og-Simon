from types import SimpleNamespace
import numpy as np

class ExchangeEconomyClass:

    def __init__(self):

        par = self.par = SimpleNamespace()

        # a. preferences
        par.alpha = 1/3
        par.beta = 2/3

        # b. endowments
        par.w1A = 0.8
        par.w2A = 0.3
        par.w1B = 1-par.w1A
        par.w2B = 1-par.w2A

    def utility_A(self,x1A,x2A):
        par = self.par
        return x1A**par.alpha*x2A**(1-par.alpha)

    def utility_B(self,x1B,x2B):
        par = self.par
        return x1B**par.beta*x2B**(1-par.beta)

    def demand_A(self,p1):
        par = self.par
        x1A = par.alpha*(p1*par.w1A+par.w2A)/p1
        x2A = (1-par.alpha)*(p1*par.w1A+par.w2A) 
        return x1A, x2A

    def demand_B(self,p1):
        par = self.par
        x1B = par.beta*(p1*par.w1B+par.w2B)/p1
        x2B = (1-par.beta)*(p1*par.w1B+par.w2B)
        return x1B, x2B 
    
    def initial_endowment(self):
        par = self.par
        initial_utility_A = self.utility_A(par.w1A,par.w2A)
        initial_utility_B = self.utility_B(par.w1B,par.w2B)
        return initial_utility_A, initial_utility_B
    
    def pareto(self,N,do_print=True):
        par = self.par

        # a. Numpy array
        shape_tuple = (N)
        x1A_values = np.empty(shape_tuple)
        x2A_values = np.empty(shape_tuple)
        x1B_values = np.empty(shape_tuple)
        x2B_values = np.empty(shape_tuple)
        uA_values = np.empty(shape_tuple)
        uB_values = np.empty(shape_tuple)

        # b. start from guess
        x1A_initial = 0.8
        x2A_initial = 0.3
        x1B_initial = 0.2
        x2B_initial = 0.7
        # we have already expressions for endowmnet values and utility

        # c. loop through possibilities
        for i in range(N):

            # i. x1
            x1A_values[i] = x1A = i/N
            x1B_values[i] = x1B = 1 - x1A_values[i]

            # ii. x2
            x2A_values[i] = x2A = i/N
            x2B_values[i] = x2B = 1 - x2A_values[i]

            # utilities 
            uA_values[i] = uA = self.utility_A(x1A,x2A)
            uB_values[i] = uB = self.utility_B(x1B,x2B)

            if uA_values[i] >= self.utility_A(par.w1A,par.w2A):
                x1A_initial = x1A_values[i]
                x2A_initial = x2A_values[i]
                self.initial_utility_A = uA_values[i]

            if uB_values[i] >= self.utility_B(par.w1B,par.w2B):
                x1B_initial = x1B_values[i]
                x2B_initial = x2B_values[i]
                self.initial_utility_B = uB_values[i]

        # d. print
        #if do_print:
         #   print_solution(x1A_initial,x2A_initial,x1B_initial,x2B_initial,uA_values,uB_values)

        return x1A_initial,x2A_initial,x1B_initial,x2B_initial,uA_values,uB_values,uA,uB
    
    # function for printing the solution
#def print_solution(x1A,x2A,x1B,x2B,uA,uB):
    #print(f'x1A = {x1A:.2f}')
    #print(f'x2A = {x2A:.2f}')
    #print(f'x1B = {x1B:.2f}')
    #print(f'x2B = {x2B:.2f}')
    #print(f'uA  = {uA:.2f}')
    #print(f'uB  = {uB:.2f}')













    # For question 2
    def check_market_clearing(self,p1):

        par = self.par

        x1A,x2A = self.demand_A(p1)
        x1B,x2B = self.demand_B(p1)

        eps1 = x1A-par.w1A + x1B-(1-par.w1A)
        eps2 = x2A-par.w2A + x2B-(1-par.w2A)

        return eps1,eps2
