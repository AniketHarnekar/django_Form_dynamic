from django.shortcuts import redirect, render,HttpResponse
from django.views import View
from msgapp.models import Message

#two type of views- classbase and function base view

# Create your views here.
def about(request):
    return HttpResponse("This is form about page")

class ContactForm(View):#two method get and post method
    def get(self,request,eid):
        #return HttpResponse("This is from class base view")
        return HttpResponse("Emp id "+eid)

def hello(request):
    return render(request,'hello.html') #return web page response we use render

def demo(request):
    #x="Itvedant" #using dictionory pass data from views to html
    d={}
    d['x']="Itvedant"
    d['y']=[1,2,3]
    #d={'x':'Itvedant'}
    d["a"]=2
    d["c"]=6
    d["d"]=4

    lst=[{'id':1,'name':'hardik','city':'pune'},{'id':2,'name':'Divya','city':'jalgaon'}]
    d['data']=lst

    return render(request,'demo.html', d) #render(request,'html file',dict)

def main(request):
    return render(request,'main.html')

def product(request):
    return render(request,'product.html')

def cart(request):
    return render(request,'cart.html')

def form(request):

    print(request.method)
    if request.method=="GET":
        return render(request,'form.html')
    else:
        name=request.POST['uname']
        email=request.POST['uemail']
        mob=request.POST['mob']
        msg=request.POST['msg']

        # print(name)
        # print(email)
        # print(mob)
        # print(msg)

        obj=Message.objects.create(name=name,email=email,mob=mob,msg=msg)
        obj.save()

        return render(request,"form.html")

def dashboard(request):
    obj=Message.objects.all()
    print(obj)
    context={}
    context['data']=obj
    #return HttpResponse("Data featched from database")
    return render(request,'dashboard.html',context)#data will not pass without dictionary
    

def delete(request,eid):

    obj=Message.objects.filter(id=eid)
    print(obj)
    obj.delete()
    #return render(request,"dashboard.html")#render shows that html page response

    return redirect('/dashboard')   #redirect is diffrent from render

    #return HttpResponse("Emp id "+eid)
    #filter the data we need to use object

def edit(request,eid):

    print(request.method)
    if(request.method=="GET"):
        obj=Message.objects.filter(id=eid)
        print(obj)
        context={}
        context['data']=obj

        return render(request,"edit.html",context)
    else:
        name=request.POST['uname']
        email=request.POST['uemail']
        mob=request.POST['mob']
        msg=request.POST['msg']

        # print(name)
        
        obj=Message.objects.filter(id=eid)
        obj.update(name=name,email=email,mob=mob,msg=msg)

        return redirect("/dashboard")

    
