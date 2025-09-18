from math import sqrt
def form(x):
    return format(x,'.6f')
def f(x):
    return x*x*x+x*x-1
def g(x):
    return sqrt(1/(x+1))
def iteration(vX,maxIt,countV):
    countV=countV+1
    for i in range(maxIt):
        if(form(g(vX))==form(vX)):
            print("Counted: ",countV)
            return form(vX)
        else:
            vX=g(vX)
            return iteration(vX,maxIt-1,countV)
           
    
x=iteration(0.5,50,0)
print("Value of root: ",x)
