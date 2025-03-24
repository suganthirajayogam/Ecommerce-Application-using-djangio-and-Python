from django.shortcuts import render,redirect
from .models import Product, Category
from django.http import HttpResponse 
from django.contrib.auth import authenticate, login
from .models.customer import *
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
def index(request):
    # Fetch all products and categories
    # products = Product.get_all_products()
    # categories = Category.get_all_categories()
    # for category id purpose
    products=None
    categories=None
    categories = Category.get_all_categories()
    categoryid=request.GET.get('category')
    if categoryid:
        products=Product.get_all_products_by_categoriesid(categoryid)
    else:
        products=Product.get_all_products()
    
    # Prepare data dictionary
    data = {}
    data['products']=products
    data['categories']=categories
    
    
    # Debugging: Print to the console
    print(products)
    print(categories)
    
    # Render the template with the context data
    return render(request, 'index.html', data)


#FOR SIGNUP FUNCTION
def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    else:  # Handle POST request
        # Return a success message as plain text
        # print(request.POST)
        postdata=request.POST
        FirstName=postdata.get('firstname')
        LastName=postdata.get('lastname')
        Mobno=postdata.get('phonenumber')
        Emailid=postdata.get('email')
        Password=postdata.get('password')
        #validation start
        error_msg=None
        
        if not FirstName:
            error_msg="Firstname required"
        elif len(FirstName)<3:
            error_msg="Firstname must be at least 3 characters long"
        if not LastName:
            error_msg="Lastname required"
        elif len(LastName)<3:
            error_msg="Lastname must be at least 3 characters long"
        if not Mobno:
            error_msg="phone required"
        elif len(Mobno)<10:
            error_msg="phone must be at least 10 characters long"
        if not Emailid:
            error_msg="emailid required"
        elif "@" not in Emailid:
            error_msg="Invalid emailid"
        if not Password:
            error_msg="password required"
        elif len(Password)<8:
            error_msg="password must be at least 8 characters long"
        #validation end

            
        if not error_msg:
            customer=Customer(
                      FirstName=FirstName,
                      LastName=LastName,
                      Mobno=Mobno,
                      Emailid=Emailid,
                      Password=Password)

            customer.register()
            # return HttpResponse('Useer account created  successfully')
            return redirect('homepage')
        
        else:
           
            data={}
            values={
                'firstname':FirstName, #fields matching
                'lastname':LastName,
                'mobno':Mobno,
                'emailid':Emailid,
                'password':Password
            }
            
            data['error_msg']=error_msg
            data['values']=values 
            return render(request, 'signup.html',data)
    
    #login page
# def login_page(request):
#     # return HttpResponse("login page is working")
#     return render(request,'login.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("homepage")  # Ensure 'homepage' exists in urls.py
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")  # Make sure this file exists

# logout
def logout_user(request):
    logout(request)  # Logs out the user
    return render(request, "logout.html")
    
    
    
  
    # if request.method == "POST":
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')

    #     # Authenticate the user
    #     user = authenticate(request, username=email, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('homepage')  # Redirect to the homepage after successful login
    #     else:
    #         error_msg = "Invalid login credentials."
    #         return render(request, 'login.html', {'error_msg': error_msg})

    # return render(request, 'login.html')
    
