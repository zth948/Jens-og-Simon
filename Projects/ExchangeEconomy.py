from types import SimpleNamespace

class ExchangeEconomyClass:

    def __init__(self):

        par = self.par = SimpleNamespace()

        # a. preferences
        par.alpha = 1/3
        par.beta = 2/3

        # b. endowments
        par.w1A = 0.8
        par.w2A = 0.3

    

    def utility_A(self,x1A,x2A):
        return par.x1A**par.alpha*par.x2A**(1-par.alpha)

    def utility_B(self,x1B,x2B):
        return par.x1B**par.beta*par.x2B**(1-par.beta)


    def demand_A(self,p1,p2):
        x1A = par.alpha*(p1*par.w1A+p2*par.w2A)/p1
        x2A = (1-par.alpha)*(p1*par.w1A+p2*par.w2A)/p2
        return x1A, x2A

    def demand_B(self,p1):
        x1B = par.beta*(p1*par.w1B+p2*par.w2B)/p1
        x2B = (1-par.beta)*(p1*par.w1B+p2*par.w2B)/p2
        return x1B, x2B 
        

    def check_market_clearing(self,p1):

        par = self.par

        x1A,x2A = self.demand_A(p1)
        x1B,x2B = self.demand_B(p1)

        eps1 = x1A-par.w1A + x1B-(1-par.w1A)
        eps2 = x2A-par.w2A + x2B-(1-par.w2A)

        return eps1,eps2
