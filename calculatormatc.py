# ope= input("choees opertotr \n + \t - \t * \t / \n chooes an option")
while True:
    ope= input("choees opertotr \n + \t - \t * \t / \t syop \n chooes an option \t")

    match ope:
        case '+':
            v1=int(input("Enter a value :"))
            v2=int(input("Enter a value :"))
            res=v1+v2
            print(f'{v1} + {v2} =',res)
        case '-':
            v1=int(input("Enter a value :"))
            v2=int(input("Enter a value :"))
            res=v1-v2
            print(f'{v1} - {v2} =',res)
        case '*':
            v1=int(input("Enter a value :"))
            v2=int(input("Enter a value :"))
            res=v1*v2
            print(f'{v1} * {v2} =',res)
        case '/':
            v1=int(input("Enter a value :"))
            v2=int(input("Enter a value :"))
            if v2!=0:
                res=v1/v2
                print(f'{v1} / {v2} =',res)
            else:
                print(f'{v1} is dividibale by 0 infinite ') 
        case "stop":
            exit()              


