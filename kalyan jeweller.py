print("\n")

print("-:  WELLCOM TO KALYAN JWELLERS :-") 

print("-----------------------------------")

name=input("Enter your name:-")  # it will take input from user
gender=(input("Enter  'F' or  'M':-")).upper()  # will take gender of user
age=int(input("Enter your age:-")) # will take age of the user


grandtotal=0 

status= True  #initilization for entry level conditional statement

while status: # creating while condition loop which will execute till the  current status is True 


    print("---------------------------\n")
    
    product=input("Enter product name:-")
    grm=int(input("Enter product gram:-"))
    
    print("Current gold price(1 grm)=5752")

    print("---------------------------")


    totalgoldrate=grm*5752          #will give the value of grm*current gold rate to totalgoldrate

    print("TOTAL GOLD RATE  :",totalgoldrate) # print total gold rate
    print("\n")
    print("MAKING CHARGES(1 GRM) : 845")
    print("-----------------------------")

    makingcharge=grm*845                       # total makimng charges of the product
    totalamount=totalgoldrate+makingcharge     # total amount of the product

    print("your total making charge of your product:",makingcharge)
    print("--------------------------------")
    print("TOTAL AMOUNT with makingcharge:",totalamount)
    print("\n")



    if age>65 and gender=='M':            # nested conditional statements
        if totalamount>=200000 and totalamount<=300000: # if totalamoutnt is between 200000 to 300000 then
            dis=totalamount*20/100 # it will give 20% discount
            print("you will get 20% discount on your purches\n")
       
   
        elif totalamount>=300000  and  totalamount<=500000: # if totalamoutnt is between 300000 to 500000 then
            dis=totalamount*30/100    # it will give 30% discount
            print("you will get 30% discount your purches\n")
       
   
        elif totalamount>=500000:  # if totalamount is greater then 500000 then 
            dis=totalamount*35/100 # it will give 35% discount 
            print("you will get 35% discount your purches\n")
       
   
        elif totalamount<=200000:# if total amount is under 200000 then
            print("you will not get any discount\n") # will not give any dicount
       
        else:
            print("you will not get any discount")


    elif age<65 and gender=='M':
        if totalamount>=200000 and totalamount<=300000:# if totalamoutnt is between 200000 to 300000 then
            dis=totalamount*10/100 # it will give 10% discount
            print("you will get 10% discount your purches\n")
       
   
        elif totalamount>=300000  and  totalamount<=500000:  # if totalamoutnt is between 300000 to 500000 then
            dis=totalamount*20/100 # it will give 20% discount
            print("you will get 20% discount your purches\n")
        
   
        elif totalamount>=500000:  # if totalamount is greater then 500000 then
            dis=totalamount*25/100 # it will give 25% discount
            print("you will get 25% discount your purches\n")
       
   
        elif totalamount<=200000: # if total amount is under 200000 the
            print("you will not get any discount\n") # will not give any dicount
       
        else:
            print(" ")

    elif age>65 and gender=='F':             # nested conditional statements
        if totalamount>=200000 and totalamount<=300000:# if totalamoutnt is between 200000 to 300000 then
            dis=totalamount*25/100 # it will give 25% discount
            print("you will get 25% discount on your purches\n")
       
   
        elif totalamount>=300000  and  totalamount<=500000: # if totalamoutnt is between 300000 to 500000 then
            dis=totalamount*35/100 # it will give 35% discount
            print("you will get 35% discount your purches\n")
       
   
        elif totalamount>=500000:  # if totalamount is greater then 500000 then
            dis=totalamount*40/100 # it will give 40% discount
            print("you will get 40% discount your purches\n")
       
   
        elif totalamount<=200000: # if total amount is under 200000 the
            print("you will not get any discount\n") # will not give any dicount
       
        else:
            print("you will not get any discount")


    elif age<65 and gender=='F':
        if totalamount>=200000 and totalamount<=300000:# if totalamoutnt is between 200000 to 300000 then
            dis=totalamount*15/100 # it will give 15% discount
            print("you will get 15% discount your purches\n")
       
   
        elif totalamount>=300000  and  totalamount<=500000: # if totalamoutnt is between 300000 to 500000 then
            dis=totalamount*25/100 # it will give 25% discount
            print("you will get 25% discount your purches\n")
        
   
        elif totalamount>=500000:  # if totalamount is greater then 500000 then
            dis=totalamount*30/100 # it will give 30% discount
            print("you will get 30% discount your purches\n")
       
   
        elif totalamount<=200000: # if total amount is under 200000 the
            print("you will not get any discount\n") # will not give any dicount
       
        else:
            print(" ")
        

    else:
        print("you have not give proper information")


    disamount=dis-makingcharge # it will show discount amount without makinng charges 


    if disamount<0: # if discount amount is less then 0 
        disamount="zero" # assign zero to discount amount 
        print(f"your dicounted amount without making charges: {disamount}")

    else:  
        disamount=disamount # it will assign original value to discount amount
        print(f"your dicounted amount without making charges: {disamount}")

    print("---------------------------------")
    totalamount1=totalamount-dis # store the value of final amount into totalamount1
    print("FINAL amount :",totalamount1)
    print("\n")


    choice=input("do you wnat to purchese more: press 'Y' for yes and press 'N' for no:").upper()

    if choice=='y' or choice=='Y' or choice=='yes':
        status=True   # if status= true, then it will run while loop again
    else:
       
       status=False # it will break the loop 

    
    grandtotal+=totalamount1 # grand total of all products

    
print("your grand total of all product:",grandtotal) #it will give total of all products 
print("\n")
print("-:THANKU FOR VISITING KALYAN JWELLER:-")
    
print("\n")






