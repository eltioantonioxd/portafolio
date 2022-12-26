from pymongo import MongoClient

def clientMongo():
    try:
        MONGO_URI = 'mongodb://'
        client = MongoClient(
                    MONGO_URI,
                    username= 'brayan',
                    password='colocolo'
                )
        return client
    
    except ConnectionError as error:
        return error