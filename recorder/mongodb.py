import os 

DB_PATH='~/ryandata/mongo'
DB_LOG_PATH='~/ryanlog/mongo/douban_expdb_log'

def start_mongo():
    os.system('mongod --fork --logpath '+DB_LOG_PATH+' --dbpath '+DB_PATH)


if __name__=='__main__':
    start_mongo()



