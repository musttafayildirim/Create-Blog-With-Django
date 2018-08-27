python manage.py migrate
python manage.py createsuperuser

#daha sonra oluþturacaðýmýz uygulamayý yazýyoruz...

python manage.py startapp article        þeklinde...


oluþturduðumuz tablolarý kullanmak için

python manage.py makemigrations

daha sonra tablolarýmý oluþturmak için 

python manage.py migrate

satýrýný çalýþtýrýyoruz...


eðer shell üzerinden iþlem yapmak istersek

python manage.py shell

komutunu önce çalýþtýrýyoruz bu bize Django nun shellini açýyor.

daha sonra 

from django.contrib.auth.models import User

komutu ile django.contrib.auth.models den User'ý import ediyoruz.

from article.models import Article
bu komutla da article.models den Article classýný import ediyoruz..

newUser = User(username = "denemeKullanici",password = "123")
newUser.save()
þeklinde bir kullaným yaparsak veritabanýna þifrelemeden parolamýzý yazýyoruz.


newUser2 = User(username = "denemeKullanici2")
newUser2.set_password("123")
newUser2.save()

þeklinde kullanýrsak parolamýzý þifreliyerek kaydediyoruz.

veya 

newUser3 = User() þeklinde User() classýndan bir tane user oluþturarak
newUser3.username = "denemeKullanici3"
newUser3.set_password("123")
newUser3.first_name = "Mustafa"
newUser3.save()

þeklinde ayrý ayrý giriþlerimizi yapabiliyoruz...

article = Article(title = "Django Shell Deneme", content ="Deneme yazýsý", author = newUser3)
þeklinde article giriþi yapabiliriz bundan sonra 
article.save()

yapmamýz gerekir....

article = Article.objects.create(title = "deneme article",content="32flkdjsdfdklsfj" , author =newUser3)
þeklinde kullanýrsak save etmeye gerek kalmadan Article.object.create diyerek oluþturuyoruz..

eðer burada article'mýzýn baþlýðýný deðiþtirmek istersek

article.title = "deneme þeklinde"
article.save() yapmamýz gerekiyor sonra..


Article.objects.all()
þeklinde kullanýrsak tüm articlarýmýz gelir

Article.objects.get(title = "deneme2") dersek deneme2 isimli articlimiz gelir

eðer bu  makaleyi

article = Article.objects.get(title = "deneme2")

þeklinde kullanýrsak

buna eriþebilir duruma geliyoruz..

article.title
dersek bize makalenin baþlýðýný verir
eðer article.delete()
þeklinde kullanýrsak makaleyi veritabanýndan sileriz

Article.objects.filter(title__contains = "den" )
þeklinde kullanýrsak içerisinde den geçen baþlýklarý alýyoruz.....

bu arkada bir tane sql sorgusuna çeviriliyor sorgumuz þu þekilde
select ... where title like '%den%'  þeklinde



static dosyalar resim javascript css dosyalarý olabilir.....
staticfilesýn  setting altýnda install appin altýnda olduðundan emin olmamýz gerekiyor.





þimdi user uygulamasý oluþturuyorum
python manage.py startapp user
dediðimiz zaman user diye bir uygulamamýz oluþacak


