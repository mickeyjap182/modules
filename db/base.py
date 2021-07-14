
class ConnectInfo():
    def __init__(self, *args, **kwargs):
        self.dbname = kwargs['file_path'] if 'file_path' in kwargs else ''
        if 'dbname' in kwargs:
            self.dbname = kwargs['dbname'] 
    def db_name(self):
        return self.dbname


class Factory(): 

    def __init__(self, db_class, connect_info:ConnectInfo, *args, **kwargs):
        # todo: init_script_path
        self.db_class = db_class
        self.connect_info = connect_info


    def create(self):
        return DataStore(self.db_class, self.connect_info)

class DataStore():

    def __init__(self, db, connect_info):
        self.db = db(connect_info)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        del self.db


    def execute(self, query, **kwargs):
        params = kwargs.pop('params') if 'params' in kwargs else None
        return self.db.execute(query, params, **kwargs)
    def select(self, query, **kwargs):
        params = DataStore.paramerter(**kwargs)
        return self.db.select(query, params, **kwargs)

    def begin(self):
        return self.db.begin()
    def commit(self):
        return self.db.commit()
    def rollback(self):
        return self.db.rollback()
    def close(self):
        return self.db.close()
    def insert(self, query, **kwargs):
        params = DataStore.paramerter(**kwargs)
        params = paramerter(kwargs)
        kwargs['force'] = kwargs['force'] if 'force' in kwargs else False
        return self.db.insert(query, params, **kwargs)

    def update(self, query, **kwargs):
        params = DataStore.paramerter(**kwargs)
        kwargs['force'] = kwargs['force'] if 'force' in kwargs else False
        return self.db.update(query, params, **kwargs)
    def delete(self, query):
        return self.db.delete(query)




