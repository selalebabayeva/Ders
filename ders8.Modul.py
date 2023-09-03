# MODULLLAR 

# 1.Time.sleep Modulu/   time.sleep(5)

# 2. Datetime Modulu/  Format - print(datetime.strptime(a, "%Y.%m.%d"))

# 3. Time delta -Total sekonds /  print(x.total_seconds()) 

# 4. Math Modulu/ # Floor, round, ceil/ print(math.floor(a))/ sqrt





# import cowsay
# print(cowsay.cow("Hello world"))

# import cowsay
# print(cowsay.dragon("salam"))



# Time.sleep Modulu (Print etmekcun gozlemek)

# import time 

# time.sleep(5)

# print("Hello World")


# Time.sleep Modullunun qisa varianti as 

# import time as t
# t.sleep(3)
# print("Hello world")


# Datetime Modulu

# import time as t
# from datetime import datetime
# print(datetime.now())



# il, ay, gun

# import time as t
# from datetime import datetime
# print(datetime.now(). date())



# Format

# import time as t
# from datetime import datetime

# a = "2023.08.23"

# print(datetime.strptime(a, "%Y.%m.%d"))



# Time Delta 

# import time as t
# from datetime import  datetime, timedelta
# x = timedelta(seconds=60)
# print(x)

# import time as t
# from datetime import  datetime, timedelta
# x = timedelta(days= 7)
# print(x)


# Total sekonds (gunun icindeki saniyeler)

# import time as t
# from datetime import  datetime, timedelta

# x = timedelta(days = 1)
# print(x.total_seconds())


# import time as t
# from datetime import  datetime, timedelta

# x = timedelta(weeks = 1)
# print(x.total_seconds())


# Math Modulu  Floor Yuvarlasdirilmasi(asagi)

# import time as t
# from datetime import  datetime, timedelta
# import math

# a = 2.5
# print(round(a))
# print(math.floor(a))


# Round Yuvarlasdirilmasi(asagi ve hansi yaxindirsa)

# import time as t
# from datetime import  datetime, timedelta
# import math

# a = 2.5
# print(round(a))



# Cell yuxari Yuvarlaqlasdirir

# import time as t
# from datetime import  datetime, timedelta
# import math

# a = 2.5
# print(math.ceil(a))


# Kokalti(**)

# import time as t
# from datetime import  datetime, timedelta
# import math

# a = 16
# print(math.sqrt(a))


# Choise 

# import time as t
# from datetime import  datetime, timedelta
# import math
# from random import randint, choice

# x = [1,2,3,4,5,6,7,8,9,10]

# print(choice(x))


# 2 ustu 16

# import time as t
# from datetime import  datetime, timedelta
# import math
# from random import randint, choice

# print(math.pow(2,4)) 



# Os Modulu(Install elekem lazim deyil, daxilidir)

# (bu saat hardasizsa gosterir, sehife, fayl) 

# import os
# print(os.getcwd()) 

# papka duzelt(yarat)

# import os
# print(os.mkdir("test")) 

# ve ya terminalda mkdir test yazmaqla yaranir



# Requests (Xarici Modul)

# import requests 

# data = requests.get("https://oxu.az") 
# print(data.text) 





# Task

# bir program qur 
# sorushsun : Dogum gununuzu daxil edin 
# dogum gununu daxil etdikden sonra hesablasin : Siz heyatda xxxxxxxxxx saniye xxxxxxx deqiqe xxxxx saat xxxx gun xxx aydir ki movcudsunuz ve sizin xx yashiniz var  

# datetime, strpt time, total secondsdan istifade edilecek



from datetime import datetime
a = input("Dogum gununuzu daxil edin:")

bu_gun = datetime.now()

past = datetime.strptime(a,"%Y.%m.%d" )

netice = bu_gun - past 

san = netice.total_seconds()
san + int(san)
deq = int(san/60)
saat = int(deq/60)

gun = int(saat/24)
ay = int(gun/30)

yas = int(ay/12)

print(" siz heyatda "  + str(san) + " saniye "  + str(deq) +" deqiqe " +str(saat) + " saat " + str(gun) + " gun " + str(ay) + " gun " + str(ay) + " aydir ki movcudsunuz ve sizin " + str( yas) + " yasiniz var ")








