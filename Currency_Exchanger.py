class xyx:

    def __init__(self):
        self.value=""


        self.option()


    def option(self):
        options=int(input("""  *********** Welcome ***************
                            **** How would  you like to proceed ***
                             1). press 1 for Rs to $
                             2). press 2 for Rs to euro
                             3). press 3 for Rs to Dirham
                             4). press 4 for Rs to Chinese Yuan
                             5). press 5 for RS to japenese Yen
    """))

        if options==1:
            print("You have selected the option for RS to $ ")
            self.dollar()
        if options==2:
            print("You have selected the option for RS to euro ")
            self.euro()
        if options==3:
            print("You have selected the option for RS to dirham ")
            self.dirham()
        if options==4:
            print("You have selected the option for Rs to yuan  ")
            self.yuan()
        if options==5:
            print("You have selected the option for Rs to YEN ")
            self.yen()
        else:
            self.exit()

    def exit(self):
        print("PLEASE ENTER THE VALID CHOICE !!!!!!")

    def dollar(self):
        self.value = int(input("enter the amount "))
        temp=self.value/81.5
        print("after converting your amount ", round(temp,3))
        print("thank you for using ")
        n=int(input("press 1 if you want to continue: \n"))
        if n==1:
            self.option()
        else:
            print(" please visit again")



    def euro(self):
        self.value = int(input("enter the amount "))
        temp = self.value / 84.34
        print("after converting your amount ", round(temp,3))
        print("thank you for using ")
        n = int(input("press 1 if you want to continue: \n"))
        if n == 1:
            self.option()
        else:
            print(" please visit again")


    def dirham(self):
            self.value = int(input("enter the amount "))
            temp = self.value / 22.19
            print("after converting your amount ", round(temp,3))
            print("thank you for using ")
            n = int(input("press 1 if you want to continue: \n"))
            if n == 1:
                self.option()
            else:
                print(" please visit again")

    def yuan(self):
            self.value = int(input("enter the amount "))
            temp = self.value /11.45
            print("after converting your amount ", round(temp,3))
            print("thank you for using ")
            n = int(input("press 1 if you want to continue: \n"))
            if n == 1:
                self.option()
            else:
                print(" please visit again")

    def yen(self):
        self.value = int(input("enter the amount "))
        temp = self.value / 0.58
        print("after converting your amount ", round(temp, 3))
        print("thank you for using ")
        n = int(input("press 1 if you want to continue: \n"))
        if n == 1:
            self.option()
        else:
            print(" please visit again")
