
# Class OOP (Oject Programming) Obyekt yonumlu prqramlasdirma


# __init__(name,surname): Baslat demek


# class Test():
#     print("Test")



# class Test():
#     def __init__(self):
#         print("init metodu cagirildi")

# a= Test() 


    

# class Masin():
#     def __init__(self,reng,il,at_gucu,motor):
#         self.reng = reng
#         self. il = il
#         self.motor = motor
#         self.at_gucu = at_gucu

# a = Masin("qara", 2015, 300, 5.5)   

# print(a.motor)
# print(a.motor,a.reng,a.at_gucu,a.il)




# class Masin():

#     def __init__(self,reng,il,at_gucu,motor):
#         self.reng = reng
#         self.il = il
#         self.at_gucu= at_gucu
#         self.motor = motor


#     def cagir(self):
#         # print("Reng: {} , Il: {} , At gucu:{} , Motor: {}".format(self.reng,self.il,self.at_gucu,self.motor))
#           print(f"Reng:{self.reng}, Il:{self.il}, At gucu: {self.at_gucu}, Motor: {self.motor}")

# a = Masin("qara",2015,300,5.5)   

# print(a.cagir())


# xxxx



# class Masin():

#     def __init__(self,reng,il,at_gucu,motor):
#         self.reng = reng
#         self.il = il
#         self.at_gucu= at_gucu
#         self.motor = motor

#     def __str__(self):
#         print(f" Reng:{self.reng}, Il: {self.il}, At gucu: {self.at_gucu}, Motor: {self.motor}")

# a = Masin("qara", 2015, 300, 5.5)
# a.__str__()




# class Company():
#     def __init__(self,ad,soyad,sirket,maas):
#         self.ad = ad
#         self.soyad =soyad
#         self.sirket=sirket
#         self.maas= maas

#     def cagir(self): 
#         print(f"Ad: {self.sirket}, Soyad:{self.soyad} Sirket:{self.sirket}, Maas: {self.maas}")

# a = Company("Fuad", "Aliyev", "Xalq bank", 1000)
# a.cagir()


# maasi artirmaq


# class Company():
#     def __init__(self,ad,soyad,sirket,maas):
#         self.ad = ad
#         self.soyad =soyad
#         self.sirket=sirket
#         self.maas= maas

#     def bonus(self):
#         self.maas+=300


#     def cagir(self): 
#         print(f"Ad: {self.sirket}, Soyad:{self.soyad} Sirket:{self.sirket}, Maas: {self.maas}")

# a = Company("Fuad", "Aliyev", "Xalq bank", 1000)
# a.bonus()
# a.cagir()



# Inhertions Miras

# class Company():
#     def __init__(self,ad,soyad):
#         self.ad= ad
#         self.soyad = soyad

#     def __str__(self):
#      print(f"Ad: {self.ad}, Soyad:{self.soyad}")
    

# class Test(Company):
#     pass 

# b = Test("Fuad", "aliyev")
# b.__str__()





# class calisan:
#     def __init__(self,isim,maas):

#       self.isim = isim
#       self.maas = maas

# calisan1 = calisan("Ali", 500)
# calisan2 = calisan("Mahemmed", 300)

# print(calisan1.isim)
# print(calisan2.maas)

# print(calisan1.__dict__)
# print(calisan2.__dict__)




























      




    











