import math, time

def perimeter_of_square(side: float) -> float : 
    perimeter= 4 * side
    return perimeter 

def perimeter_of_rectangle(length,width: float) -> float:
    perimeter= 2 * length + 2 * width
    return perimeter

def circumference_of_circle(radius : float) -> float:
    circumference= math.pi * 2 * radius
    return circumference

def perimeter_of_pentagon(side: float) -> float:
    perimeter= side * 5 
    return perimeter

def perimeter_of_hexagon(side: float) -> float:
    perimeter= side * 6 
    return perimeter

def validation(users_choice: str,shapes: list)-> bool:
    for e in shapes:
        if users_choice==e:
            return True
        elif users_choice=="quit":
            return True
        else:
        
            return False

# --- main function entry ----------------- 
start_time=time.time()
question= int(input('how much times would you like to do this: '))
if time.time()-start_time>5:
    print("you ran out of time")
    exit()
shapes =['square','circle','rectangle','pentagon','hexagon']
for i in range(question):
    print("we only support " + str(shapes))
    starttime=time.time()
    users_choice=input("which shape would you like to choose: " ).lower()
    if time.time() -start_time>6:
        print("you ran out of time")
        exit()
    if validation(users_choice,shapes)==False:
        print("That is not one of our shapes")
        continue
    if users_choice =="circle":
        radius=float(input("what is the radius: "))
        circumfrence= circumference_of_circle(radius)
        print("The circumfrence is " + str(circumfrence))
    elif users_choice=='square':
        side=float(input("What is your side: "))
        perimeter= perimeter_of_square(side)
        print("The perimeter is " + str(perimeter))
    elif users_choice=="rectangle":
        length=float(input("what is the length: "))
        width=float(input("what is your width: "))
        perimeter= perimeter_of_rectangle(length,width)
        print("the perimeter is "+str(perimeter))
    elif users_choice=="pentagon":
        side=float(input("What is the side: "))
        perimeter= perimeter_of_pentagon(side)
        print("The perimeter is ",perimeter)
    else:
        if users_choice=="quit":
            exit()
        side=float(input("What is the side: "))
        perimeter= perimeter_of_hexagon(side)
        print("The perimeter is ", perimeter)


