from django.shortcuts import render,redirect,HttpResponse
from AppPress.models import client,User,depot,vetement,Item,Book
from django.core.paginator import Paginator
from datetime import datetime
from django.http import JsonResponse
import json








vetem=vetement.objects.all()
liste=depot.objects.all()
clnt=client.objects.all()
forms=User.objects.all()


# Create your views here.

def SignAdmin(request):
    if request.method=='POST':
            print(request.POST.get('mdp'),request.POST.get('mdp2'))
            if request.POST.get('mdp')==request.POST.get('mdp2'):
                print("liman")
                forms=User(
                Username=request.POST.get('fst'),
                Lastname=request.POST.get('lst'),
                Password=request.POST.get('mdp'),
                Identifiant=request.POST.get('usr'),
                Mail=request.POST.get('ema'),
                Number=request.POST.get('num'),
                Adresse=request.POST.get('add')
                    )
                
                forms.save()
        
    return render(request,"Vues/checkout.html")

def dashbord(request):
    
    return render(request,'Vues/index.html',{"nbr_clt":clnt.count(),"nbr_dep":liste.count(),"nbr_ret":liste.filter(Regler__icontains=1).count(),"nbr_nret":liste.filter(Regler__icontains=0).count(),})

def login(request):
        
        admin=request.POST.get('user')
        passwd=request.POST.get('pwd')
        
        for use in forms :
           
            if use.Identifiant==admin and use.Password==passwd:
                return redirect('dashboard')
            else:
                return HttpResponse('Authentification incorrecte')
        return render(request,'Vues/index.html')
def route(request):
        return render(request,'Vues/login.html')

def  modals_client(request):
    return render(request,'Vues/model_client.html')





def sign2(request):
    if request.method=="POST":
        if request.POST.get("apt"):
            forms=client.objects.get(pk=int(request.POST.get("apt")))
            return render(request,'Vues/model_client.html',context={"clients":forms,"reg":request.POST.get("apt")})
        else: 
            if request.POST.get("id"):
                updt=client.objects.get(pk=int(request.POST.get('id')))
                updt.Username=request.POST.get('first')
                updt.Lastname=request.POST.get('last')
                updt.Mail=request.POST.get('email')
                updt.Number=request.POST.get('numero')
                updt.Adresse=request.POST.get('adresse')
                updt.save()
                
            else:
                forms=client(
                        Username=request.POST.get('first'),
                        Lastname=request.POST.get('last'),
                        Mail=request.POST.get('email'),
                        Number=request.POST.get('numero'),
                        Adresse=request.POST.get('adresse')
                    )
                forms.save()
            return redirect('table_client')
    
def add_client(request):
            return render(request,'Press/add_client.html')
def tb(request):
    
    return render(request,'Press/tableau.html')


# Dans cette vue table de dépot il y'a une logique pour la paginaion de mes tables

def table_depot(request):
    cnt=depot.objects.all()
    paginator = Paginator(cnt, 10) 
    if request.GET.get("nbr"):
         paginator = Paginator(cnt,int(request.GET.get("nbr"))) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    if request.GET.get('query1'):
       
        quest = depot.objects.filter(client__Lastname__icontains=request.GET.get('query1'))
      
        return render(request,'Vues/table_depot.html',context={"page_obj":page_obj,"query":quest})

    if request.GET.get('query2'):
        print(request.GET.get('query2'))
        dates=datetime.strptime(request.GET.get('query2'),"%Y-%m-%d").date()
        quest = depot.objects.filter(date_depot__icontains=dates)
        for i in quest:
            print(i)
        return render(request,'Vues/table_depot.html',context={"page_obj":page_obj,"query":quest})

       
    return render(request,'Vues/table_depot.html',{"page_obj":page_obj})

        
        

def headers(request):
    return render(request,'Vues/header.html')


def foot(request):
    return render(request,'Vues/footer.html')



# la table du client



def table_client(request):
    cnt=client.objects.all()
    
    paginator = Paginator(cnt, 10)  
    if request.GET.get("nbr"):
         paginator = Paginator(cnt,int(request.GET.get("nbr"))) 
   
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    

    if request.GET.get('query1'):
        quest = client.objects.filter(Username__icontains=request.GET.get('query1'))
        return render(request,'Vues/table_client.html',context={"page_obj":page_obj,"query":quest,"btn_clt":request.GET.get("client")})
    if request.GET.get('query2'):
        quest = client.objects.filter(Mail__icontains=request.GET.get('query2'))
        return render(request,'Vues/table_client.html',context={"page_obj":page_obj,"query":quest,"btn_clt":request.GET.get("client")})
    if request.GET.get('query3'):
        quest = client.objects.filter(Number__icontains=request.GET.get('query3'))
        return render(request,'Vues/table_client.html',context={"page_obj":page_obj,"query":quest,"btn_clt":request.GET.get("client")})    
     
    
    return render(request,'Vues/table_client.html',context={"page_obj":page_obj,"btn_clt":request.GET.get("client")})

def essai(request):
    item_list = Item.objects.all()
    paginator = Paginator(item_list, 5)  # 10 items par page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Vues/AlertButton.html', {'page_obj': page_obj})
      
      
      
        
def modifier_type(request):
    pass
    # if request.method=="POST":
    #     if request.POST.get('modi'):
    #         upd.objects.get(pk=int(request.POST.get('modi')))
    #         if request.POST.get('vet'):
    #             updt.libelle=request.POST.get('vet')
    #         return render(request,'Vue.html',context={'type_modif':updt})
    #     if request.POST.get('modif'):
    #         upd.objects.get(pk=int(request.POST.get('modif')))
    #         if request.POST.get('vet'):
    #             updt.libelle=request.POST.get('vet')             
    #         return render(request,'Vues/type_vet.html',context={'type_vet':forms}) 
    
  
  

def home(request):
    
    return render(request,'Vues/home.html')

#essai

def add_item(request):
    if request.method == "POST":
        item_name = request.POST.get("name")
        # Vous pouvez faire des validations ici
        return JsonResponse({"name": item_name})

def save_items(request):
    if request.method == "POST":
        items_data = json.loads(request.POST.get("items"))
        for item in items_data:
            Item.objects.create(name=item['name'])
        return JsonResponse({"status":"success"})
    
 #----------------------------------------------------------------------------
 
def add_img(request):
    print('ok')
    if request.method == "POST":
        print('ok')
        iphoto = request.POST.get("photo")
        iclien = request.POST.get("clien")
        id = request.POST.get("depo")
        # Vous pouvez faire des validations ici
        return JsonResponse({"photo": iphoto,"clien":iclien,"depo":id})

def save_img(request):
    if request.method == "POST":
        items_data = json.loads(request.POST.get("items"))
        for item in items_data:
            Item.objects.create(name=item['name'])
        return JsonResponse({"status":"success"})
    
def book_search(request):
        query_params = request.GET
        books = Book.objects.all()

        title = query_params.get('title')
        author = query_params.get('author')
        genre = query_params.get('genre')

        if title:
            books = books.filter(title__icontains=title)
        if author:
            books = books.filter(author__icontains=author)
        if genre:
            books = books.filter(genre__icontains=genre)

        return render(request, 'Vues/recherche.html', {'books': books})



