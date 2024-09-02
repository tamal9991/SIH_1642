from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import ContactUs,DomainForm,Feedback,Forum_details,Stack_details
import google.generativeai as genai
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import random
import google.generativeai as genai
import os
#send otp

genai.configure(api_key="AIzaSyDuCFBnazuw5M2FbvoSAw1UupjbfjL16rE")
def send_otp(email):
    otp = random.randint(100000, 999999)  # Generate a 6-digit OTP
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    subject = 'Your OTP for Secure Access'
    message = f"""
       Dear User,

            For security purposes, we have generated a One-Time Password (OTP) to verify your identity. Please use the OTP below to complete your transaction or login process:

            Your OTP: {otp}

            This OTP is valid for the next [7 minutes/10 minutes]. Please do not share this code with anyone to ensure the security of your account.

            If you did not request this OTP, please ignore this email or contact our support team immediately at admin@gmail.com.

            Thank you for using our services.


"""
    send_mail(subject, message, email_from, recipient_list)
    return otp


#login page
def login_def(request):
    if request.method == 'POST':
        username = request.POST['username'] #fetch user from html
        password = request.POST['password'] # fetch password from html
        user = authenticate(username=username, password=password) # if user is exist
        if user is not None: 
                login(request, user) # login to user
                return redirect('/')  # Redirect to a different page after login
        else:
             return redirect('/login') #method is not post
    return render(request,'login.html') 

def request_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = send_otp(email)
        request.session['otp'] = otp  # Save OTP in session
        request.session['email'] = email  # Save email in session
        
        print('send mail')

    
def opt_verify(request):
    if request.method == 'POST':
        # fetch every user data from html
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        otp = request.POST['otp']
        otp_verify = request.COOKIES.get('otp_verify', 'No data provided')
        password1 = request.POST['password']
        print(otp_verify,otp)
        # Validate the data
        errors = []
        if not username or not email or not password1:
            errors.append("All fields are required.")
        try:
            validate_email(email)
        except ValidationError:
            errors.append("Invalid email address.")
        
        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'register.html')
        # Create the user
        try:
            if str(otp_verify )== str(otp):
                    user = User.objects.create_user(username=username, password=password1, email=email,
                                            first_name=first_name, last_name=last_name)
                    login(request, user)
                    return redirect('/domain')  # Redirect to a different page after registration
            else:
                return redirect('/opt_verify')
        except Exception as e:
            messages.error(request, str(e))
    return render(request,"otp_verify.html")


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        otp = send_otp(email)
        response = redirect('/opt_verify')
        response.set_cookie('otp_verify', otp)
        print('email send to {}'.format(email))
        return response
    else:
        print('wait')
    return render(request, 'register.html')


def logout_def(request):
    logout(request)
    return redirect('/')
    


def home(request):
    return render(request,'home.html')


# org details
def org_details(request):
    return render(request,'org_details.html')


def profile_def(request):
    userDetails = User.objects.get(id = request.user.id)
    return render(request,'profile_def.html',{'userDetails':userDetails})

def feed_back(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        rating = request.POST.get('rating')
        feedback = request.POST['feedback']
        feed_save = Feedback.objects.create(name = name,email=email,rating=rating,feedback=feedback)
        if feed_back is not None:
            subject = 'Thank You for Your Feedback!'
            message = f""" 
            Dear {name},

                        Thank you for taking the time to share your feedback with us. We have received your comments and suggestions, and we truly appreciate your input. Your feedback is invaluable as we strive to improve our services and provide a better experience for all our users.

                        Please know that your feedback has been forwarded to the relevant team, and we are committed to taking appropriate actions to address your concerns or consider your suggestions.

                        If you have any further comments, questions, or require assistance, feel free to reply to this email or contact our support team at admin@gmail.com . We're here to help!

                        Once again, thank you for helping us make our platform better. We look forward to serving you in the future.
                    """
            email_from = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)
        return redirect('/')
    return render(request,'fed_back.html')

def about_us(request):
    return render(request,'about_us.html')

def contect_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contect_us = ContactUs.objects.create(name=name,email=email,message=message)
        return redirect("/contect")
    
    return render(request,'contect_us.html')

def domain_form_stack(request):
    
    return render(request,'domain_form_stack.html')


def domain_def(request):
    if request.method == 'POST':
        org_name = request.POST['org_name']
        idea = request.POST['idea']
        location = request.POST['location']
        contact_no = request.POST['contact_no']
        domain_save = DomainForm.objects.create(user = request.user,org_name=org_name,idea=idea,
                                                location=location,contact_no=contact_no)
        print(domain_save)
        return redirect('/domain_form_stack')
    return render(request,'domain_def.html')

def forms_def(request):
    if request.method == 'POST':
        ask_question = request.POST['ask_question']
        Collaboration = request.POST['Collaboration']
        problem = request.POST['problem']
        resources = request.POST['resources']
        Forum_details.objects.create(user = request.user,ask = ask_question,call = Collaboration,pro = problem,
                                     res = resources)
        return redirect('/domain_form_stack')
    return render(request,'forms_def.html')

def stack_def(request):
    if request.method == 'POST':
        role = request.POST['role']
        Equity = request.POST['Equity']
        investment = request.POST['investment']
        decision_power = request.POST['decision_power']
        involvement = request.POST['involvement']
        interests = request.POST['interests']
        returns = request.POST['returns']
        exit_statergy = request.POST['exit_statergy']
        Stack_details.objects.create(user = request.user,role = role,equity=Equity,invest=investment,
                                     decision = decision_power,involvement=involvement,interest=interests,
                                     retunrs = returns,exit_sta=exit_statergy)
        return redirect('/domain_form_stack')
    return render(request,'stack_def.html')




def chart_bot(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        data = request.GET.get('data')
        print("Received data:", data)
    
        model = genai.GenerativeModel("gemini-1.5-pro")
        response_content = model.generate_content(data)
        
        return JsonResponse({'data': response_content.text}, status=200)
    
    return render(request, 'chart_bot.html')


# chaert bot

def chart_reponse(request):
    pass