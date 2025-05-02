from django.apps import AppConfig

# uygulamayı temsil eden classtır yani bizim uygulamanın class ı pagesconfig
# bu class ne işe yaricak biz bu class ı alıcaz bizim root klasörü altındaki
# settings e gelicez INSTALLED_APPS e eklicez 

class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'
