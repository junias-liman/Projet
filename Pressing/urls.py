"""
URL configuration for Pressing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from Pressing import settings
from .views import add_item, book_search, essai, home,modals_client,foot, SignAdmin,dashbord,login, modifier_type,route,headers, sign2, table_client,table_depot,save_items

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashbord/',dashbord,name='dashboard'),
    path('sign/',SignAdmin,name='sign'),
    path('route/',login,name='route'),
    path('client/',modals_client,name="modals_client"),

    path('',route,name="logout"),
    path('foot/',foot),
    path('entete/',headers),
    path('table_client/',table_client,name="table_client"),
    # path('table_depot/<int:direct>/<int:pos>/',table_depot,name="table_depot"),
    path('table_depot/',table_depot,name="table_depot"),
    path('formulaire_client/',sign2,name="forms"),
    path('AppPress/', include('AppPress.urls')),
    path('type/',modifier_type,name="modif"),
    path('home/',home,name="home"),
    #essai
    path('search/',book_search, name='book_search'),
    path('add-item/', add_item, name='add_item'),
    path('save-items/', save_items, name='save_items'),
    path('essai/',essai,name="essai")

    
]
# if settings.DEBUG:
#     print('ok')
#     urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# else:
#     print('notok')