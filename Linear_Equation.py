import time
def calculate_slope_and_intercept(a: float,b: float,c: float) -> dict:
    if b==0:
        return {"slope": None , "intercept": None}
    slope= -a/b 
    intercept= -c/b
    return {"slope": slope, "intercept": intercept}

#-main function entry---------------
question=int(input("How many times would you like to do this: "))
for i in range(question):
    a=float(input("What is your a: "))
    b=float(input("what is your b: "))
    c=float(input("What is your c: "))
    answer= calculate_slope_and_intercept(a,b,c)
    print("The slope is ",answer["slope"])
    print("The intercept is ", answer["intercept"])
