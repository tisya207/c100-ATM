class ATM:
    def __init__(self, card_no, pin):
        self.card_no=card_no
        self.pin=pin
    def check_balance(self):
        print('your balance is 5000RS.')
    
    def withdrawal(self,amount):
        new_amount=5000-amount
        print('balance= '+str(new_amount))

def main():
    number=input("insert your card no. ")
    pin=input('insert pin... ')
    new_user=ATM(number,pin)
    print('press 1 if you want to withdraw')
    print('press 2 for checking cash balance')
    option=int(input(''))
    if(option==1):
        amount=int(input('enter the amount... '))
        new_user.withdrawal(amount)
    elif(option==2):
        new_user.check_balance()
    else:
        print('enter a valid no.')

main()
            