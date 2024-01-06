import math,time

def quadratic_function_solver(a:float,b:float,c: float)-> list:
    if a==0 and b==0 and c==0:
        return ["Infinite Solutions"]
    if b==0 and a==0:
        return []
    if a ==0:
        x=-c/b
        return x 

    delta= pow(b,2) - 4*a*c
    if delta==0:
        x=-b/(2*a)
        return x
    elif delta <0:
        x=-b/(2*a) + (1j)*math.sqrt(-delta)/(2*a)
        x2=x.conjugate()
        return x,x2
    else:
        
        x1= (-b+ math.sqrt(delta)) /(2*a)
        x2= (-b-math.sqrt(delta))/(2*a)
        return x1,x2
    
# --- main function entry ----------------- 
start_time=time.time()
if time.time()-start_time>15:
    print("you ran out of time")
    exit()
question=int(input("How much times would you like to do this: "))
if time.time()-start_time>10:
    print("You ran out of time")
    exit()
for i in range(question):
    print("We only support quadratic equations in the form ax**2 + bx + c")
    a=float(input("What is your a: "))
    b=float(input("what is your b: "))
    c=float(input("What is your c: "))
    
    answer=quadratic_function_solver(a,b,c)
    print("The answer is", answer)
    