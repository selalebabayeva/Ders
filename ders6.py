# Dictonary[luget]

# listden ferqli olaraq indeksi yoxdur, sirasizdir,
 
# Acar ve Deyer (Keys ve Value)




# print(a.keys())
# print(a.values())
# print(a.items())          
# print(a["Unvan"][0])
# print(a['Unvan'][0][1])    
# a.pop("Ad")                Pop hardan geldi gotutub silir, indexe muraciet etmek olmaz
# a.popitem()                sonuncu deyeri silir
# a.clear()
# print(a.get("Unvan"))      keysin deyerini silir
# a.discard(3)               silmek, cixmaq  remove kimi 
# a.remove(5)                silmek
# a. add(6)                  elave etmek
# a.update({"Baki": "Paytaxt"}) deyisdirir





















# a = {"Sheher": "Baki", "Unvan":"Serifzade"}
# print(a["Unvan"])


# keysleri(acarlari) ekrana cixardir

# a ={"Sheher": "Baki", "Unvan":"Serifzade"}
# print(a.keys())

# valuesleri (deyerleri) ekrana cixardir

# a ={"Sheher": "Baki", "Unvan":"Serifzade"}
# print(a.values())


# values ve keysleri ekrana cixardir

# a = {"Sheher": "Baki", "Unvan":"Serifzade"}
# print(a.items())

# a ={"Sheher": "Baki", "Unvan":"Serifzade"}
# for x in a.keys():
#     print(x) 


# a = {"Sheher": "Baki", "Unvan":["Serifzade", "Abbasov"]}
# print(a["Unvan"][0])


# a = {"Sheher": "Baki", "Unvan":[["Serifzade", "Abbasov"]]}
# print(a['Unvan'][0][1])


# Pop (sonuncu deyeri silir) Keysein deyerlerini silir
# a = {"Sheher": "Baki", "Unvan":[["Serifzade", "Abbasov"]]}
# a.pop("Unvan")
# print(a)

# Popitem (sonuncu deyeri silir)

# a = {"Sheher": "Baki", "Unvan":[["Serifzade", "Abbasov"]]}
# a.popitem()
# print(a) 


# Update (deyismek)
# a = {"Sheher": "Baki", "Unvan":[["Serifzade", "Abbasov"]]}
# a.update({"Sheher": "Sumqayit"})
# print(a) 


# Del (lugeti silir)
# a = {"Sheher": "Baki", "Unvan":[["Serifzade", "Abbasov"]]}
# del andprint(a)


# Clear (temizlemek)
# a = {"Sheher": "Baki", "Unvan":[["Serifzade", "Abbasov"]]}
# a.clear()
# print(a)

# a.get keysin deyerini silir
# a = {"Sheher": "Baki", "Unvan":[["Serifzade", "Abbasov"]]}
# print(a.get("Unvan"))


# Child family


# a = {"ad" : "Emil"}
# b = {"ad" : "Aslan"}

# c = {
    
#     "child1": a,
#     "child2": b
#     }
# print(c)


# Set Datatipi

# a = {"Fuad", "Aslan"}
# print(a)


# Set tekrarlanan elementi qebul etmir
# a = {1,2,3,4,5,5}
# print(a)



# Diskard (a.discard) Silmek a.remove kimi
# a = {1,2,3,4,5,5}
# a.discard(3)        
# print(a)

# a= {1,2,3,4,5} Remove
# a.remove(5)
# print(a) 

# a = {1,2,3,4,5}  Pop hardan geldi gotutub silir, indexe muraciet etmek olmaz
# a.pop()
# print(a) 

# Add(a.add) Metodu - Elave etmek
# a = {1,2,3,4,5}
# a. add(6)
# print(a)

# Update metodu birlesdirib qarisiq verir (dublikat goturmur)

# set1 = {"a", "b", "c", }

# set2 ={1,2,3}

# set1.update(set2) 

# print(set1)





# Tuple Datatipi () Deyisdirmek update elemek olmur

# a = (1,2,3)
# a.index(1)
# print(a)


# a = (1,2,3)
# print(a.index(1))


# a = (1,2,3)
# a = list(a)
# print(type(a))

# a = [1,2,3]
# a = tuple(a)
# print(type(a)) 



# Tuple metodu ( birlesdirmek)
# tuple1 = (1,2,3,4)
# tuple2 = (5,6,7,8,9)
# tuple3 = tuple1 + tuple2 
# print(tuple3)

# def my_function(country ="Norway"):
    














 

























# a = {"ad" : "Emil"}
# print(type(a))