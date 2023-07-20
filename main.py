import matplotlib.pyplot as plt
import numpy as np
import time
import random
class Bank_Account:
    def __init__(self):
        self.balance=0
        a=" WELCOME TO AGA BANKING SYSTEM "
        print("")
        print(" _________________________________________________")
        print("|                                                 |")
        print(a.center(51,'#'))
        print("|                                                 |")
        print(' `````````````````````````````````````````````````')
    def deposit(self):
        amount=int(input("Enter amount to be Deposited: "))
        self.balance += amount
        time.sleep(1)
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = int(input("Enter amount to be Withdrawn: "))
        time.sleep(1)
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
    def display(self):
        time.sleep(1)
        print("\n Net Available Balance=",self.balance)

class account:
    def __init__(self,amt) :       
        self.amount=amt
        amount=self.amount
    def deposit(self):
        q1=int(input("Enter amount to be Deposited: "))
        self.amount +=q1
        time.sleep(1)
        print("\n Amount Deposited:",q1)              
    def withdraw(self):
        q2 = int(input("Enter amount to be Withdrawn: "))
        time.sleep(1)
        if self.amount>=q2:
            self.amount-=q2
            print("\n You Withdrew:",q2)
            print("Your balance is " ,self.amount)
        else:
            print("\n Insufficient balance  ")
    def display(self):  
        time.sleep(1)
        print("\n Available Balance=", self.amount)         
