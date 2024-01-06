import math,time

def area_of_square(side: float):
    area = pow(side,2)
    return area

def area_of_rectangle(length: float, width: float):
    area= length*width
    return area

def area_of_circle(radius: float):
    area= pow(radius,2) * 3.141592
    return area
 
def area_of_pentagon(side: float):
    area= 0.25 * math.sqrt(5*(5+2*math.sqrt(5)))*pow(side,2)
    return area

def area_of_hexagon(side: float):
    area= 1.5*math.sqrt(3) * pow(side,2)
    return area

# --- main function entry ----------------- 
start_time=time.time()
while True: 
    question= int(input("how much times would you like to do this: "))
    if question>0:
        break
    elif question==0:
        quit()
    elif time.time()-start_time>30:
        print("Sorry you ran out of time")
        exit()

shape_names=["square","circle","hexagon","pentagon","rectangle"]

def validation(shape,shape_names):
    for s in shape_names:
        if s==shape:
            return True
    return shape=="quit"

starttime=time.time()
for i in range(question):
    
    print("We only support: ", shape_names)
    shape=input("what is the shape you want to compute: ").lower()
    if time.time()-starttime>15:
        print("you ran out of time")
        exit()
    if validation(shape,shape_names)==False:
        continue
    starttime=time.time()

    if shape=="quit":
        break
    elif shape =="rectangle":
        length=input("what is the length: ")
        width= input("what is the width: ")
        length=float(length)
        width=float(width)
        area= area_of_rectangle(length,width)
        print(area)
    elif shape =="circle":
        radius =input("what is your radius: ")
        radius=float(radius)
        area= area_of_circle(radius)
        print(area)
    else:
        side=input("what is the side: ")
        side=float(side)
        if shape =="square":
            area=area_of_square(side)
            print(area)
        elif shape =="pentagon":
            area=area_of_pentagon(side)
            print(area)
        elif shape =="hexagon":
            area=area_of_hexagon(side)
            print(area)
