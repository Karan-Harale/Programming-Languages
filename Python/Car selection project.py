class vehicle:
    def showmenu(self,Type_of_vehicle,wheel_formation,category):
        self.Type_of_vehicle=Type_of_vehicle
        self.wheel_formation=wheel_formation
        self.category=category

        print("Type of vehicle ",self.Type_of_vehicle)        
        print("wheel formation of vehicle ",self.wheel_formation)        
        print("category",self.category)


print("Welcome to Online Vehicle Shop")
print("please Select one of the following option\n 1.category\n 2.wheel_formation of vehicle\n 3.Type of vehicle\n4. Quit")

userip=int(input("Enter Your Choice:- "))

if userip==0:
    print("Invalid choice\n Please Enter valid key")
elif userip==1:
        print("select category\n\n 1.Transport\n 2. Non-transport\n3. Back")
        userip11=int(input("Enter Choice:- "))
        
        if userip11==1 or userip11==2:
            print("Available wheel vehicles (basis of no.of wheels per vehicles \n \n 1. 2-wheeler\n 2. 3-wheeler\n 3. 4-wheelar\n 4. 8-wheeler 5.Back")
            
            userip2=int(input("Enter Your Choice:- "))
            
            if userip2==1:
                print("1. Motorcycle\n2. scooter\n3.EV Bike\n4.Ev.Scooter")
            elif userip2==2:
                print("1. Auto\n2. Goods Carrier\n3. LPG Delivery vehicle")
            elif userip2==3:
                print("1. SUV\n2. XUV\n3. Offroad\n4. THAR")
            else:
                print("Invalid choice\nPlease Enter Valid Option")
        else:
            print("Invalid choice\nPlease Enter Valid Option")
else:
    print("Invalid choice\nPlease Enter Valid Option")

# v1=vehicle()



# v1.showmenu()