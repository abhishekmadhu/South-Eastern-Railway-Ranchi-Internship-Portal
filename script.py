from pymongo import MongoClient

client = MongoClient("mongodb://admin:XOOvxd32349@mongodb16086-hello2.mj.milesweb.cloud:27017")
db = client.serly
a = "Hello"
print(a)

try: db.command("serverStatus")
except Exception as e: print(e)
else: print("You are connected!")
client.close()