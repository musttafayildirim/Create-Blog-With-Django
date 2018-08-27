python manage.py migrate
python manage.py createsuperuser

#daha sonra olu�turaca��m�z uygulamay� yaz�yoruz...

python manage.py startapp article        �eklinde...


olu�turdu�umuz tablolar� kullanmak i�in

python manage.py makemigrations

daha sonra tablolar�m� olu�turmak i�in 

python manage.py migrate

sat�r�n� �al��t�r�yoruz...


e�er shell �zerinden i�lem yapmak istersek

python manage.py shell

komutunu �nce �al��t�r�yoruz bu bize Django nun shellini a��yor.

daha sonra 

from django.contrib.auth.models import User

komutu ile django.contrib.auth.models den User'� import ediyoruz.

from article.models import Article
bu komutla da article.models den Article class�n� import ediyoruz..

newUser = User(username = "denemeKullanici",password = "123")
newUser.save()
�eklinde bir kullan�m yaparsak veritaban�na �ifrelemeden parolam�z� yaz�yoruz.


newUser2 = User(username = "denemeKullanici2")
newUser2.set_password("123")
newUser2.save()

�eklinde kullan�rsak parolam�z� �ifreliyerek kaydediyoruz.

veya 

newUser3 = User() �eklinde User() class�ndan bir tane user olu�turarak
newUser3.username = "denemeKullanici3"
newUser3.set_password("123")
newUser3.first_name = "Mustafa"
newUser3.save()

�eklinde ayr� ayr� giri�lerimizi yapabiliyoruz...

article = Article(title = "Django Shell Deneme", content ="Deneme yaz�s�", author = newUser3)
�eklinde article giri�i yapabiliriz bundan sonra 
article.save()

yapmam�z gerekir....

article = Article.objects.create(title = "deneme article",content="32flkdjsdfdklsfj" , author =newUser3)
�eklinde kullan�rsak save etmeye gerek kalmadan Article.object.create diyerek olu�turuyoruz..

e�er burada article'm�z�n ba�l���n� de�i�tirmek istersek

article.title = "deneme �eklinde"
article.save() yapmam�z gerekiyor sonra..


Article.objects.all()
�eklinde kullan�rsak t�m articlar�m�z gelir

Article.objects.get(title = "deneme2") dersek deneme2 isimli articlimiz gelir

e�er bu  makaleyi

article = Article.objects.get(title = "deneme2")

�eklinde kullan�rsak

buna eri�ebilir duruma geliyoruz..

article.title
dersek bize makalenin ba�l���n� verir
e�er article.delete()
�eklinde kullan�rsak makaleyi veritaban�ndan sileriz

Article.objects.filter(title__contains = "den" )
�eklinde kullan�rsak i�erisinde den ge�en ba�l�klar� al�yoruz.....

bu arkada bir tane sql sorgusuna �eviriliyor sorgumuz �u �ekilde
select ... where title like '%den%'  �eklinde



static dosyalar resim javascript css dosyalar� olabilir.....
staticfiles�n  setting alt�nda install appin alt�nda oldu�undan emin olmam�z gerekiyor.





�imdi user uygulamas� olu�turuyorum
python manage.py startapp user
dedi�imiz zaman user diye bir uygulamam�z olu�acak


