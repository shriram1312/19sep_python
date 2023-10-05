print("\n")

print("-:  WELLCOM TO KALYAN JWELLERS :-") 

print("-----------------------------------")

name=input("Enter your name:-")
gender=(input("Enter  'F' or  'M':-")).upper()
age=int(input("Enter your age:-"))


A=0

status= True

while status:


    print("---------------------------\n")
    
    product=input("Enter product name:-")
    grm=int(input("Enter product gram:-"))
    
    print("Current gold price(1 grm)=5752")

    print("---------------------------")


    totalgoldrate=grm*5752                                    #total gold rate

    print("TOTAL GOLD RATE  :",totalgoldrate)
    print("\n")
    print("MAKING CHARGES(1 GRM) : 845")
    print("-----------------------------")

    makingcharge=grm*845                                      # total makimng charges of the product
    totalamount=totalgoldrate+makingcharge                    # total amount of the product

    print("your total making charge of your product:",makingcharge)
    print("--------------------------------")
    print("TOTAL AMOUNT with makingcharge:",totalamount)
    print("\n")



    if age>65 and gender=='M':                                                        # nested conditional statements
        if totalamount>=200000 and totalamount<=300000:
            dis=totalamount*20/100
            print("you will get 20% discount on your purches\n")
       
   
        elif totalamount>=300000  and  totalamount<=500000:
            dis=totalamount*30/100
            print("you will get 30% discount your purches\n")
       
   
        elif totalamount>=500000:
            dis=totalamount*35/100
            print("you will get 35% discount your purches\n")
       
   
        elif totalamount<=200000:
            print("you will not get any discount\n")
       
        else:
            print("you will not get any discount")


    elif age<65 and gender=='M':
        if totalamount>=200000 and totalamount<=300000:
            dis=totalamount*10/100
            print("you will get 10% discount your purches\n")
       
   
        elif totalamount>=300000  and  totalamount<=500000:
            dis=totalamount*20/100
            print("you will get 20% discount your purches\n")
        
   
        elif totalamount>=500000:
            dis=totalamount*25/100
            print("you will get 25% discount your purches\n")
       
   
        elif totalamount<=200000:
            print("you will not get any discount\n")
       
        else:
            print(" ")
        

    else:
        print("you have not give proper information")


    disamount=dis-makingcharge


    if disamount<0:
        disamount="zero"
        print(f"your dicounted amount without making charges: {disamount}")

    else:
        disamount=disamount
        print(f"your dicounted amount without making charges: {disamount}")

    print("---------------------------------")
    totalamount1=totalamount-dis
    print("FINAL amount :",totalamount1)
    print("\n")


    choice=input("do you wnat to purchese more: press 'Y' for yes and press 'N' for no:").upper()

    if choice=='y' or choice=='Y' or choice=='yes':
        status=True
    else:
       
       status=False

    
    A+=totalamount1

    
print("your grand total of all product:",A)
print("\n")
print("-:THANKU FOR VISITING KALYAN JWELLER:-")
    
print("\n")






