from django.urls import path 
from . import views

# http://127.0.0.1:8000/movies her zaman movies etiketini kullanıcaz bu yüzden catalog içindeki urls ye eklicez
# http://127.0.0.1:8000/movies/2 3 vs gibi bir değer gelirse
# http://127.0.0.1:8000/movies/search olursa bu durumda search metoduna gidicek
urlpatterns = [
    path('', views.index, name="movies"),
    path('<int:movie_id>', views.detail, name="detail"),# tipini int olarak belirttik 
    path('search', views.search, name="search"),
]