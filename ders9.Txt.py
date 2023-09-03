
# "r" texti oxumaq
# "a" textin uzerine yeni element elave etmek
# "w" movcud textin icindeki elementleri silir, yeni element elave edir

# Text Open le aciilir



# a = open("Test.txt", "r") 
# print(a.read())


# a = open("Test.txt", "a") 
# print(a.write("Aslan"))


# a = open("Test.txt", "a") 
# a.write(" " + "Aslan")

# a= open("test.txt").read()

# print(a)



# a = open("Test.txt", "w") 
# a.write(" " + "Elsen")

# a= open("test.txt").read()

# print(a)


# sorusmaq

# a = open("test.txt").read()

# if len(a) == 0:

#     a.open("test.txt","a")
#     a.write("Fuad")

# else:
    
#     a.open("test.txt","a")
#     a.write(" " + "Fuad")

# a = open("test.txt").read()

# print(a)







# a = open("test.txt")
# print(a.readline())


# a = open("test.txt")
# print(a.readlines())





# Task

# Siz heyatda 1216236105 saniye 20270601 deqiqe 337843 saat14076 gun 469 ay  aydirki varsiniz

# from datetime import datetime

# a = input("Dogum gununuzu daxil edin:")

# bugun = datetime.now()

# past = datetime.strptime(a, "%Y.%m.%d")

# netice = bugun - past

# san = netice.total_seconds()

# san = int(san)

# deq = int(san/60)

# saat = int(deq/60)

# gun = int(saat/24)

# ay = int(gun/30)

# yas = int(ay/12)

# print(" Siz heyatda " + str(san) + " saniye " + str(deq) + " deqiqe " + str(saat) + " saat" + str(gun) + " gun " +str(ay) + " ay " + " aydirki varsiniz ")




# Task
# proqram sorusur : 1 Spesifik Elementi Yazdir : 2 Fayli sil
# 1-i basanda spesifik elementleri ele kecirsin
# 2ni basanda example.txt faylini silsin




# a = input("Secim edin: (1) spesifik elementi qaytar(2) Butun melumatlari sil ve yeni melumat yaz: (3) Melumat")

# a = open("test.txt").read()

# if a == "1":

#         txt = input("Bazaya yeni ad elave edin:")

#         if len(a) ==0:
               
#            a = open("test.txt", "a")
#            a.write(txt)
#         else:
#               txt = input("Bazaya yeni ad elave edin:")
#               a = open("test.txt", "a")
#               a.write(" " +txt)

# elif a == "2":
#         txt = input("Butun melumatlari sil ve yeni melumat yaz:")
#         a.open("test.txt", "w")
#         a.write(txt)

# elif a == "3":
#         a = open("test.txt", "r").read()
#         c = a.split()
#         if len(c) ==0:
#           print("Bazada hec bir melumat yoxdur")
#         else:
#               print("Bazada " +str(len(c))+ " element var")
        

# else:
#         print("Duzgun daxil etmediniz")








        

        






