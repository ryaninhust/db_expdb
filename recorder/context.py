from pymongo import Connection
from datetime import datetime
from pprint import pprint

db_info = "test"


class ContextError(Exception):
    pass


class ContextInitError(ContextError):
    pass

    
class ContextSaveError(ContextError):
    pass


class Context(object):
    
    def __init__(self,collection_name):
        self.collection=getattr(Connection().test,collection_name)
        self.data_dict={}
        

    def append(self,function_name,function_kwargs):
        self.data_dict[function_name]=function_kwargs
    
    def save(self):
        self.collection.save(self.data_dict)

    def find_one(self):
        return self.collection.find_one()
        
    def func_collector(self,function):
        def wrapper(*args,**kwargs):
            function_record_dict={}
            function_record_dict={}
            function_record_dict["args"]=kwargs
            result=function(*args,**kwargs)
            function_record_dict["result"]=result
            function_record_dict['timestamp']=datetime.now()
            self.append(function.__name__,function_record_dict)
            return result
        return wrapper
       
context=Context(db_info)









if __name__=="__main__":
    Context("testi")()
    print context.data_dict




