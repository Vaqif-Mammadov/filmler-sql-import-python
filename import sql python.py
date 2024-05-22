import sqlite3

connection = sqlite3.connect("filmler.db")

cursor = connection.cursor()

def cedvel_yarat():
    cursor.execute("CREATE TABLE IF NOT EXISTS filmler (ad TEXT, rejissor TEXT, buraxilis_ili INT, muddet INT)")
    connection.commit()

def elave_et_data():
    cursor.execute("INSERT INTO filmler VALUES ('Inception', 'Christopher Nolan', 2010, 148)")
    connection.commit()

def dynamic_elave_et_data(ad, rejissor, buraxilis_ili, muddet):
    cursor.execute("INSERT INTO filmler VALUES (?, ?, ?, ?)", (ad, rejissor, buraxilis_ili, muddet))
    connection.commit()

def data_goster():
    cursor.execute("SELECT * FROM filmler")
    data = cursor.fetchall()
    for row in data:
        print(row)

def dynamic_data_goster(rejissor):
    cursor.execute("SELECT ad FROM filmler WHERE rejissor=?", (rejissor,))
    data = cursor.fetchall()
    for row in data:
        print(row)

def duzelt(old_muddet, new_muddet):
    cursor.execute("UPDATE filmler SET muddet = ? WHERE muddet = ?", (new_muddet, old_muddet))
    connection.commit()

def datani_sil(ad):
    cursor.execute("DELETE FROM filmler WHERE ad = ?", (ad,))
    connection.commit()

cedvel_yarat()
elave_et_data()

ad = input("Filmin adı: ")
rejissor = input("Rejissor: ")
buraxilis_ili = int(input("İl: "))
muddet = int(input("Müddət (dəqiqə): "))
dynamic_elave_et_data(ad, rejissor, buraxilis_ili, muddet)

rejissor = input("Axtarmaq istədiyiniz filmin rejissorunu qeyd edin: ")

# dynamic_data_goster(rejissor)
# data_goster()
# duzelt(148, 150)
# datani_sil("Inception")

connection.close()
