# SQL (Strukturlasdirilmis Sorgu dili)

# SQL KODLARI : 

# 1. SELECT *  FROM
# 2.CREATE TABLE IF NOT EXISTS
# 3. INSERT INTO
# 4. UPDATE data SET
# 5.DELETE FROM
# 6. ID INTEGER PRIMARY KEY AUTOINCREMENT





# import sqlite3

# db = sqlite3.connect("test.db")

# sql = db.cursor()

# sql.execute(" CREATE TABLE IF NOT EXISTS data(ad TEXT, soyad TEXT, yash INT)")


# sql.execute(" INSERT INTO data(ad,soyad,yash) VALUES ('Fuad', 'Aliyev', 20) ")

# db.commit()






# import sqlite3

# db = sqlite3.connect("test.db")

# sql = db.cursor()

# sql.execute(" CREATE TABLE IF NOT EXISTS data(ad TEXT, soyad TEXT, yash INT)")

# sql.execute( " SELECT *  FROM data ")

# for i in sql:

#     print(i)

#     db.commit()





# # Melumatari cekib hamisin atir, massiv gonderir

# print(sql.fetchall())
# db.commit()



# tek element cixarir

# print(sql.fetchone())
# db.commit()



# # xxxxx
# # Spesifik elementi (ad) qaytardi

# import sqlite3

# db = sqlite3.connect("test.db")

# sql = db.cursor()

# sql.execute(" CREATE TABLE IF NOT EXISTS data(ad TEXT, soyad TEXT, yash INT)")

# sql.execute( " SELECT soyad  FROM data ")

# print(sql.fetchone())

# db.commit()



# Datadan butun melumatlari cixar, harda ki, ad  Aliyevdir

# import sqlite3

# db = sqlite3.connect("test.db")

# sql = db.cursor()

# sql.execute(" CREATE TABLE IF NOT EXISTS data(ad TEXT, soyad TEXT, yash INT)")

# # sql.execute( " SELECT *  FROM data WHERE soyad = 'Aliyev' ")

# sql.execute( " SELECT soyad  FROM data WHERE soyad = 'Aliyev' ")

# print(sql.fetchone())

# db.commit()




# Update/ adi yenilemek

# import sqlite3

# db = sqlite3.connect("test.db")

# sql = db.cursor()

# sql.execute(" CREATE TABLE IF NOT EXISTS data(ad TEXT, soyad TEXT, yash INT)")

# sql.execute( " UPDATE data SET ad = 'Aslan' ")

# db.commit()





# import sqlite3

# db = sqlite3.connect("test.db")

# sql = db.cursor()

# sql.execute(" CREATE TABLE IF NOT EXISTS data(ad TEXT, soyad TEXT, yash INT)")

# ad = 'Huseyn'
# soyad = 'Eliyev'
# yash = 25

# sql.execute( f" INSERT INTO data (ad,soyad,yash) VALUES ('{ad}', '{soyad}', '{yash}')")

# db.commit()





# DELETE Silmek emri

# import sqlite3

# db = sqlite3.connect("test.db")

# sql = db.cursor()

# sql.execute(" CREATE TABLE IF NOT EXISTS data(ad TEXT, soyad TEXT, yash INT)")

# sql.execute(" DELETE FROM data")

# db.commit()



# spesifik elementi silmek ???


# import sqlite3

# db = sqlite3.connect("test.db")

# sql = db.cursor()

# ad = input('adi secin:')

# ad = input(" Adi secin:")

# sql.execute(" CREATE TABLE IF NOT EXISTS data(ad TEXT, soyad TEXT, yash INT)")

# sql.execute( f"DELETE FROM data WHERE ad == '{ad}' ")

# db.commit() 




# Data DB si yaratmaq Test Tablenin ADI



# import sqlite3

# db = sqlite3.connect('data.db')

# sql = db.cursor()

# sql.execute("""

            
#         CREATE TABLE IF NOT EXISTS test(ID INTEGER PRIMARY KEY AUTOINCREMENT, metn TEXT) 
            
#             """)

# sql.execute(" INSERT INTO test(metn) VALUES ('Hello World') ")
# sql.execute(" iNSERT INTO test(metn) VALUES ('PHP')") 

# db.commit()







#  ID 'Hello World'  'PHP'


# import sqlite3

# db = sqlite3.connect('data.db')

# sql = db.cursor()


# sql.execute("""

            
#         CREATE TABLE IF NOT EXISTS test(ID INTEGER PRIMARY KEY AUTOINCREMENT, metn TEXT) 
            
#             """)

# sql.execute(" INSERT INTO test(metn) VALUES ('Hello World') ")
# sql.execute(" iNSERT INTO test(metn) VALUES ('PHP')") 


# # db.commit()


# sql.execute(" SELECT * FROM test WHERE ID = 5")

# print(sql.fetchone())

# db.commit()



# ORDER BY 





# import sqlite3

# db = sqlite3.connect('data.db')

# sql = db.cursor()

# sql.execute("""

            
#         CREATE TABLE IF NOT EXISTS test(ID INTEGER PRIMARY KEY AUTOINCREMENT, metn TEXT) 
            
#             """)

# sql.execute("  INSERT INTO test (metn) VALUES ('Javascript') ")

# sql.execute("  INSERT INTO test (metn) VALUES ('Python') ")


# db.commit()




# DESC ASC - Elave edeni basa ve sona atmaq


import sqlite3 

db = sqlite3.connect('data.db')

sql = db.cursor()

sql.execute("""

            
        CREATE TABLE IF NOT EXISTS test(ID INTEGER PRIMARY KEY AUTOINCREMENT, metn TEXT) 
            
            """)

