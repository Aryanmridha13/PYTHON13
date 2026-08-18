balance = 10000
while True:
    operation= input("choess \n deposite \t widrawel \t blance \t cancel \n choees an option \t")

    match operation:
        case 'deposite':
            amt=int(input("Enter amount : "))
            balance+=amt
            print(f'{amt} add succsefully \n avalible amount is {balance}')
        case 'widrawel':
               amt=int(input("Enter amount :"))
               if amt>balance:
                    print(f"insaficient blance {balance}")
               else:
                    balance-=amt
                    print(f'{amt} widrewal sucsefull \n avilable blance is {balance}')
        case 'blance':
            print(f'avilabe blanece is = {balance} ')  
        case 'cancel':
              exit()              

                       