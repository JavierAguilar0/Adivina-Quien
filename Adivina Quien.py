import sqlite3

conn=sqlite3.connect('OnePiece.db')
c=conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS OnePiece (
    Nombre TEXT PRIMARY KEY,
    Humano REAL NOT NULL,
    Animal REAL NOT NULL,
    Logia REAL NOT NULL,
    Paramecia REAL NOT NULL,
    Zoan REAL NOT NULL,
    Manos REAL NOT NULL,
    Pistolas REAL NOT NULL,
    Arma REAL NOT NULL) """)

c.execute("INSERT INTO OnePiece VALUES ('Luffy',1,0,0,0,1,1,0,0)")
c.execute("INSERT INTO OnePiece VALUES ('Chopper',0,1,0,0,1,1,0,0)")
c.execute("INSERT INTO OnePiece VALUES ('Robin',1,0,0,1,0,1,0,0)")
c.execute("INSERT INTO OnePiece VALUES ('Brook',1,0,0,1,0,0,0,1)")
c.execute("INSERT INTO OnePiece VALUES ('Kaido',1,0,0,0,1,0,0,1)")
conn.commit()

c.execute("SELECT * FROM OnePiece")
OnePiece=c.fetchall()

database=[]

for row in OnePiece:        
    database.append({'nombre':row[0],'humano':bool(row[1]),'animal':bool(row[2]),'logia':bool(row[3]),'paramecia':bool(row[4]),'zoan':bool(row[5]),'manos':bool(row[6]),'pistolas':bool(row[7]),'arma':bool(row[8])},)

def take_chance(answer,property):
    if answer == "s":
        ans=True
    else:
        ans=False

    to_remove=[]
    for d in database:
        if d[property]!=ans:
            to_remove.append(d)

    for i in to_remove:
        database.remove(i)

ans=input("tu personaje es humano(S/N)")
take_chance(ans,"humano")
if ans=='s':
    ans1=1
else:
    ans1=0

ans=input("tu personaje es un animal(S/N)")
take_chance(ans,"animal")
if ans=='s':
    ans2=1
else:
    ans2=0

ans=input("tu personaje es usuario de una fruta tipo logia?(S/N)")
take_chance(ans,"logia")
if ans=='s':
    ans3=1
else:
    ans3=0

ans=input("tu personaje es usuario de una fruta tipo paramecia?(S/N)")
take_chance(ans,"paramecia")
if ans=='s':
    ans4=1
else:
    ans4=0

ans=input("tu personaje es usuario de una fruta tipo zoan?(S/N)")
take_chance(ans,"zoan")
if ans=='s':
    ans5=1
else:
    ans5=0

ans=input("tu personaje pelea con las manos?(S/N)")
take_chance(ans,"manos")
if ans=='s':
    ans6=1
else:
    ans6=0

ans=input("tu personaje pelea con armas de largo alcance?(S/N)")
take_chance(ans,"pistolas")
if ans=='s':
    ans7=1
else:
    ans7=0

ans=input("tu personaje pelea con armas de corto alcance?(S/N)")
take_chance(ans,"arma")
if ans=='s':
    ans8=1
else:
    ans8=0

if len(database)==1:
    print("tu personaje es "+database[0]["nombre"])
else:
    print("No logre adivinar tu personaje")
    print('cual era el personaje en el que estabas pensando?')
    ans9=input()
    c.execute("INSERT INTO OnePiece VALUES (?,?,?,?,?,?,?,?,?)",(ans9,ans1,ans2,ans3,ans4,ans5,ans6,ans7,ans8))
    conn.commit()

conn.close()