sql.execute(" INSERT INTO test (metn) VALUES  ('Javaskript') ") 
sql.execute(" SELECT * FROM test ORDER BY ID DESC ") 

for x in sql:

    print(x) 

db.commit()


# 
# LIMIT 


# import sqlite3

# db = sqlite3.connect('data.db')

# sql = db.cursor()

# sql.execute("""

            
#         CREATE TABLE IF NOT EXISTS test(ID INTEGER PRIMARY KEY AUTOINCREMENT, metn TEXT) 
            
#             """)

# sql.execute(" SELECT * FROM test LIMIT 1,3")

# for x in sql:
#     print(x)

#     db.commit()




# DISTINC emri ISTISNA dublikatlari cixarir



# import sqlite3

# db = sqlite3.connect('data.db')

# sql = db.cursor()

# sql.execute("""

            
#         CREATE TABLE IF NOT EXISTS test(ID INTEGER PRIMARY KEY AUTOINCREMENT, metn TEXT) 
            
#             """)


# # sql.execute(" SELECT DISTINC metn FROM test")

# sql.execute(" SELECT DISTINCT metn FROM test")


# for x in sql:
#     print(x)

#     db.commit()




# DROP  TABLE (Databazani silmir, TABLEni silir, temizleyir) 


# import sqlite3

# db = sqlite3.connect('data.db')

# sql = db.cursor()

# sql.execute(" DROP TABLE test")


# db.commit()




# KAZINO 

# import sqlite3

# from random import randint

# db = sqlite3.connect('data.db')

# sql = db.cursor()

# sql.execute(" CREATE TABLE IF NOT EXISTS data(login TEXT, password INT, cash INT)")
# db.commit()

# secim = int(input("""
                  
#         Secim edin : \n 
#         (1)Qeydiyyatdan kecin: \n
#         (2)Oyuna basla: \n 
#         (3)Istifadecini silin: \n 
#         (4)Melumat
                  
#                   """))

# if secim == 1:

#     login = input('Istifadecini daxil edin :')
#     password = int(input('Parolu daxil edin :'))
#     cash = int(input('Daxil etmek istediyiniz meblegi secin :'))


#     sql.execute(f" INSERT INTO data(login,password,cash) VALUES ('{login}','{password}', '{cash}')")

#     db.commit()

#     print('Siz ugurla qeydiyyatdan kecdiniz')


# if secim == 2:
#     login = input('Istifadecini daxil edin :')
#     password = int(input('Parolu daxil edin :'))
#     number = randint(1,2)

#     if number ==1:

#        sql.execute(f" UPDATE   data SET cash = cash + '{30}' WHERE login == '{login}' AND password == '{password}'  ")
#        db.coommit()

#        print('Siz qalib geldiniz')

#     elif number ==2:
#         sql.execute( f" UPDATE data SET cash = cash -'{10}' WHERE login == '{login}' AND password == '{password}'" )
#         db.commit()
#         print('Siz meglub oldunuz')





    #    if number == 2:
           
    #     sql.execute(f" UPDATE  SET data = cash = '{20}' WHERE login == '{login}' AND password == '{password}'  ")
    #     print('Siz uduzdunuz')





# Pandas


# import sqlite3

# from pandas import DataFrame

# from random import randint

# db= sqlite3.connect("data.db")





# ATM

# import sqlite3

# db = sqlite3.connect("atm.db")

# sql= db.cursor()

# sql.execute("CREATE TABLE IF NOT EXISTS atm (pin INT, cash INT)")

# sql.execute(" INSERT INTO atm(pin,cash) VALUES (8855, 300)")

# db.commit()

# pin = int(input(' Pin kodu daxil edin:'))

# sql.execute(f" SELECT pin FROM atm WHERE pin == '{pin}' ")

# if pin in sql.fetchone():
 

#     while True:

#         secim = int(input("""
                          
#         (1) Balansi yoxla \n           
#         (2) Kartdan pul cixar \n
#         (3) Karta medaxil et \n
#         (4) Pini deyish \n
#         (5) Cixis et

#                     """))  
    

#         if secim == 1:
       
#           sql.execute(f"SELECT cash FROM atm WHERE pin =='{pin}'")

#           print(sql.fetchone())

#           break

#         if secim == 2:

#             cash = int(input("Meblegi daxil edin:"))

#             sql.execute(f" UPDATE atm SET cash = cash -'{cash}' WHERE pin =='{pin}'")
            
#             db.commit()

#             print('Mebleg +' +str(cash))

#             break

#         if secim == 3:

#             cash = int(input("Meblegi daxil edin:"))

#             sql.execute(f" UPDATE atm SET cash = cash +'{cash}' WHERE pin =='{pin}'")
                    
#             db.commit()

#             sql.execute(f" SELECT cash FROM atm WHERE pin = '{pin}'")
                    
#             for x in sql:

#                 print('Umumi mebleg ' + str(x))
                    
#             break



#         if secim == 4:
            
#             pass1 = int(input(" Pini daxil edin"))
#             pass2 = int(input(" Pini tesdiq edin"))

#             if pass1 == pass2:
                            
#                 sql.execute(f" UPDATE atm SET pin == '{pass2}' WHERE pin = '{pin}'")
                    
#                 db.commit()

#                 print("Sizin pin ugurla deyisdirildi")
                
#                 break
            

#             else: 

#                 print("Sizin pin ugurla deyisdirilmedi")




#         if secim ==5:

#             print('Cixish edilir ...')
#             break



# else:
#     print("Pin yalnisdir")
       

  


   
       


    
                  

# # sql.execute("SELECT * FROM data")

# # data= sql.fetchall()

# # dt = DataFrame(data)

# # dt.to_excel("data.xlsx")







    

























