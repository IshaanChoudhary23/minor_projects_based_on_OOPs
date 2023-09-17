class Atm:

    counter=1
    def __init__(self):
        self.__pin=""
        self.__balance=0         # INITIALIZE INSATANCE VARIABLE AS SELF.
        self.sno=Atm.counter     #  ALWAYS USE CLASS NAME TO INITIALIZE STATIC VARIABLE
        Atm.counter=Atm.counter+1



        self.menu()
    @staticmethod        #   use this key word for initialze the static method
    def get():           # in static function self os not used
        return Atm.counter
    def get_pin(self):
        return self.__pin
    def set_pin(self,new_pin):
        if type(new_pin)==str:
            self.__pin=new_pin
            print("pin changsed")
        else:
            print("sdsd")

    def menu(self):
        user_input=int(input("""     HOW WOULD YOU LIKE TO PROCEED:
                                    1). ENTER 1 TO SET THE PIN.
                                    2). ENTER 2 TO DEPOSIT THE BALANCE.
                                    3). ENTER 3 TO WITHDRAW THE AMOUNT.
                                    4). ENTER 4 TO CHECK THE BALANCE. 
                                    5). PRESS ANY KEY TO EXIT .   
        
    """))
        if user_input==1:
            self.create_pin()
        elif user_input==2:
            self.deposit()
        elif  user_input==3:
            self.withdraw()
        elif user_input==4:
            self.check_balance()
        else:
            print("thank you for using the ATM machine")



    def create_pin(self):
        self.__pin=int(input("enter your pin"))
        print("pin set successfully")
        temp=int(input("press 1 to continue"))
        if temp ==1:
            self.menu()
        else:
            print("somthing went wrong")

    def deposit(self):
        temp=int(input("enter your pin"))
        if temp==self.__pin:
           amount= int(input("enter your amount"))
           self.__balance=self.__balance+amount
           print(" deposit sucessfully")
        else:
            print("enter a vaild pin")
        temp=int(input("press 1 to continue"))
        if temp ==1:
            self.menu()
        else:
            print("somthing went wrong")


    def withdraw(self):
        temp = int(input("enter your pin"))
        if temp==self.__pin:
            amount=int(input("enter the amount you want to withdraw"))
            if amount<self.__balance:
                self.__balance = self.__balance - amount
                print("amount withdraw successfully")
            else :
                print("enter the valid amount ")
                print("you have in sufficient balance in your acount")

        else :
            print("ebneter the valid pin")
        temp=int(input("press 1 to continue"))
        if temp ==1:
            self.menu()
        else:
            print("somthing went wrong")


    def check_balance(self):
        temp=int(input("enter your pin"))
        if temp==self.__pin:
            print("your account balance is :",self.__balance)
        else:
            print("enter the valid pin")
        temp=int(input("press 1 to continue"))
        if temp ==1:
            self.menu()
        else:
            print("somthing went wrong")


#******************** Encapsulation ->   put two underscore " __ " front of any data variable assigh that as private ********




