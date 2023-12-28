import time


water = 200
milk = 200
coffee = 100
pudia = 200 
collection = 0

class espresso :
                    water = 50
                    milk = 0
                    coffee = 18
                    price = 1.50
                    
class latte :
                    water = 200
                    milk = 150
                    coffee = 24
                    price = 2.50
                    
class cappuccino :
                    water = 250
                    milk = 100
                    coffee = 24
                    price = 3
                    
class bournvita :
                    milk = 50 
                    pudia = 100
                    sugar = 10
                    price = 5
def coin_collector() :
                    a = int(input("Any  Penny's   : "))
                    b = int(input("Any  Nickel's  : "))
                    c = int(input("Any  Dime's    : "))
                    d = int(input("Any  Cent's    : "))
                    
                    return convertor(a,b,c,d)
                                        
def convertor(a,b,c,d) :
                    a = a*0.01
                    b = b*0.05
                    c = c*0.10
                    d = d*0.25
                    return a,b,c,d
def resource_checker(classname) :
                    global water , coffee , milk , collection 
                    if water>=classname.water and coffee>=classname.coffee and milk>=classname.milk :
                                        return True
                    else :
                                        return False
                    
def process(classname) :
                    global water , coffee , milk , collection
                    
                    print("PROCESSING YOUR COFFEE!!!")
                    time.sleep(10)
                    print("HERE'S YOUR COFFEE , HAVE A NICE DAY")
                                                                                                    
                    water -= classname.water 
                    milk -= classname.milk
                    if classname == "bournvita" :
                                        pudia -= classname.pudia 
                    else :
                                        coffee -= classname.coffee 
                    collection += classname.price
                    
                    
def flavour(classname) :
                    if resource_checker(classname) :
                                        print(f"SURE SIR , PLEASE PAY : {classname.price}$ [only coins accepted(penny,nickel,dime,quarter)] : ")
                                        a,b,c,d = coin_collector()
                                        if ( a+b+c+d ) >= classname.price  :
                                                            if ( a+b+c+d ) == classname.price : 
                                                                                print("TRANSACTION SUCCESSFUL")
                                                                                process(classname)
                                                            else :
                                                                                print(f"HERE'S YOUR CHANGE : {(a+b+c+d)-classname.price}$")
                                                                                print("TRANSACTION SUCCESSFUL")
                                                                                process(classname)
                                        else :
                                                            print("PROCESSING FAILED AS YOU DIDN'T PAY THE COMPLETE AMOUNT!!  ")
                    else :
                                        print("SORRY BRO INSUFFICIENT RESOURCES ........ CAN NOT PROCESS REQUEST")
                                       


print("         ................WELCOME TO THE CENTRAL PERK................ ")
print()
def start():
                    
                    opt = input(''' ....................DISPLAYING THE MENU................  
~ ESPRESSO
~ LATTE
~ CAPPUCCINO
` BOURNVITA
                                        
what would you like to order sir ? \n''')
                    global water , coffee , milk , collection
                    if opt.lower() == "espresso" :
                                        
                                        flavour(espresso)
                                        
                    elif opt.lower() == "latte" :
                                        
                                        flavour(latte)
                                        
                    elif opt.lower() == "cappuccino" :
                                        
                                        flavour(cappuccino)
                    
                    elif opt.lower() == "report" :
                                        print(f'''..........AVAILABLE RESOURCES................
                                                      WATER      : {water} ml
                                                      MILK       : {milk} ml
                                                      COFFEE     : {coffee} g
                                                      COLLECTION : {collection}$
                                                      
                     
                                                      
                                                      
                                                                                                ''')
                    elif opt.lower() == "bournvita" :
                                        if water>=bournvita.water and pudia>=bournvita.pudia and milk>=bournvita.milk :
                                                            print(f"SURE SIR , PLEASE PAY : {bournvita.price} [only coins accepted] : ")
                                                            a,b,c,d = coin_collector()
                                                            if ( a+b+c+d ) >= bournvita.price  :
                                                                                if ( a+b+c+d ) == bournvita.price : 
                                                                                                    print("TRANSACTION SUCCESSFUL")
                                                                                                    process(bournvita)
                                                                                else :
                                                                                                    print(f"HERE'S YOUR CHANGE : {(a+b+c+d)-bournvita.price}")
                                                                                                    print("TRANSACTION SUCCESSFUL")
                                                                                                    process(bournvita)
                                                            else :
                                                                                print("PROCESSING FAILED AS YOU DIDN'T PAY THE COMPLETE AMOUNT!!  ")
                                        else :
                                                            print("SORRY BRO INSUFFICIENT RESOURCES ........ CAN NOT PROCESS REQUEST")
                                                                                                    
                    else :
                                        print("MACHINE NOT RESPONSIVE!!!")
                    ask = input("would you like to order anything else  ?[yes/no] : \n") 
                    if ask.lower() == "yes" :
                                        start()
                    else :
                                        print("THANK YOU FOR YOUR VISIT SIR !!")
                                        
                                        
                                        
                                        
                                        
start()

                                                                                                     


















