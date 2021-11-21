import sqlite3  as sql
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('show')
parser.add_argument('table_name')
args=parser.parse_args()
table_name=args.table_name
isshow=args.show

print(table_name)


con=sql.connect("country.db")

curs=con.cursor()

curs.execute(" CREATE TABLE IF NOT EXISTS country(id integer PRIMARY KEY AUTOINCREMENT,name  text unique,capital text,population int) ")

while True:
   try: 

    countryname=input('Country:')
    capital=input('Capital:')
    popul=input('pop:')
    curs.execute('INSERT INTO country(name,capital,population) values(?,?,?)',(countryname,capital,popul))
    con.commit()
    res=curs.execute('select * from country')
    names = list(map(lambda x: x[0], curs.description))
    result=""
    result=' | '.join(f'{names}')
    print(result)

    print(res.fetchall())
    
   except KeyboardInterrupt:
       print('Exit') 
       exit()
   except Exception as ex:
       print(ex)    
con.close()
