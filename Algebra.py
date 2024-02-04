import math,random



def sum_of_digits(number: int) -> int:

    total_sum=0
    if number<0:
        print("Sorry we do not support negative numbers")
        quit()
    while(number>0):
        lower_digit= number %10
        number=number//10 
        total_sum= total_sum+lower_digit

    return total_sum

def sum_of_paired_digits(number: int) -> int:

    total_sum_paired=0
    if number<0:
        print("Sorry we do not support negative numbers")
        quit()
    while(number>0):
        lower_digit= number %100
        number=number//100 
        total_sum_paired= total_sum_paired+lower_digit

    return total_sum_paired



question1= input("Would you like to do paired or sum : ")
if question1.lower()=="sum" or question1.lower()=="sum of digits":
    question=int(input("How much times would you like to do this: "))
    for i in range(question):
        current_number= int(input("What is your number: "))
        sum= sum_of_digits(current_number)
        print("The sum of the digits is " + str(sum))
            



elif question1.lower()=="paired" or question1.lower()=="paired digits":
    question3=int(input("How much times would you like to do this: "))
    for i in range(question3):
        current_number=int(input("What is your number: "))
        sum_paired= sum_of_paired_digits(current_number)
        print("The sum of the paired digits is "+ str(sum_paired))

else:
    print("We only support the options of paired of sum")
    quit()


