MENU={
    "espresso":{
        "ingredients":{
            "water":50,
             "cofee":18,   
      },
      "cost":1.5,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
             "cofee":24,   
      },
      "cost":2.5,
},
"cappuchinu": 
    {
        "ingredients":{
            "water":250,
             "cofee":24,
             "milk": 100,   
      },
      "cost":3,
}
}
profit=0
resources= {
    "water": 300,
    "milk": 200,
    "cofee":100,
}

def is_resources_sufficent(order_ingred1ients):
  for item in order_ingred1ients:
   if order_ingred1ients[item]>= resources[item]:
     print(f"Sorry there is not enough{item}.")
     return False
   return True


def process_coins():
   
   print("Pleasw insert the coin")
   total=int(input("How many quarters?: "))*0.25
   total=int(input("How many dines?: "))*0.1
   total=int(input("How many nickels?: "))*0.05
   total=int(input("How many penneis?: "))*0.01

def  is_transaction_successful(money_recieved,drink_cost):
     if money_recieved>=drink_cost:
       change=round(money_recieved-drink_cost,2)
       print(f"here is the ${change}")
       global profit
       profit+=drink_cost
       return True
       
     else:
        print("not enough money")
        return False


def make_coffe(drink_name,order_ingredients):
  for item in order_ingredients:
    resources[item]-= order_ingredients[item]
  print(f"here is your{drink_name}")

is_on=True


while is_on:
  choice=input("What would you like? (espresso/latte/cappuccino): ")
  if choice == "off":
    is_on=False
  elif choice=="report":
    print(f"water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffe: {resources['cofee']}g")
    print(f"money:${profit}")
  else:
    drink=MENU[choice]
    if is_resources_sufficent(drink['ingredients']):
       payement=process_coins()
       if is_transaction_successful(payement,drink["cost"]):
         make_coffe(choice,drink['ingredients'])
      

      
    

