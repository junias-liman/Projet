from datetime import datetime, timedelta
from django.shortcuts import render,redirect
from AppPress.models import depot_image, images, tarif
from AppPress.models import User, client, depot, vetement
import pyautogui
import time
from django.core.paginator import Paginator
# Create your views here.
"""
context={'type_vet':vetem}
{'clients':clnt,'vetem':vetem,'listes':liste}
{'Ajout':updt,"vetem":vetem}
"""
def date(date1_str, date2_str):
        # Conversion des chaînes de caractères en objets de type datetime
        date1 = datetime.strptime(date1_str, "%Y-%m-%d").date()
        date2 = datetime.strptime(date2_str, "%Y-%m-%d").date()
        
        # S'assurer que date1 est avant date2
        if date1 > date2:
            date1, date2 = date2, date1
        
        # Générer et afficher les jours entre les deux dates
        current_date = date1
        somme=0
        while current_date <= date2:
            mont=depot.objects.filter(date_depot__icontains=current_date)
            for i in mont:
                somme+=i.montant
            current_date += timedelta(days=1)
        return somme
def send_whatsapp_message(contact_name, message):
    # Assurez-vous que l'application WhatsApp Desktop est ouverte et active
    # Attendez quelques secondes pour basculer manuellement vers l'application WhatsApp Desktop
    time.sleep(5)

    # Cliquez sur la barre de recherche pour trouver le contact
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)
    
    # Tapez le nom du contact
    pyautogui.write(contact_name)
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    # Appuyez sur 'Enter' pour sélectionner le contact
    pyautogui.press('enter')
    time.sleep(1)
    
    # Tapez le message
    pyautogui.write(message)
    time.sleep(1)
    
    # Appuyez sur 'Enter' pour envoyer le message
    pyautogui.press('enter')
    
clnt=client.objects.all()
vetem=vetement.objects.all()
liste=depot.objects.all()

