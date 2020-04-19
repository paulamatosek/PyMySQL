import pymysql

class ConnectionConfig:
    def connection(self, user="tm_user", passwd="qwe123"):
        self.conn = pymysql.connect("localhost", user, passwd, "tm_db")
        if(self.conn):
            print("...połączono z bazą danych...")
        else:
            print("błąd połączenia")
        return self.conn
    def closeConnection(self):
        self.conn.close()
        print("...połączenie zakmniete...")

cc = ConnectionConfig()     # wywolanie kontruktora klasy
cc.connection()
cc.closeConnection()

def connection(user = "tm_user", passwd= "qwe123"):
    global conn     # zakres widoczności obiektu conn dotyczy całego skryptu
    conn = pymysql.connect("localhost", user, passwd, "tm_db")
    if(conn):
        print("...połączono z bazą danych...")
    else:
        print("błąd połączenia")
    return conn

def closeConnection():
    conn.close()
    print("...połączenie zakmniete...")

connection()
closeConnection()