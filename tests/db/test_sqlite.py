import os, sys, unittest
import json

# It is required when you'll run the unittest. 
if __name__ == '__main__':
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    if path not in sys.path:
        sys.path.append(path)

from db.sqlite import *
from db.base import *
from tests.core import Config

dbname = os.path.join(Config.module_path, 'startnature.db') 

class TestSqlite(unittest.TestCase):

    def setUp(self):
            db = DataStore(Sqlite, ConnectInfo(dbname=dbname))
            db.begin()
            db.execute('''
              DROP TABLE IF EXISTS tests_stocks
            ''')
            db.commit()
            db.close()

    def tearDown(self):
        pass

    def test_query(self):
        # set your api token on your environment variable from issued at official site.
        conn = None
        conn2 = None
        try :
            print("dbname: {} ... use sqlite3 <dbname>".format(dbname)) 
            conn = DataStore(Sqlite, ConnectInfo(dbname=dbname))
            conn.begin()

            # conn.execute("ATTACH DATABASE '" + dbname + "' as 'tests'")
            conn.execute('CREATE TABLE tests_stocks (date text, trans text, symbol text, qty real, price real)')
            conn.commit()

            # Insert a row of data
            query_single = "INSERT INTO tests_stocks (trans, symbol, qty, price, date) VALUES (? , ?,  ?,  ?,  ?)"
            param_single = ('BUY','RHAT', 100, 5.14, '2006-01-05')
            conn.execute(query_single, params=param_single)

            query_multi = "INSERT INTO tests_stocks VALUES (? , ?,  ?,  ?,  ?)"
            param_multi = [
                ('2006-03-28', 'BUY', 'IBM', 1000, 45.0),
                ('2006-04-06', 'SELL', 'IBM', 500, 53.0)
            ]
            conn.execute(query_multi, params=param_multi)

            query_multi2 = "INSERT INTO tests_stocks VALUES (:date, :trans, :symbol, :qty, :price)"
            param_multi2 = [
                {'date':'2006-04-09', 'trans':'BUY',  'symbol':'MSFT', 'qty':1000, 'price':72.0},
                {'date':'2006-04-12', 'trans':'SELL', 'symbol':'APPL', 'qty':1200, 'price':66.0}
            ]
            conn.execute(query_multi2, params=param_multi2)
            conn.commit()
            conn.close()

            conn2 = DataStore(Sqlite, ConnectInfo(dbname=dbname))
            query2 = 'SELECT * FROM tests_stocks WHERE trans=:trans ORDER BY price'
            filter_buy = {'trans': 'BUY'}
            st = conn2.execute(query2, params=filter_buy)
            for row in st:
                print(row)

            conn2.close()

        except Exception as e:
            print("An error occurred:{} type:{}".format(e.args[0], type(e)))
            self.assertTrue(False)
            if conn is not None:
                conn.rollback()  
                conn.close()  
            if conn2 is not None:
                conn2.rollback()  
                conn2.close()  
        else : 
            self.assertTrue(True)
        finally :
            pass

if __name__ == '__main__':
    unittest.main()
