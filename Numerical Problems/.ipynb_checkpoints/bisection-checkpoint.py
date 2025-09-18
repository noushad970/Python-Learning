from math import cos
def f(x):
    return 3*x - cos(x) - 1

def valid(a, b):
    if(f(a) * f(b) >= 0):
        print("Invalid interval")
        return valid(a + 1, b + 1)
    else:
        return (a, b)
def bisection(a,b,maxIt,countV):
    countV=countV+1
    for i in range(maxIt):
        c=a+b/2
        

print(valid(0, 1))
a=valid(0,1)[0]
b=valid(0,1)[1]
print("a: ",a)
print("b: ",b)