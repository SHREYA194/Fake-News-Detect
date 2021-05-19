from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import Contact
import joblib

import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Create your views here.
def home(request):

    import requests
    import json

    news_api_request = requests.get(
       "https://newsapi.org/v2/everything?q=tesla&from=2021-04-05&sortBy=publishedAt&apiKey=9af417b71f8a45248f70d19a18e7728d"  
    )
    api = json.loads(news_api_request.content)

    return render(request,'home.html',  {'api':api})

def about(request):
    return render(request,'about.html')

def login(request):
    if request.method == 'POST':
        Userid = request.POST['User id']
        Password = request.POST['Password']

        user = auth.authenticate(username=Userid, password=Password)

        if user is not None :
            auth.login(request, user)
            return redirect('search.html')

        else :
            messages.info(request, "Invalid credential")
            return redirect('Registration.html')
    else :
        return render(request, 'Registration.html')

def register(request):
    if request.method == 'POST':
        Userid = request.POST['User id']
        Email = request.POST['Email']
        Password = request.POST['Password']

        user = User.objects.create_user(username=Userid,email=Email,password=Password)
        user.save();
        print('user created')
        return redirect('/')
    else:
        return render(request,'Registration.html')

def contact(request):
    if request.method == 'POST':
        contact = Contact()
        FirstName = request.POST['First Name']
        LastName = request.POST['Last Name']
        Email = request.POST['Email']
        MobileNumber = request.POST['Mobile Number']
        Message = request.POST['Message']
        
        contact.firstName = FirstName
        contact.lastName = LastName
        contact.email = Email
        contact.mobileNo = MobileNumber
        contact.message = Message

        contact.save();
        return redirect('/')

    else :
        return render(request,'contact.html')


def search(request) :
    return render(request,'search.html')


def preprocessArticle(article):
    #Clean up and preprocess data
    stop_words = stopwords.words('english')
    lemmatizer = WordNetLemmatizer()

    #Clean sentence to remove any punctuations, convert to lower case
    cleaned_sentence = re.sub(r'[^\w\s]', '', str(article).lower())
    #Tokenize sentence into words
    words = nltk.word_tokenize(cleaned_sentence)
    #Remove stop words and words with length less than equal to 3
    filtered_words = [word for word in words if not word in stop_words and len(word) > 3]
    #Lemmatize
    output_sentence = ''
    for word in filtered_words:
        output_sentence = output_sentence  + ' ' + str(lemmatizer.lemmatize(word))
   
    print("\n After Preprocessing news : ", output_sentence)
    print("\n")
    return output_sentence


def getPredictions(lis):
    
    model = joblib.load('final_trained_model.sav')
    #scaled = joblib.load('preprocess.sav')
    #prediction = model.predict(sc.transform([lis]))
    article = preprocessArticle(lis)
    prediction = model.predict([article])

    if prediction == 0:
        return "REAL"
    elif prediction == 1:
        return "FAKE"
    else:
        return "error"

def result(request):
    #cls = joblib.load('final_trained_model.sav')
    #lis = []
    #lis.append(request.GET['data'])
    lis = str(request.GET['data'])
    print(lis)
    ans = getPredictions(lis)
    #ans = str(cls.predict([lis]))
    return render(request,'result.html',{'ans':ans, 'data':lis})

def logout(request) :
    auth.logout(request)
    return redirect('/')