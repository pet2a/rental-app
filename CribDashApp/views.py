from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactInquiryForm,AppartmentForm
from CribDashApp.models import Contact1, Apartments1, UserProfile1, Appartment1
from django.template.context_processors import request
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')
def register(request):
    if request.method == "POST":
        members = UserProfile1(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            mothers_name=request.POST['mothers_name'],
            fathers_name=request.POST['fathers_name'],
            address=request.POST['address'],
            gender=request.POST['gender'],
            phone_number=request.POST['phone_number'],
            national_id_number=request.POST['national_id_number'],
            email=request.POST['email'],
            password=request.POST['password'],

        )
        members.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')
def agents(request):
    return render(request, 'agents.html')
def contact(request):
    if request.method == "POST":
        mycontact=Contact1(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        mycontact.save()
        return redirect('/services')
    else:
        return render(request, 'contact.html')

def properties(request):
    return render(request, 'properties.html')
def propertysingle(request):
    return render(request, 'property-single.html')
def services(request):
    return render(request, 'services.html')
def starter(request):
    return render(request, 'starter-page.html')
def sunshine(request):
    return render(request, 'Sunshine_Eco_Homes.html')
def yellowstone(request):
    return render(request, 'Yellow-Stone homes.html')
def orangehouse(request):
    return render(request, 'Orange House.html')

def contact_agent(request):
    if request.method == 'POST':
        form = ContactInquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.agent_name = ', '.join(form.cleaned_data['agent_name'])  # Join multiple selections
            inquiry.save()  # Save the form data to the database
            messages.success(request, "Your message has been sent successfully.")
            return redirect('properties')
    else:
        form = ContactInquiryForm()

    return render(request, 'contact_agent.html', {'form': form})


def landlords_dashboard(request):
    if request.method == 'POST':
        form = AppartmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, 'Apartment listing has been successfully added!')
            return redirect('landlords_dashboard')  # No Redirect and a success page
    else:
        form = AppartmentForm()

    return render(request, 'landlords_dashboard.html', {'form': form})



def search_results(request):
    # Get the filter parameters from the GET request
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    location = request.GET.get('location')
    bedrooms = request.GET.get('bedrooms')
    sort_by = request.GET.get('sort_by', 'price_asc')  # Default to price ascending if not provided

    # Start the query to get apartments
    apartments = Apartments1.objects.all()

    # Apply filters based on the user's search criteria
    if min_price:
        apartments = apartments.filter(price__gte=min_price)
    if max_price:
        apartments = apartments.filter(price__lte=max_price)
    if location:
        apartments = apartments.filter(location__icontains=location)
    if bedrooms:
        apartments = apartments.filter(bedrooms=bedrooms)

    # Sorting by price (ascending or descending)
    if sort_by == 'price_desc':
        apartments = apartments.order_by('-price')
    else:
        apartments = apartments.order_by('price')

    # Render the search form along with the results in the same page
    return render(request, 'search_results.html', {'apartments': apartments})
