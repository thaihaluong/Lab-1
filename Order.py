import pymongo


# Config MongoDB

uri = "mongodb://admin:admin@ds119598.mlab.com:19598/cafeteria"
client = pymongo.MongoClient(uri)
db = client.get_default_database()
# Get MENU collection
menu_items = db["menu"].find()
menu_items_length = db["menu"].count()
order_items = db["order"].find()
order_items_length = db["order"].count()

def pick(food):    
    for i in range(0,4):
        if food.lower()==menu_items[i]["name"].lower():
           x=menu_items[i]["price"]
    return x

for i in range(0,order_items_length):
    bill = 0

    for fud in range(0,len(order_items[i]["order"])):
        print(order_items[i]["customer"],"buys:",order_items[i]["order"][fud])
        bill +=pick(order_items[i]["order"][fud])
    print(order_items[i]["customer"],"'s bill is:",bill)
    print("==========")
