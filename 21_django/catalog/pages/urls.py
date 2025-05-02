# ayrı ayrı hazırladığımız url yapılarını ana uygulamadaki url ye tanıtmamız gerekiyor
from django.urls import path # bunu eklememiz gerekiyor
from . import views

# http://127.0.0.1:8000 den sonra herhangi bir şey eklemicez o yüzden boş neresi çağırılacak views in altındaki index
# oluşturmuş olduğumuz url şema yapısına da bir isim verdik index diye /index dersen alta da index yazman gerekir

urlpatterns = [

    path('',views.index, name="index"), # views.indexi çağırıcaz o da response olarak h1 i yollicak
    path('about',views.about, name="about") # /about yazarsan about u çağıracak
]