def jhon():
    sum=0
    d2=True
    while sum<6:
        we=int(input("Enter the pin code : "))
        time.sleep(1)
        if we==8888:
            while d2==True:
                a=150000
                s1=account(a)
                time.sleep(1)
                print('''\nWe provide services like
                  1: Loan
                  2: Insurance
                  3: Create a upi ID
                  4: Credit card apply
                  5: Stock market
                  6: Withdraw
                  7: Deposit
                  8: Check the Balance
                  9: EXIT''')
                time.sleep(1)
                e1=input("enter : ")
                if e1==c:
                    time.sleep(1)
                    s1.withdraw()
                    
                elif e1==d:
                    time.sleep(1)
                    s1.display()
                    continue
                elif e1==po:
                    print("How much money do you want to apply for the loan")
                    print("The amount should be more than 50,000")
                    s6=int(input("Enter a amount : "))
                    if s6>=50000 and s6<=500000:
                        print("Do you want a loan of %d (yes/no)"%s6)
                        e2=input("Enter y/n : ")
                        if e2.lower()=='y':
                            print("\nYou are required to provide your pin for the transaction")
                            ew=int(input("Enter the pin : "))
                            if ew==jh:
                                time.sleep(1)
                                print("\nTransaction has been completed succesfully !")
                                print("Transaction can take a while to reach in your account")
                                time.sleep(1)
                                a=a+s6
                            else:
                                print("\nTransaction has been terminated due to incorrect pin number")
                                time.sleep(1)
                        else:
                            time.sleep(1)
                            print("\nThank you for your time")
                            time.sleep(1)
                    elif s6>500001:
                        time.sleep(1)
                        print("\nAmount is too HIGH !")
                        print("It should be less than 5,00,000")
                        time.sleep(1)
                    else:
                        time.sleep(1)
                        print("\nAmount too LOW !")                           
                elif e1==c2:
                    print("What sort of insurance are you Looking for ? ")
                    print('''
                    1 : Health insurance
                    2 : House insurance
                    3 : Education insurance''')
                    es=int(input("Enter : "))
                    if es==1:
                        print("\nWelcome To LIC")
                        print('\nAs individuals it is inherent to differ. Each individuals insurance needs and requirements are different from that of the others.\nLICs Insurance Plans are policies that talk to you individually and give you the most suitable options that can fit your requirement.')
                        print("Please choose from the option given below")
                        print('''
                        1 : LIC Bima Jyoti(Endowment Plan)
                        2 : LIC Bachat Plus(Endowment Plan)
                        3 : LIC Jeevan Umang(Whole Life Plan)''')
                        print("Choose an option : ")
                        ch=int(input(""))
                        if ch==1:
                            print('''
                                    Minimum Sum Assured : Rs:1,00,000
                                    Maximum Sum Asuured : No Limit
                                    Policy Term : 10yrs and 15yrs (5yrs)
                                    Minimum Entery Age : 90 days
                                    Maximum Entery : 60yrs
                                    Minimum Age at maturity : 18yrs
                                    Maximum Age at maturity : 75yrs''')
                            print("Do you want to apply for this Insurance :")
                            re=input("Enter(y/n) : ")
                            if re.lower()=='y':
                                print("\nApplication processing ...")
                                time.sleep(1)
                                print("Application has been sent to the firm ")
                                print("Further information will be notify via sms")
                                time.sleep(1)
                            else:
                                time.sleep(1)
                                print("\nThank you for your time")
                                time.sleep(1)
                        elif ch==2:
                            print('''
                                    Minimum Sum Assured : Rs:1,00,000
                                    Maximum Sum Asuured : No Limit
                                    Policy Term : 10yrs and 25yrs
                                    Minimum Entery Age : 90 days
                                    Maximum Entery : 70yrs
                                    Minimum Age at maturity : 16yrs
                                    Maximum Age at maturity : 75yrs''')
                            print("Do you want to apply for this Insurance :")
                            re=input("Enter(y/n) : ")
                            if re.lower()=='y':
                                print("\nApplication processing ...")
                                time.sleep(1)
                                print("Application has been sent to the firm ")
                                print("Further information will be notify via sms")
                                time.sleep(1)
                            else:
                                time.sleep(1)
                                print("\nThank you for your time")
                                time.sleep(1)
                        elif ch==3:
                            print('''
                                    Minimum Sum Assured : Rs:2,00,000
                                    Maximum Sum Asuured : No Limit
                                    Policy Term : (100-age at entry)years
                                    Minimum Entery Age : 90 days
                                    Maximum Entery : 55 yrs
                                    Age at maturity : 100 yrs''')
                            print("Do you want to apply for this Insurance :")
                            re=input("Enter(y/n) : ")
                            if re.lower()=='y':
                                print("\nApplication processing ...")
                                time.sleep(1)
                                print("Application has been sent to the firm ")
                                print("Further information will be notify via sms")
                                time.sleep(1)
                            else:
                                time.sleep(1)
                                print("\nThank you for your time")
                                time.sleep(1)            
                        else:
                            time.sleep(1)
                            print("\nINVALID SYNTAX")       
                            time.sleep(1)    
                    elif es==2:
                        print("\nPolicy Bazaar")
                        print("Home Insurance")
                        print('\nHome insurance provides cover against unforeseen incidents such as natural calamities (storms, floods, landslides) and man-made disasters such as (burglary, riots, theft, etc.).')
                        print('''Available House insurance
                        1 : Bharat Girha Raksha
                        2 : All in one home protector''')
                        se=int(input("Enter : "))
                        if se==1:
                            print('''
                            Strucure SI : Rs: 35L
                            Content SI : Rs: 7L
                            Premium/Month : Rs: 1,035''')
                            print("Do you want to apply for this Insurance :")
                            re=input("Enter(y/n) : ")
                            if re.lower()=='y':
                                print("\nApplication processing ...")
                                time.sleep(1)
                                print("Application has been sent to the firm ")
                                print("Further information will be notify via sms")
                                time.sleep(1)
                            else:
                                time.sleep(1)
                                print("\nThank you for your time")
                                time.sleep(1)                       
                        elif se==2:
                            print('''
                            Structure SI : Rs: 35L
                            Content SI : Rs: 7L
                            Premium/Month : Rs: 2,263''')
                            print("Do you want to apply for this Insurance :")
                            re=input("Enter(y/n) : ")
                            if re.lower()=='y':
                                print("\nApplication processing ...")
                                time.sleep(1)
                                print("Application has been sent to the firm ")
                                print("Further information will be notify via sms")
                                time.sleep(1)
                            else:
                                time.sleep(1)
                                print("\nThank you for your time")
                                time.sleep(1)                
                        else:
                            time.sleep(1)
                            print("\nINVALID SYNTAX")
                            time.sleep(1)   
                    elif es==3:
                        print("\nSBI - Education Insurance")
                        print('\nA Child Education Plan is an insurance policy that offers protection as well as an opportunity for saving money to ensure a secure future for your child.')
                        print('''Available Insurance
                        1 : Smart Champ Insurance
                        2 : Smart Scholar''')
                        se=int(input("Enter : "))
                        if se==1:
                            print('''
                            Annual Premium Range : Rs:6,000 onwards
                            Entery Age : child-0yrs, proposer-21yrs
                            ''')
                            print("Do you want to apply for this Insurance :")
                            re=input("Enter(y/n) : ")
                            if re.lower()=='y':
                                print("\nApplication processing ...")
                                time.sleep(1)
                                print("Application has been sent to the firm ")
                                print("Further information will be notify via sms")
                                time.sleep(1)
                            else:
                                time.sleep(1)
                                print("\nThank you for your time")
                                time.sleep(1)                        
                        elif se==2:
                            print('''
                            Annual Premium Range: Rs:24,000 onwards
                            Entry Age: Child-0yrs , Proposer : 18yrs
                            ''')
                            print("Do you want to apply for this Insurance :")
                            re=input("Enter(y/n) : ")
                            if re.lower()=='y':
                                print("\nApplication processing ...")
                                time.sleep(1)
                                print("Application has been sent to the firm ")
                                print("Further information will be notify via sms")
                                time.sleep(1)
                            else:
                                time.sleep(1)
                                print("\nThank you for your time")
                                time.sleep(1)       
                        else:
                            time.sleep(1)
                            print("\nINVALID SYNTAX ")              
                            time.sleep(1)
                    else:
                        time.sleep(1)
                        print("\nInvalid option")
                        time.sleep(1)
                elif e1==c3:
                    print("\nManage UPI ID")
                    print("\nEnter mobile number for generating the ID")
                    S=int(input(""))
                    if S>1000000000 and S<10000000000:
                        print("\nUPI ID has succesfully changed !")
                        print("UPI - %d@aga"%S)
                    else:
                        time.sleep(1)
                        print("\nINVALID number")
                        time.sleep(1)
                elif e1==c4:
                    print("\nDo you want to apply for credit card")
                    ds=input("Enter (y/n) : ")
                    if ds.lower()== 'y':
                        print("Enter your pin for verification")
                        pi=int(input())
                        if pi==8888:
                            print("\nDo you want to have the same credential as this account")
                            yr=input("Enter (y/n) : ")
                            if yr.lower()=='y':
                                print("\nProcessing....")
                                time.sleep(1)
                                print("write your address for the deliver")
                                a2=input("")
                                time.sleep(1)
                                print("\nIt will be delivered it to you soon !")
                                time.sleep(1)
                            else:
                                print("Enter the following to apply for the card")
                                es=input("Enter the name : ")
                                ed=int(input("Enter a phone number : "))
                                eq=int(input("Enter the pin code for the card : "))
                                print("\nProcessing....")
                                time.sleep(1)
                                print("Enter a address for the delivery")
                                sk=input("")
                                time.sleep(1)
                                print("\nIt will be delivered it to you soon !")
                                time.sleep(1)
                        else:
                            time.sleep(1)
                            print("\nIncorrect Password")
                            time.sleep(1)
                    else:
                        time.sleep(1)
                        print("\nThank you for your time")
                        time.sleep(1)
                elif e1==c5:
                    print("\nNSE(National Stock Exchange)")
                    print('\nPowered by millions of dreams, hopes and aspirations, India today is brimming with potential. \nAt NSE, we are driven by this ambition that makes India charge ahead and take a more prominent place on the global stage.')
                    print('''Top 3 Stock
                    1 : CoalIndia
                    2 : SbiLife
                    3 : HDFC''')
                    se=int(input('Enter a option : '))
                    if se==1:
                        print("\nCoal India Limited")
                        line_1 = np.random.randint(low = 30, high = 60, size = 50)
                        l=np.arange(10,60)
                        plt.plot(l,line_1, color = 'green', label = 'Coal India')
                        plt.ylabel('% Increase')
                        plt.xlabel("Time")
                        plt.title("NSE Stock market")
                        plt.legend()
                        plt.show()
                        print("Do you want to invest in this stock")
                        a=input("Enter(y/n) : ")
                        if a.lower()=='y':
                            print("Enter an amount you would like to invest.\nNote that the amount should be less than 50,000")
                            s=int(input(""))
                            if s<=50000 and s>=10:
                                print("\nProcessing...")
                                time.sleep(1)
                                print("An amount of %d has been invested in Coal India limited"%s)
                                time.sleep(1)
                            else:
                                time.sleep(1)
                                print("\nAmount too high !")
                        else:
                            time.sleep(1)
                            print("\nThank you for your time")
                            time.sleep(1)
                    elif se==2:
                        print("\nSBI LIFE INSURANCE COMPANY LIMITED")
                        line_2 = np.random.randint(low = 30, high = 60, size = 50)
                        l=np.arange(10,60)
                        plt.plot(l,line_2, color = 'green', label = 'SBI Life')
                        plt.ylabel('% Increase')
                        plt.xlabel("Time")
                        plt.title("NSE Stock market")
                        plt.legend()
                        plt.show()
                        print("Do you want to invest in this stock")
                        a=input("Enter(y/n) : ")
                        if a.lower()=='y':
                            print("Enter an amount you would like to invest.\nNote that the amount should be less than 50,000")
                            s=int(input(""))
                            if s<=50000 and s>=10:
                                print("\nProcessing...")
                                time.sleep(1)
                                print("An amount of %d has been invested in SBI LIFE INSURANCE COMPANY LIMITED"%s)
                                time.sleep(1)
                            else:
                                time.sleep(1)
                                print("\nAmount too high !")
                        else:
                            time.sleep(1)
                            print("\nThank you for your time")
                            time.sleep(1)
                    elif se==3:
                        print("\nHOUSING DEVELOPMENT FINANCE CORPORATION LIMITED")
                        line_3 = np.random.randint(low = 0, high = 60, size = 50)
                        l=np.arange(10,60)
                        plt.plot(l,line_3, color = 'green', label = 'HDFC')
                        plt.ylabel('% Increase')
                        plt.xlabel("Time")
                        plt.title("NSE Stock market")
                        plt.legend()
                        plt.show()
                        print("Do you want to invest in this stock")
                        a=input("Enter(y/n) : ")
                        if a.lower()=='y':
                            print("\nEnter an amount you would like to invest.\nNote that the amount should be less than 50,000")
                            s=int(input(""))
                            if s<=50000 and s>=10:
                                print("\nProcessing....")
                                time.sleep(1)
                                print("An amount of %d has been invested in HOUSING DEVELOPMENT FINANCE CORPORATION LIMITED"%s)
                                time.sleep(1)
                            else:
                                time.sleep(1)
                                print("\nAmount too high !")
                        else:
                            time.sleep(1)
                            print("\nThankyou for your Time")
                            time.sleep(1)
                    else:
                        time.sleep(1)
                        print("\nThank you for your time")
                        time.sleep(1)
                elif e1.lower()==pe:
                    d2==False
                    return
                elif e1.lower()==dep:
                    time.sleep(1)
                    s1.deposit()
                else:
                    ("\nINVALID SYNTAX")
                    time.sleep(1)
        else:
            sum+=1
            a=5-sum
            if a<=0:
                break
            time.sleep(1)
            print("\nYou have \b times left",a)

