from django.shortcuts import render
from django.http  import HttpResponse  # response için bunu eklememiz gerekiyor

# Create your views here.
# views lar da bize kaynakla ilişkili olarak
# hangi html sayfasını getirmek istiyorsak onu getirecek

# def index(request):  # bir request alıcak bunun sonucunda da bir response döndürecek 
#     return HttpResponse("<h1>pages app ten merhaba </h1>")

# views içinde bir metot var metodu çalıştırdığında bir response döndürecek ve response içinde de bu şekilde
# bir h1 etiketi olucak yazı vs 
# tamam ama bu metotu nasıl çağırıcaz uygulama üzerinden nasıl bir talep yapıcaz bir url eklemeliyiz pages içerisine


def index(request):
    return render(request, 'pages/index.html')
# templates in altındaki pages ın altındaki index.html yi bul

def about(request):
    return render(request, 'pages/about.html')
# templates in altındaki pages ın altındaki about.html yi bul