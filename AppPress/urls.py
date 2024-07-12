from django.contrib import admin
from django.urls import path


from AppPress.views import detail, modals, modals_depot, modi_depot, profil, tarifs, type_dpnr, type_dpr, type_vet,historique
from Pressing import settings
from Pressing.views import add_img, save_img

urlpatterns = [
  
    path('depot/',modals_depot,name="modals_depot"),
    path('depots/',modi_depot,name="modifier"),
    path('type_vetement/',type_vet,name='type_vet'),
    path('type_retrait/',type_dpr,name='type_dpr'),
    path('type_nonretrait/',type_dpnr,name='type_dpnr'),
    path('Profile/',profil,name="profile"),
    path('tarif/',tarifs,name="tarif"),
    path('detail/',detail, name='detail'),
    path('save_img/',save_img, name='save_img'),
    path('img/',add_img, name='add_img'),
    path('histo/',historique, name='histo'),
    path('modal/',modals,name="modal"),# Inclusion des motifs de routage d'une application
]