def type_vet(request): 
   
    types=vetement.objects.all()
    paginator = Paginator(types, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
      
    if request.GET.get('query1'): 
        print("ok")
        quest = vetement.objects.filter(libelle__icontains=request.GET.get('query1'))    
        print(quest)
        return render(request,'Vues/type_vet.html',context={"page_obj":page_obj,"query":quest})
    
    if request.method=="POST":
        if request.POST.get("modif"):
            
            forms=vetement.objects.get(pk=int(request.POST.get("modif")))
          
            forms.libelle=request.POST.get("libelle")
            
            forms.save()
               
            return render(request,"Vues/type_vet.html",{"types":types})
        elif request.POST.get("env"):
           
            forms=vetement.objects.get(pk=int(request.POST.get("env")))
           
            return render(request,"Vues/type_vet.html",{"types":types,"type_mod":forms})
        
        type=vetement(
            libelle=request.POST.get('libelle'),
            tarif=tarif.objects.get(pk=1)
        )
        type.save()
    return render(request,'Vues/type_vet.html',{"page_obj":page_obj})
  
    
def profil(request):
    inter=images.objects.all()
    
    return render(request,'Vues/profile.html',context={"util":User.objects.get(pk=1)})

def modals(request):

   
    return render(request,'Vues/model_depot.html' )

def modi_depot(request):
    
    if request.method=="POST":
        if request.POST.get("nret"):
            updt=depot.objects.get(pk=int(request.POST.get('nret')))
        if request.POST.get("mod"):    
            updt=depot.objects.get(pk=int(request.POST.get('mod')))
        
        if updt=="True":
            return redirect("table_depot")
        else:
            updt.Regler='True'
            updt.date_retrait=datetime.today().date()
            updt.save()
            if request.POST.get("nret"):
                return redirect('type_dpnr')
                
            return redirect('table_depot')
    
        
def detail(request):
    if request.POST.get('det'):
        chf=int(request.POST.get('det'))
        updt=depot.objects.get(pk=chf)
                
        results= depot_image.objects.filter(depot_id__id__icontains=chf) 
        paginator = Paginator(results, 4) 
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    
    if request.method=="POST": 
        if request.POST.get('add'):
            
            chf=request.POST.get('add')
            updt=depot.objects.get(pk=int(request.POST.get('add')))
            
            results= depot_image.objects.filter(depot_id__id__icontains=chf) 
            updt=depot.objects.get(pk=int(request.POST.get('add')))
            if updt=="True":
                  return render(request,'Vues/détail.html',{"clt":updt,"liste":results} )

            else:
                updt.Regler='True'
                updt.date_retrait=datetime.today().date()
                updt.save()
                return render(request,'Vues/détail.html',{"clt":updt,"liste":results} )
        
        if  request.POST.get("num"):
            contact_name = request.POST.get("num")
        
            
            message = f"Mr/Mme {request.POST.get("name")} Pressing-Plus Viens par cette note vous informez que vos vetements sont prêts Vous êtes priez de venir les récupérer , le montant à versé est { request.POST.get("mont")} Francs Au cas contraire Voulez-vous etre livre ?"
            if contact_name:
                send_whatsapp_message(contact_name[2:], message)
            
            return redirect('table_depot')
                
       
    return render(request,'Vues/détail.html',{"clt":updt,"page_obj":page_obj} )
            
            

        
        
# Create your views here.
def type_dpr(request): 
    
    cnt=depot.objects.filter(Regler__icontains=1)
    paginator = Paginator(cnt, 10) 
    
    if request.GET.get("nbr"):
         paginator = Paginator(cnt,int(request.GET.get("nbr"))) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
     
    if request.GET.get('query1'):
       
        quest = depot.objects.filter(client__Lastname__icontains=request.GET.get('query1'))
      
        return render(request,'Vues/table_dpr.html',context={"page_obj":page_obj,"query":quest})

    if request.GET.get('query2'):
        print(request.GET.get('query2'))
        dates=datetime.strptime(request.GET.get('query2'),"%Y-%m-%d").date()
        quest = depot.objects.filter(date_depot__icontains=dates)
        for i in quest:
            print(i)
        return render(request,'Vues/table_dpr.html',context={"page_obj":page_obj,"query":quest})

       
    return render(request,'Vues/table_dpr.html',{"page_obj":page_obj})
  




def type_dpnr(request): 
    
    cnt=depot.objects.filter(Regler__icontains=0)
    paginator = Paginator(cnt, 10) 
    if request.GET.get("nbr"):
         paginator = Paginator(cnt,int(request.GET.get("nbr"))) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
     

    if request.GET.get('query1'):
       
        quest = depot.objects.filter(client__Lastname__icontains=request.GET.get('query1'))
      
        return render(request,'Vues/table_dpnr.html',context={"page_obj":page_obj,"query":quest})

    if request.GET.get('query2'):
        print(request.GET.get('query2'))
        dates=datetime.strptime(request.GET.get('query2'),"%Y-%m-%d").date()
        quest = depot.objects.filter(date_depot__icontains=dates)
        for i in quest:
            print(i)
        return render(request,'Vues/table_dpnr.html',context={"page_obj":page_obj,"query":quest})

       
    return render(request,'Vues/table_dpnr.html',{"page_obj":page_obj})






def modals_depot(request): 
    inter=images.objects.all()
    tar=tarif.objects.all()
    vetem=vetement.objects.all()
    if request.method=="POST":
        if request.POST.get('del'):
            images.objects.get(pk=request.POST.get('del')).delete()
            clt=int(request.POST.get('apt'))
            image=images.objects.filter(client__id__icontains=clt)
            return render(request,"Vues/model_depot.html",{"vetem":vetem,"id_client":clt,"img":image,"tarif":tar})
        
        if request.POST.get('depot'):
            ckk=client.objects.all()
           
            return  render(request,"Vues/model_depot.html",{"clients_dep":ckk})
            
        if request.POST.get('apt'):
            print(2)
            clt=int(request.POST.get('apt'))
            image=images.objects.filter(client__id__icontains=clt)
            return render(request,"Vues/model_depot.html",{"vetem":vetem,"id_client":clt,"img":image,"tarif":tar})
        
        if request.POST.get('depo'):
            print(3)
            clt=request.POST.get('clien')
            image=images.objects.filter(client__id__icontains=clt)
            return render(request,"Vues/model_depot.html",{"vetem":vetem,"id_client":clt,"img":image,"tarif":tar})
            
            
        if request.POST.get('clien'):
                print(1)
                clt=request.POST.get('clien')
                image=images.objects.filter(client__id__icontains=clt)
                forms=images(
                        client=client.objects.get(pk=clt),
                        type_vetements=vetement.objects.get(pk=int(request.POST.get('vet'))),
                        image=request.POST.get('img')
                                                        
                    )
                forms.save()
                return render(request,"Vues/model_depot.html",{"vetem":vetem,"id_client":clt,"img":image,"tarif":tar})
                
        
        
        if  request.POST.get('clnts'):
            formss=depot(
                    client=client.objects.get(pk=int(request.POST.get('clnts'))),
                    montant=int(request.POST['prix']),
                    date_depot=datetime.today().date(),
                    date_retrait=None
                    
                )
            formss.save()
           
            for i in list(request.POST.keys())[2:-1]:
                
                
                forms=depot_image(
                            depot=depot.objects.get(pk=formss.id),
                            photo=images.objects.get(pk=int(i))
                            
                            )
                forms.save()
            
            return redirect('table_depot')
            
            
            
        
        
       
    
    return render(request,"Vues/model_depot.html",context={'clients':clnt,'vetem':vetem,'listes':liste})

def tarifs(request): 
    cnt=tarif.objects.all()     
    paginator = Paginator(cnt, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if request.GET.get('query1'):  
        quest = tarif.objects.filter(Prix__icontains=int(request.GET.get('query1'))) 
        print(quest)
        return render(request,'Vues/tarif.html',context={"page_obj":page_obj,"query":quest})

    if request.GET.get('query2'):     
        quest = tarif.objects.filter(nbr_vet__icontains=int(request.GET.get('query2')))
        return render(request,'Vues/tarif.html',context={"page_obj":page_obj,"query":quest})  
    
    if request.method=="POST":  
        if request.POST.get("modif"):
            
            forms=tarif.objects.get(pk=int(request.POST.get("modif")))
          
            forms.nbr_vet=int(request.POST.get("nbr_vet"))
           
            forms.Prix=int(request.POST.get("prix"))
            forms.save()
               
            return render(request,"Vues/tarif.html",{"page_obj":page_obj})
        elif request.POST.get("env"):
            forms=tarif.objects.get(pk=int(request.POST.get("env")))
            return render(request,"Vues/tarif.html",{"page_obj":page_obj,"tarif_mod":forms})
        
        forms=tarif(
            nbr_vet=request.POST.get("nbr_vet"),
            Prix=request.POST.get("prix")
            )
        forms.save()
        
    return render(request,"Vues/tarif.html",{"page_obj":page_obj})


# Fonction pour générer et afficher les jours entre deux dates



def historique(request):
    clnt=client.objects.all()
    som_depot=0
    som_depr=0
    som_deprn=0
    som_clnt=0
    depo=depot.objects.all()
    depor=depo.filter(Regler__icontains=1)
    depon=depo.filter(Regler__icontains=0)
    for i in depo:
        som_depot +=i.montant
    for i in depor:
        som_depr +=i.montant
    for i in depon:
        som_deprn +=i.montant
    
    if request.method=="POST":
        if request.POST.get("vet"):
            depo_client=depo.filter(client_id__id__icontains=int(request.POST.get("vet")))
            for i in depo_client:
                som_clnt+=i.montant
            print(som_clnt)
            return render(request,'Vues/historique.html',{"depot":som_depot,"retrait":som_depr,"nonretrait":som_deprn,"client":clnt,"som_client":som_clnt})
        
        if  request.POST.get("dd") and request.POST.get("df"):
                somme=date(request.POST.get("dd"),request.POST.get("df"))
                print(somme)
                return render(request,'Vues/historique.html',{"depot":som_depot,"retrait":som_depr,"nonretrait":som_deprn,"client":clnt,"somme":somme})
        
        
            
    
    
    
    

    return render(request,'Vues/historique.html',{"depot":som_depot,"retrait":som_depr,"nonretrait":som_deprn,"client":clnt})

