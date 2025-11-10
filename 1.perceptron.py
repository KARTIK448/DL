import numpy as np
def unitStep(v):
    if v>=0:
        return 1
    else:
        return 0
    
def perceptronModel(x,w,b):
    v=np.dot(w,x)+b
    y=unitStep(v)
    return y

def orLogicFunction(x):
    w=np.array([1,1])
    b=-0.5
    return perceptronModel(x,w,b)

test1=np.array([0,1])    
test2=np.array([1,1])  
test3=np.array([1,0])  
test4=np.array([0,0])  
        
print("OR ({},{})={}".format(0,1,orLogicFunction(test1)))  
print("OR ({},{})={}".format(1,1,orLogicFunction(test2)))
print("OR ({},{})={}".format(1,0,orLogicFunction(test3)))
print("OR ({},{})={}".format(0,0,orLogicFunction(test4)))      
