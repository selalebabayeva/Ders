# a = {"Anar", "Aslan"}
# a.add("Aydin")
# print(a) 

# a = {"Baki": "Paytaxt", "Naxcivan" : "region", "Azerbaycan": "Olke"}
# print(a["Baki"])
# print( a["Naxcivan"])
# print(a["Azerbaycan"])

# # print(["Azerbaycan"])
# # print(a["Baki"])
# # print(["Paytaxt"])

# ab = {"Azerbaycan": "Olke", "Amerika": "Qite"}
# print(ab["Azerbaycan"])
# print(ab["Amerika"])

# a = {"Azerbaycan": "Olke", "Amerika": "Qite"}
# print(a.keys()) 

# a = {"Azerbaycan": "Olke", "Amerika": "Qite"}
# print(a.items())


# a = {"Azerbaycan": "Olke", "Amerika": "Qite"}
# for x in a.keys():
#     print(x)

# a = {"Azerbaycan": "Olke", "Amerika": "Qite"}
# for j in a.values():
#     print(j)

# a = {"Azerbaycan": "Olke", "Amerika":["Qite", "yraimqite"]}
# print(a ["Amerika"][0])

# b = {"Anar":"Heyat", "Aygun":["Qonsu", "Qohum"]}
# print(b ["Aygun"] [0])


# a = {"Seher": "Baki", "Unvan": ["Serifzade", "Abbasov"]}
# print(a ["Unvan"] [0])



# a = {"Seher": "Baki", "Unvan": [["Serifzade", "Abbasov"]]}

# a.pop("Unvan")
# print(a)

# a = {"Baki": "Seher", 'Sumqayit': "qesebe"}
# a.pop('Sumqayit')
# print(a) 

# a = {"Baki": "Seher", 'Sumqayit': "qesebe"}
# a.popitem()
# print(a)

# a = {"Baki": "Seher", 'Sumqayit': "qesebe"}
# a.pop('Sumqayit')
# print(a)

# a = {"Baki": "Seher", 'Sumqayit': "qesebe"}
# a.update({"Baki": "Paytaxt"})
# print(a)


# a = {"Baki": "Seher", 'Sumqayit': "qesebe"}
# a.clear()
# print(a)

 

# a = {"Ad": "Aytac"}
# b = {"Ad": "Rafiq"}

# c = {
    
#     "child1": a,
#     "child2": b
#     }
# print(c)


# a = {"Aytac", "Afiq", "Aytac"}
# print(a)

# b = {5,6,7,8,9}
# print(b)

# b = {5,6,7,8,9}
# b.discard(7)
# print(b)

# a = {"Vaqif", "Nurane", "Gultac"}
# a.discard("Nurane")
# print(a)

# c = {"Nuray", "Elnur", "Konul"}
# c.discard("Elnur")
# print(c) 

# c = {1,2,3,4,5,6,7,8,9}
# c.remove(3)
# print(c)

# c = {"Nuray", "Elnur", "Konul"}
# c.remove("Nuray")
# print(c) 


# a = {1,2,3,4,5,6,}

# a.pop()

# print(a)

# c = {"Nuray", "Elnur", "Konul"}
# c.pop()
# print(c)


# a= {1,2,3,4,5,6,}

# a.add(7)
# print(a)

# c = {"Nuray", "Elnur", "Konul"}
# c.add("renka")
# print(c)



# set1 = {"Nuray", "Orxan"}
# set2= {1,2,3,4}
# set1.update(set2)
# print(set1)

# c = {"Nuray": "Elnur"}
# c.clear()
# print(c)




# a = (1,2,3)
# a = list(a)
# print(type(a))
# a.append(4)
# print(a)
# a= tuple(a)
# print(type(a))
# a.add(5)
# print(a) 


# a = ["Fuad", "Aslan", "Afaq"]
# ad = int(input("ad daxil edin"(1), "ad silin(2):"))
# if ad == 1: 
#     s = input("ad daxil edin:")
#     a.append(s) 
#     print(a)
#     for i in a:
#         print(i) 