dep='7'
c='6'
pe='9'
d='8'
y='1'
c2='2'
c3='3'
c4='4'
c5='5'
c6='6'
ex='3'
jh=8888
n='2'
po='1'
lop=True 
while lop==True:
    s = Bank_Account() 
    time.sleep(1)
    print("What can we help you with today !")
    time.sleep(1)
    print("Do you have an account in this bank")
    time.sleep(1)
    print('''Select any one of the following
    1: Yes
    2: NO
    3: EXIT''')
    l=input("Enter : ")
    time.sleep(1)
    if l.lower()==n:
        print("\nTo get started you need to depoasit a sum of amount")
        time.sleep(1)
        s.deposit()
        print("Also provide your Name")
        eqw=input("")
        time.sleep(1)
        print("Your Email ID")
        dae=input("")
        time.sleep(1)
        print("Your phone number")
        nop=int(input(""))
        da=random.randint(1000,10000)
        sp=da
        time.sleep(1)
        print("Your pincode is %d"%sp)
        time.sleep(1)
        e=True
        while e==True:
            print(''''\nWe provide services like
                  1: Loan
                  2: Insurance
                  3: Create UPI ID
                  4: Credit card apply
                  5: Stock market
                  6: Withdraw
                  7: Deposit
                  8: Check the Balance
                  9: EXIT''')
            time.sleep(1)
            e1=input("enter : ")
            if e1.lower()==c:
                s.withdraw()
                time.sleep(1)
                print("You have left only" ,s.display(),"in your account")
            elif e1.lower()==d:
                s.display()
            elif e1==po:
                    print("How much money do you want to apply for the loan")
                    print("The amount should be more than 50,000")
                    s6=int(input("Enter a amount : "))
                    if s6>=50000 and s6<=500000:
                        print("Do you want a loan of %d (yes/no)"%s6)
                        e2=input("Enter y/n : ")
                        if e2 =='y':
                            print("\nYou are required to provide your pin for the transaction")
                            ew=int(input("Enter the pin : "))
                            if ew==sp:
                                time.sleep(1)
                                print("\nTransaction has been completed succesfully !")
                                print("Transaction can take a while to reach in your account")
                                time.sleep(1)
                                sp+=s6
                            else:
                                print("\nTransaction has been terminated due to incorrect pin number")
                                time.sleep(1)
                        else:
                            time.sleep(1)
                            print("\nThank you for your time")
                            time.sleep(1)
                            continue
                    elif s6>500001:
                        time.sleep(1)
                        print("\nAmount is too HIGH !")
                        print("It should be less than 5,00,000")
                        time.sleep(1)
                    else:
                        time.sleep(1)
                        print("\nAmount too LOW !")
                        time.sleep(1)
            elif e1==c2:
                print("\nWhat sort of insurance are you Looking for ? ")
                print('''
                1 : Health insurance
                2 : House insurance
                3 : Education insurance''')
                es=int(input("Enter : "))
                if es==1:
                    print("\nWelcome To LIC")
                    print('\nAs individuals it is inherent to differ. Each individuals insurance needs and requirements are different from that of the others.\nLICs Insurance Plans are policies that talk to you individually and give you the most suitable options that can fit your requirement.')
                    print("Please choose from the option given below")
                    print('''
                    1 : LIC Bima Jyoti(Endowment Plan)
                    2 : LIC Bachat Plus(Endowment Plan)
                    3 : LIC Jeevan Umang(Whole Life Plan)''')
                    print("Choose an option : ")
                    ch=int(input(""))
                    if ch==1:
                        print('''
                                Minimum Sum Assured : Rs:1,00,000
                                Maximum Sum Asuured : No Limit
                                Policy Term : 10yrs and 15yrs (5yrs)
                                Minimum Entery Age : 90 days
                                Maximum Entery : 60yrs
                                Minimum Age at maturity : 18yrs
                                Maximum Age at maturity : 75yrs''')
                        print("Do you want to apply for this Insurance :")
                        re=input("Enter(y/n) : ")
                        if re.lower()=='y':
                            print("\nApplication processing ...")
                            time.sleep(1)
                            print("Application has been sent to the firm ")
                            print("Further information will be notify via sms")
                            time.sleep(1)
                        else:
                            time.sleep(1)
                            print("\nThank you for your time")
                            time.sleep(1)
                    elif ch==2:
                        print('''
                                Minimum Sum Assured : Rs:1,00,000
                                Maximum Sum Asuured : No Limit
                                Policy Term : 10yrs and 25yrs
                                Minimum Entery Age : 90 days
                                Maximum Entery : 70yrs
                                Minimum Age at maturity : 16yrs
                                Maximum Age at maturity : 75yrs''')
                        print("Do you want to apply for this Insurance :")
                        re=input("Enter(y/n) : ")
                        if re.lower()=='y':
                            print("\nApplication processing ...")
                            time.sleep(1)
                            print("Application has been sent to the firm ")
                            print("Further information will be notify via sms")
                            time.sleep(1)
                        else:
                            time.sleep(1)
                            print("\nThank you for your time")
                            time.sleep(1)
                    elif ch==3:
                        print('''
                                Minimum Sum Assured : Rs:2,00,000
                                Maximum Sum Asuured : No Limit
                                Policy Term : (100-age at entry)years
                                Minimum Entery Age : 90 days
                                Maximum Entery : 55 yrs
                                Age at maturity : 100 yrs''')
                        print("Do you want to apply for this Insurance :")
                        re=input("Enter(y/n) : ")
                        if re.lower()=='y':
                            print("\nApplication processing ...")
                            time.sleep(1)
                            print("Application has been sent to the firm ")
                            print("Further information will be notify via sms")
                            time.sleep(1)
                        else:
                            time.sleep(1)
                            print("\nThank you for your time")
                            time.sleep(1)    
                    else:
                        time.sleep(1)
                        print("\nThank you for your time")
                        time.sleep(1)                   
                elif es==2:
                    print("\nPolicy Bazaar")
                    print("Home Insurance")
                    print('\nHome insurance provides cover against unforeseen incidents such as natural calamities (storms, floods, landslides) and man-made disasters such as (burglary, riots, theft, etc.).')
                    print('''Available House insurance
                    1 : Bharat Girha Raksha
                    2 : All in one home protector''')
                    se=int(input("Enter : "))
                    if se==1:
                        print('''
                        Strucure SI : Rs: 35L
                        Content SI : Rs: 7L
                        Premium/Month : Rs: 1,035''')
                        print("Do you want to apply for this Insurance :")
                        re=input("Enter(y/n) : ")
                        if re.lower()=='y':
                            print("\nApplication processing ...")
                            time.sleep(1)
                            print("Application has been sent to the firm ")
                            print("Further information will be notify via sms")
                            time.sleep(1)
                        else:
                            time.sleep(1)
                            print("\nThank you for your time")
                            time.sleep(1)                        
                    elif se==2:
                        print('''
                        Structure SI : Rs: 35L
                        Content SI : Rs: 7L
                        Premium/Month : Rs: 2,263''')
                        print("Do you want to apply for this Insurance :")
                        re=input("Enter(y/n) : ")
                        if re.lower()=='y':
                            print("\nApplication processing ...")
                            time.sleep(1)
                            print("Application has been sent to the firm ")
                            print("Further information will be notify via sms")
                            time.sleep(1)
                        else:
                            time.sleep(1)
                            print("\nThank you for your time")
                            time.sleep(1)
                    else:
                        time.sleep(1)
                        print("\nThank you for your time")
                        time.sleep(1)                        
                elif es==3:
                    print("\nSBI - Education Insurance")
                    print('\nA Child Education Plan is an insurance policy that offers protection as well as an opportunity for saving money to ensure a secure future for your child.')
                    print('''Available Insurance
                    1 : Smart Champ Insurance
                    2 : Smart Scholar''')
                    se=int(input("Enter : "))
                    if se==1:
                        print('''
                        Annual Premium Range : Rs:6,000 onwards
                        Entery Age : child-0yrs, proposer-21yrs
                        ''')
                        print("Do you want to apply for this Insurance :")
                        re=input("Enter(y/n) : ")
                        if re.lower()=='y':
                            print("\nApplication processing ...")
                            time.sleep(1)
                            print("Application has been sent to the firm ")
                            print("Further information will be notify via sms")
                            time.sleep(1)
                        else:
                            time.sleep(1)
                            print("\nThank you for your time")
                            time.sleep(1)                        
                    elif se==2:
                        print('''
                        Annual Premium Range: Rs:24,000 onwards
                        Entry Age: Child-0yrs , Proposer : 18yrs
                        ''')
                        print("Do you want to apply for this Insurance :")
                        re=input("Enter(y/n) : ")
                        if re.lower()=='y':
                            print("\nApplication processing ...")
                            time.sleep(1)
                            print("Application has been sent to the firm ")
                            print("Further information will be notify via sms")
                            time.sleep(1)
                        else:
                            time.sleep(1)
                            print("\nThank you for your time")
                            time.sleep(1)    
                    else:
                        time.sleep(1)
                        print("\nINVALID OPTION")
                        time.sleep(1)                    
                else:
                    print("\nInvalid option")
                    time.sleep(1)
            elif e1==c3:
                print("\nManage UPI ID")
                print("\nEnter mobile number for generating the ID")
                S=int(input(""))
                if S>1000000000 and S<10000000000:
                    print("\nUPI ID has succesfully changed !")
                    print("UPI - %d@aga"%S)
                else:
                    time.sleep(1)
                    print("\nINVALID number")
            elif e1==c4:
                print("\nDo you want to apply for credit card")
                ds=input("Enter (y/n) : ")
                if ds.lower()== 'y':
                    print("Enter your pin for verification")
                    pi=int(input())
                    if pi==sp:
                        print("Do you want to have the same credential as this account")
                        yr=input("Enter (y/n) : ")
                        if yr.lower()=='y':
                            print("\nProcessing....")
                            print("write your address for the deliver")
                            a2=input("")
                            time.sleep(1)
                            print("\nIt will be delivered it to you soon !")
                            time.sleep()
                        else:
                            print("Enter the following to apply for the card")
                            es=input("Enter the name : ")
                            ed=int(input("Enter a phone number : "))
                            eq=int(input("Enter the pin code for the card : "))
                            print("\nProcessing....")
                            time.sleep(1)
                            print("Enter a address for the delivery")
                            sk=input("")
                            time.sleep(1)
                            print("\nIt will be delivered it to you soon !")
                            time.sleep(1)
                    else:
                        time.sleep(1)
                        print("\nINCORRECT PIN")
                        time.sleep(1)
                else:
                    time.sleep(1)
                    print("\nThank you for your time")
                    time.sleep(1)
            elif e1==c5:
                print("\nNSE(National Stock Exchange)")
                print('\nPowered by millions of dreams, hopes and aspirations, India today is brimming with potential. \nAt NSE, we are driven by this ambition that makes India charge ahead and take a more prominent place on the global stage.')
                print('''Top 3 Stock
                1 : CoalIndia
                2 : SbiLife
                3 : HDFC''')
                se=int(input('Enter a option : '))
                if se==1:
                    print("\nCoal India Limited")
                    line_1 = np.random.randint(low = 30, high = 60, size = 50)
                    l=np.arange(10,60)
                    plt.plot(l,line_1, color = 'green', label = 'Coal India')
                    plt.ylabel('% Increase')
                    plt.xlabel("Time")
                    plt.title("NSE Stock market")
                    plt.legend()
                    plt.show()
                    print("Do you want to invest in this stock")
                    a=input("Enter(y/n) : ")
                    if a.lower()=='y':
                        print("\nEnter an amount you would like to invest.\nNote that the amount should be less than 50,000")
                        s=int(input(""))
                        if s<=50000 and s>=10:
                            print("\nProcessing...")
                            time.sleep(1)
                            print("\nAn amount of %d has been invested in Coal India limited"%s)
                        else:
                            time.sleep(1)
                            print("\nAmount too high !")
                    else:
                        time.sleep(1)
                        print("\nThank you for your time")
                        time.sleep(1)
                elif se==2:
                    print("\nSBI LIFE INSURANCE COMPANY LIMITED")
                    line_2 = np.random.randint(low = 30, high = 60, size = 50)
                    l=np.arange(10,60)
                    plt.plot(line_2, color = 'green', label = 'SBI Life')
                    plt.ylabel('% Increase')
                    plt.xlabel("Time")
                    plt.title("NSE Stock market")
                    plt.legend()
                    plt.show()
                    print("Do you want to invest in this stock")
                    a=input("Enter(y/n) : ")
                    if a.lower()=='y':
                        print("Enter an amount you would like to invest.\nNote that the amount should be less than 50,000")
                        s=int(input(""))
                        if s<=50000 and s>=10:
                            print("\nProcessing...")
                            time.sleep(1)
                            print("\nAn amount of %d has been invested in SBI LIFE INSURANCE COMPANY LIMITED"%s)
                        else:
                            time.sleep(1)
                            print("\nAmount too high !")
                elif se==3:
                    print("\nHOUSING DEVELOPMENT FINANCE CORPORATION LIMITED")
                    line_3 = np.random.randint(low = 20, high = 60, size = 50)
                    l=np.arange(10,60)
                    plt.plot(l,line_3, color = 'green', label = 'HDFC')
                    plt.ylabel('% Increase')
                    plt.xlabel("Time")
                    plt.title("NSE Stock market")
                    plt.legend()
                    plt.show()
                    print("Do you want to invest in this stock")
                    a=input("Enter(y/n) : ")
                    if a.lower()=='y':
                        print("Enter an amount you would like to invest.\nNote that the amount should be less than 50,000")
                        s=int(input(""))
                        if s<=50000 and s>=10:
                            print("\nProcessing...")
                            time.sleep(1)
                            print("An amount of %d has been invested in HOUSING DEVELOPMENT FINANCE CORPORATION LIMITED"%s)
                        else:
                            time.sleep(1)
                            print("\nAmount too high !")
                    time.sleep(1)
                    print("\nThank you for your time")
                    time.sleep(1)
                else:
                    print("\nINVALID OPTION")
                    time.sleep(1)
            elif e1.lower()==pe:
                time.sleep(1)
                e==False
                break
            elif e1.lower()==dep:
                time.sleep(1)
                s.deposit()

            else:
                time.sleep(1)
                print('\nINVALID SYNTAX')
        
    elif l.lower()==y:  
        print("\nEnter your name:")
        time.sleep(1)
        l=input("")
        if l.lower()=='jhon':
            time.sleep(1)
            jhon()       
        else:
            time.sleep(1)
            print("\nINVALID SYNTAX")
    elif l.lower()==ex:
        print("\nThank you for visiting  AGA BANK")
        break
    else:
        print("\n INVALID SYNTAX")
        time.sleep(1)
        print('\n Try again')
        time.sleep(1)
