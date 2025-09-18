import math as m
def form(x):
    return format(x,'.3f')
def f(x):
    return 3*x - m.cos(m.radians(x)) - 1

def valid(a, b):
    if(f(a) * f(b) >= 0):
        print("Invalid interval")
        return valid(a + 1, b + 1)
    else:
        return (a, b)
def bisection(a,b,maxIt,countV):
    countV=countV+1
    print(' a: ',a,' b: ',b,' c: ',(a+b)/2,' f(a): ',f(a),' f(b): ',f(b),' f(c): ',f((a+b)/2))
    for i in range(maxIt):
        
        c=(a+b)/2
        
        if(f(a)*f(c)>=0):
            a=c
        else:
            b=c
        print('c: ',form(c),'current c: ',form((a+b)/2))
        print('-------->')
        
        if(form(c)==form((a+b)/2)):
            print("Total Iteration: ",countV)
            return c
        else:
            return bisection(a,b,maxIt-1,countV)
            
        

print(valid(0, 1))
a=valid(0,1)[0]
b=valid(0,1)[1]
print("a: ",a)
print("b: ",b)
print("Answer is: ",bisection(a,b,50,0))