#     if ad == 2:
#         s = input("ad silin:")
#         a.remove(s)
#         print(a)
#         for i in a:
#          print(i)


 

# a= {"Aslan": "Aytac", "Elnur": "Guler"}

# adlar = int(input("Keysleri yazdir(1), Valuesleri yazdir(2):"))
# if adlar == 1:
# #    c = input("Keysleri yazdir":)
#    for x in adlar.keys():
#      print(x(["Aslan"],["Elnur"]))
#      if adlar == 2:
#         # c = input("Valuesleri daxil edin":)
#         for x in adlar.values():
#            print(x(['Aytac'],["Guler"]))  

    






# a ={"Sheher": "Baki", "Unvan":"Serifzade"}
# for x in a.keys():
#     print(x)








# a = [1,2,3,4]
# a = tuple(a)
# print(type(a))



# a = (1,2,3,4,5,6,7,8)
# print(a.index(4))


# print(a.index(1)) tuple reqem
# listdeki sozlerin indeksi?






# a = (1,2,3)
# a.index(1)
# print(a)


# a = (1,2,3)
# print(a.index(1)) 



# bir eded listimiz var adlardan ibaret
# bir eded input var sorusur ad daxil edin (1), Adi silin (2)
# 1i basanda yeni input acilacaq sorusacaq : ad elave edin  adi yaziriq enteri basiriq listden hemin adi silir
# 2ni basanda sorusur : silmey istediyiniz adi secin , adi yazib enteri basanda hemin adi listden silir
# error mesajlari: Ad daxil etmediniz,Ad cox uzundur maksimum 15 herf

# a = ["Fuad", "Aslan", "Afaq"]
# ad = int(input("ad daxil edin(1), ad silin(2):"))
# if ad == 1: 
#     s = input("ad daxil edin:")
#     a.append(s) 
#     print(a)
#     for i in a:
#         print(i) 

#     if ad == 2:
#         s = input("ad silin:")
#         a.remove(s)
#         print(a)
#         for i in a:
#          print(i)


# Task


# a = (1,2,3,4,5)
# a = list(a)
# a.append(6)
# print(a)
# a = tuple(a)
# print(a)


# a = ["Fuad", "Aslan", "Afaq"]
# ad = int(inut("ad daxil edin(1) Ad silin(2)"))

# if ad ==1:
#     s = input("ad daxil edin:")
#     a.append(s)
#     print(a)
#     for a in a:
#         print(i)
# if ad ==2:
#     a = input("ad silin:")
#     a.remove(s)
#     print(a)
#     for i in a:
#         print(i)


# a ={"ad": "Fuad", "seher": "Baki"} 
# ad = int(input("secim edin(1) keys (2) Values:"))
# if ad ==1:
#    print(a.keys())
# if ad ==2:
#    print(a.values())

#    if ad == " ": 
#       print("xahis edirik secim edin:")

# import cowsay
# print(cowsay.cow("Hello world"))

# import cowsay
# print(cowsay.dragon("Hello barbie, A just eat you"))

# import cowsay
# print(cowsay.cow("Hello boy"))



# import time

# time.sleep(3)
# print("Aydin")

# import time 
# time.sleep(5)
# print("Hello baby")


# import time
# time.sleep(2)
# print("Welcome")





# import time as t
# t.sleep(3) 
# print("Hello world")

# import time as Y
# Y.sleep(5)
# print("Hello")

# import time as x
# x.sleep(4)
# print("Hello") 

# Datetime

# import time as t
# from datetime import datetime
# print(datetime.now())


# import time as t
# from datetime import datetime
# print(datetime.now(). date())

# import time as t
# from datetime import datetime
# print(datetime.now(). date())


# import time as t
# from datetime import datetime

# a = "2023.08.23"

# print(datetime.strptime(a, "%Y.%m.%d"))


# import time as t 
# from datetime import datetime
# a = "1985.02.13"

