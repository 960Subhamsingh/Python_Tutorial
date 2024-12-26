
#  some requirments for the opening of accounts
'''
1. account holder name 
2. ifsc code
3. cif number 
4. type of account number
5. address
6. contect number
7. balance

transaction 
deposit'''

class Banking:
    Intrastrate= 0.06
    def __init__(self,account_name,account_number,IFSC,CIF,type_of_account,address,contact_number):
        self.account_name = account_name
        self.account_number = account_number
        self.IFSC = IFSC
        self.CIF = CIF
        self.type_of_account = type_of_account
        
        self.address = address
        self.contact_number = contact_number
        self.balance = 0  
        self.account_statement = []
        
    def transaction(self,amount):
        if self.balance< amount:
            print(f"sorry! you have incufficient balance")
            print(f"your balance is {self.balance}")
        else:
            print(f"transaction of {amount} is successfull")
            self.balance-=amount
            print(f"your balance is {self.balance}")
            d = {"type_":"dabit","trans_amount": amount,"user_balance":self.balance}
            self.account_statement.append(d)
        
    def deposit(self,amount):
            print(f"{amount} is successfully deposited")
            self.balance+=amount
            print(f"your final balance is {self.balance}")
            d = {"type_":"credit","trans_amount": amount,"user_balance":self.balance}
            self.account_statement.append(d)
            
    def apply_Interest(self,date):
        self.date = date 
        if self.balance >60000:
            interest= self.balance*banking.interest_rate
            self.balance+=interest
            d = {"date":self.date,"type_":"interest credit","interest amount":interest,"user_balance":self.balance}
            self.account_statement.append(d)
        
shree = Banking("shree vish","1234567","SBI********","EXD********","current","*******","********89")
neelam = Banking("neelam soni","1234567","PNB********","EXD********","saving","*******","********99")
shweta = Banking("shweta sigh","1234567","HDFC*******","EXD********","saving","*******","********79")


# shree.balance
# 0
# shree.transaction(5000) 
# sorry! you have incufficient balance
# your balance is 0
# shree.deposit(1000)
# 1000 is successfully deposited
# your final balance is 1000
# shweta.deposit(10000)
# shweta.deposit(150000)
# 10000 is successfully deposited
# your final balance is 10000
# 150000 is successfully deposited
# your final balance is 160000
# shweta.balance
# 160000
# shweta.account_statement
# [{'type_': 'credit', 'trans_amount': 10000, 'user_balance': 10000},
#  {'type_': 'credit', 'trans_amount': 150000, 'user_balance': 160000}]
# neelam.balance
# 0
# neelam.deposit(100)
# 100 is successfully deposited
# your final balance is 100
# shree.account_statement
# [{'type_': 'credit', 'trans_amount': 1000, 'user_balance': 1000}]
# neelam.account_statement
# [{'type_': 'credit', 'trans_amount': 15400000, 'user_balance': 15400000}]
# neelam.account_statement[-4:]
# [{'type_': 'credit', 'trans_amount': 100, 'user_balance': 100}]
# shree.account_statement[-5:]
# [{'type_': 'credit', 'trans_amount': 1000, 'user_balance': 1000}]
# neelam.apply_Interest("04-04-2024")
# neelam.balance
# 200
# neelam.deposit(100)
# 100 is successfully deposited
# your final balance is 300
# shree.apply_Interest("14-5-2024") 
# shree.balance
# 0
# shree.deposit(15000) 
# 15000 is successfully deposited
# your final balance is 16000
# shree.transaction(15)
# transaction of 15 is successfull
# your balance is 15985
# shree.balance
# 15985
# shree.apply_Interest("15-12-2024")
# shree.balance
# 15985

# class loanaccount(Banking):
#     rate_of_interest = 0.24
#     def __init__(self,account_number,loan_amount,account_name):
        
#         self.loan_amount = loan_amount
#         interest = loan_amount*loanaccount.rate_of_interest
#         self.payable_amount= loan_amount*interest
        
#     def approve_loan(self):
#         if self.balance>loan_amount:
#             print(f"congrats your loan has been passed")
#             print(f"your {loan_amount} has been successfully disbursed to your {self.account_number}")
#             interest = loan_amount*rate_of_interest
#             self.payable_amount= loan_amount*interest
    
#     def repay_amount(self,amount_):
#         self.payable_amount -= amount_
#         print(f"payment of {amount_} was successful")
#         print(f"payable amount is {self.payable_amount}")
     
# shree.account_number
# '1234567'
# shree = loanaccount("1234567",6000,"shree vish")
# shree.repay_amount(500)
# payment of 500 was successful
# payable amount is 8639500.0
 
 
 
