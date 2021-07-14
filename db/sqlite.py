import sqlite3
class Sqlite():
    """
    """
    def __init__(self, connect_info):
        """
        dbname: "aa/xxx.db" or ":memory:"
        """
        connection = ':memory:' if (connect_info is None) or (connect_info.db_name() is None) else connect_info.db_name()
        self.con = sqlite3.connect(connection)
        self.cur = self.con.cursor()

        # if it has create_function...

    def __del__(self):
        """
        destructor
        """
        pass

    def db_con(self, *args):
        """
        set or get connection.
        """
        if len(args) > 0 and args[0].__class__.__name__ == 'Connection':
            self.con =  args[0]
        return self.con
    def cursor(self):
        """
        set or get cursor.
        """
        if len(args) > 0 and args[0].__class__.__name__ == 'Cursor':
            self.cur =  args[0]
        return self.cur

    def close(self):
        """
        autocommit
        """
        if hasattr(self, "con") and hasattr(self.con, "close"):
            self.con.close()

    def execute(self, query, params, **kwargs):
        """
        execute
        """
        query_type = query[:6]

        # if factory exists, 
        if type(params).__name__ == 'dict' and len(params) > 0:
            return self.cur.execute(query, params)
        elif type(params).__name__ == 'tuple' and len(params) > 0:
            return self.cur.execute(query, params)
        elif type(params).__name__ == 'list' and len(params) > 0:
            return self.cur.executemany(query, params)
        else :
            # no param 
            return self.cur.execute(query)

    def select(self, query, params, **kwargs):
        """
        ret.fetchone()...iterator
        ret.fetchmany(size)
        ret.fetchall()
        """
        # if factory exists, 
        return self.cur.execute(query)

    def begin(self):
        """
        nothing to do.
        """
        pass

    def commit(self):
        if hasattr(self, "con") and self.con.in_transaction :
            self.con.commit()
        return True

    def rollback(self):
        if hasattr(self, "con") and self.con.in_transaction :
            self.con.rollback()
        return True

    def insert(self, query, params:tuple, force=False):
        return self.db.insert(query, force)

    def update(self, query, params:tuple, force=False):
        return self.db.update(query, force)
