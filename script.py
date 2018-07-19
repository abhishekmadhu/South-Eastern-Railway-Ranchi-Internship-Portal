import pymongo

class Database(object):
	URI = "mongodb://admin:XOOvxd32349@mongodb16086-hello2.mj.milesweb.cloud:27017"
	DATABASE = None

	client = pymongo.MongoClient(URI)
	DATABASE = client['serly']

	a = "Hello"
	print(a)

	try: DATABASE.command("serverStatus")
	except Exception as e: print(e)
	else: print("You are connected!")
	client.close()