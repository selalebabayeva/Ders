
# List datatipi

# x = []     ve ya
# x = list()



# x = ["Fuad","Tural","Samir"]

# print(x[1])


# x.pop()       sonuncu elementi silir
# x.remove      spesifik elementi silmek 
# x.append      sona deyer elave edir
# x.insert      indeks daxil etmek
# len(x)        listin icindeki elementleri sayir
# sum(x)         listdeki elemetleri toplayir(reqemleri)
# x.reverse()      listi tersine cevirir


# a = ["Fuad", "Aysel", "Tural"]
# a.pop()
# print(a) 

# b = ["Fuad", "Aysel", "Tural"]
# b.remove("Tural")
# print(b) 

# c = ["Aysel","Aynur","Hikmet"]
# c.append("Hesen")
# print(c)

# c = ["Fuad", "Nurane", "Aygun"]
# c.insert(2, "Huseyn")
# print(c) 

# c = ["Fuad", "Nurane", "Aygun"]
# print(len(c))

# c = [1,2,3,4,5,6]
# print(sum(c))

# c = [1,2,3,4,5,6]
# c.reverse()
# print(c) 


# listin icinde list
# x= [[1,2,3], [4,5,6], [7,8,9]]
# print(x[1] [1])


# a = [1, "Fuad", True, 2.5]
# print(a[2]) 


# x = list(("Fuad","Aslan"))
# print(x) 


# a = ["Fuad","Tural", "Samir"]
# b = a.copy()
# print(a)


####



# x = ["Fuad","Tural", "Samir", "Mehemmed"]
# for i in x:
#     if "a" not in i:
#      print(i) 



# meyveler =["alma", "banan", "gilas","kivi"]
# newlist =[]
# for x in meyveler:
#     if "a" in x:
#         newlist.append(x)
#         print(newlist)


# print(type(meyveler))


# Task

# x = ["Aslan", "Firudin","Nurane", "Aydin"]
# print(x[1]) 


# # test list 
# a = [5,6,[], 3, [], [], 9]
# del a[2]
# print(a) 



# s3 = [6,12,-8,"a","b"]
# del s3[4] 
# print(s3)


# x = [5,6,[], 3, [], [], 9]
# del x [4] 
# print(x) 

# x = [5,6,[], 3, [], [], 9]
# for i in range(6):
#     print(i)





# ad = input(" ad daxil edin:")

# if ad == " Aslan":
#    print("Aslan emiogludur")
# elif ad == "Afaq":
#  print("Afaq bibi qizidir")

# elif ad == ("."):
#  print("siz ad daxil etmediniz")

# elif ad == "Murad":
#  print("Murad kimdir? Men onu xatirlamadim") 



# bir eded listimiz var adlardan ibaret
# bir eded input var sorusur ad daxil edin (1), Adi silin (2)
# 1i basanda yeni input acilacaq sorusacaq : ad elave edin  adi yaziriq enteri basiriq listden hemin adi silir
# 2ni basanda sorusur : silmey istediyiniz adi secin , adi yazib enteri basanda hemin adi listden silir
# error mesajlari: Ad daxil etmediniz,Ad cox uzundur maksimum 15 herf

# a = ["Ayten", "Aydin", "Tural"]

# a = input("ad elave edin:")

# b = input("ad silin:")

# a.remove("Aydin")
# print(a)



# ededin musbet ve ya menfi olmasini tapin

# a = int(input("a-nin qiymetini daxil edin:"))
# b = int(input("b- nin qiymetini daxil edin:"))

# c = a - b
# print(c)


# a = 10
# b = 4
# if a<10:
#     print("eded menfidir")
# else:
#     print("eded mwsbetdir")

a = ["Fuad", "Aslan", "Afaq"]
ad = int(input("ad daxil edin(1) ad silin(2)"))
if ad == 1: 
    s = input("ad daxil edin:")
    a.append(a)
    for i in a:
        print(i) 













