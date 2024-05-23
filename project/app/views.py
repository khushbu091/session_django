from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        password=request.POST.get('password')

        request.session['name']=name
        request.session['email']=email
        request.session['contact']=contact
        request.session['password']=password
        return render(request,'home.html')


def login(request):
    return render(request,'login.html')

def logindata(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        email1=request.session.get('email')
        print(email)
        password1=request.session.get('password')
        print(password)
        name=request.session.get('name')
        print(name)
        contact=request.session.get('contact')
        print(contact)
        if email==email1:
            if password==password1:
                return render(request,'dashboard.html')
        else:
            mag='email not matched'
            return render(request,'login.html',{'key':mag})

       
        

def dashboard(request):
    return render(request,'dashboard.html')