# print(datetime.strptime(a, "%Y.%m.%d"))


# # Time Delta 

# import time as t
# from datetime import datetime, timedelta
# x = timedelta(seconds=60) 
# print(x)


# import time as t
# from datetime import  datetime, timedelta
# x = timedelta(days= 7)
# print(x)

# import time as t
# from datetime import datetime, timedelta
# x = timedelta(weeks=2)
# print(x)

# import datetime as t
# from datetime import datetime, timedelta
# x = timedelta(weeks= 1)
# print(x)

# import datetime as t
# from datetime import datetime, timedelta
# x= timedelta(seconds=120)
# print(x)

# minutes veeks Total seconds

# import time as t
# from datetime import  datetime, timedelta

# x = timedelta(hours = 1)
# print(x.total_seconds())

# import time as t 
# from datetime import datetime, timedelta
# print(x.total_seconds()) 


# import time as t
# from datetime import  datetime, timedelta
# import math

# a = 2.5
# print(round(a))


# import time as t
# from datetime import datetime, timedelta
# import math
# a= 2.9
# print(math.floor(a))



# import time as t
# from datetime import  datetime, timedelta
# import math

# a = 16
# print(math.sqrt(a))



# import time as t
# from datetime import datetime, timedelta
# import math
# a= 3.7
# print(math.ceil(a))



# a = open("test.txt", "r")
# print(a.read())

# a = open("test.txt", "r")
# print (a.read())


# a = open("test", "a")
# print(a.write("Selale"))


# a = open("test.txt","a")
# print(a.write(" Aytac"))


# a = open("test.txt", "a")
# print(a.write(" O"))


# a = open("test.txt", "a") 
# print(a.write("Aslan"))


# a = open("test.txt", "a") 
# c = a.write("Aslan")
# print(c)





# a = open("test.txt", "a")

# a.write(" " +"Aslan")

# a = open("test.txt").read()

# print(a)



# a = open("test.txt", "w")

# a.write(" " +"Fuad")

# # a= open("test.txt").read()
# # print(a)





# a = open("test.txt")
# print(a.readline())



# a = open("test.txt")
# print(a.readlines())

# a= open("test.txt")
# print(a.readlines())



# a = ["Python", "Java", "Javaskript"]

# for x in a:

#     if "J" not in x:
#         print(x)



# a ={"Ad":"Fuad", "Soyad": "Eliyev", "Ish": ["Bank Respublika", 'Ekspres Bank']}

# print(a["Soyad"])

# # print(a["Ish"] [1]) 

# a["Ish"].append("Kapital bank")

# print(a)   



# a = [{
    
#     "id":"2489651045","type":"CreateEvent",
#       "actor":{"id":665991,"login":"petroav","gravatar_id":"","url":"https://api.github.com/users/petroav","avatar_url":"https://avatars.githubusercontent.com/u/665991?"},
#       "repo":{"id":28688495,"name":"petroav/6.828","url":"https://api.github.com/repos/petroav/6.828"},
#       "payload":{"ref":"master","ref_type":"branch","master_branch":"master","description":"Solution to homework and assignments from MIT's 6.828 (Operating Systems Engineering). Done in my spare time.","pusher_type":"user"},
#       "public":True,"created_at":"2015-01-01T15:00:00Z"}

# ]


# print("actor")["id"] [0]

# print(a[0]["actor"] ["id"])


# print(a[0]["publik"] [0])




# b ninnicindeki deyisenler burda yoxdursa, cni icine  deyisenleri at


# b = [1,2,3,4,5]

# c = [6,7,8,9,10]


# for x in b:
#     if x  not in c: 
#         c.append(x)
        
# print(c)




# a = open("test.txt").read()

# if len(a) == 0:

#     a.open("test.txt","a")
#     a.write("Fuad")

# else:
    
#     a.open("test.txt","a")
#     a.write(" " + "Fuad")

# a = open("test.txt").read()

# print(a)







    

































