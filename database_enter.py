import sqlite3
try:
    db = sqlite3.connect("app.db")
    cursor = db.cursor()
    with open("database.txt", 'r') as f:
        entry = f.read()
        print entry
    print("The database exists")
except:
    print("the file doesn't exists.")


cursor.execute('''CREATE TABLE app_data(player text, scored int, faced int,fours int,sixes int,bowled int,maiden int,given int,wkts int,catches int,stumping int,ro int, value int,ctg text)''')
L = entry.split("\n")
for t in range (1,16):
    e = tuple(L[t].split(" "))

    cursor.execute("INSERT INTO app_data VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", e)
db.commit()
cursor.close()
