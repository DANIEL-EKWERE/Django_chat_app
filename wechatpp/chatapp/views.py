from django.shortcuts import render, redirect
from .models import Room,Message
from django.http.request import HttpHeaders
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
import requests
import json

def rooms(request):
    resgistration  = ['dnEetf_WJIGJpt_B8Xhlz9:APA91bGXIBI93qq4mjUsy6BZS7ROToZ-TLfpRwLkMd1icdkjr2sRu08N-oSwW8xI1KM13Xa7FzoI5C9iYeaMOEnPdc15gvJ4AoD1bdGOJnt-BFznQcmYgDoFjKHDmsWjIIbioVc3MbQU','cnwQQ0aErqYJq_p5hhbsNr:APA91bG6dh8t-_h8IL7F9scrJVNXCNaAK2XFcZ6A4I2o0ZAC-YoTC1QmT2wd-ivhkN2W59EcIMtWjYmSIPljM5QFfYQg1eObpFqLgck1zKHqK1AdQH46jqdTUyCwb9GnZc2sW4viaGy8']
    send_notification(resgistration , 'Demo ChatApp by Daniel Ekwere' , 'Welcome to demo chat app by daniel ekwere,your best chatting system!!!')
    rooms=Room.objects.all()
    return render(request, "rooms.html",{"rooms":rooms})

def room(request,slug):
    #permission_classes = [IsAuthenticated]
    #resgistration  = ['dnEetf_WJIGJpt_B8Xhlz9:APA91bGXIBI93qq4mjUsy6BZS7ROToZ-TLfpRwLkMd1icdkjr2sRu08N-oSwW8xI1KM13Xa7FzoI5C9iYeaMOEnPdc15gvJ4AoD1bdGOJnt-BFznQcmYgDoFjKHDmsWjIIbioVc3MbQU','cnwQQ0aErqYJq_p5hhbsNr:APA91bG6dh8t-_h8IL7F9scrJVNXCNaAK2XFcZ6A4I2o0ZAC-YoTC1QmT2wd-ivhkN2W59EcIMtWjYmSIPljM5QFfYQg1eObpFqLgck1zKHqK1AdQH46jqdTUyCwb9GnZc2sW4viaGy8']
    #send_notification(resgistration , f'{ request.user.username} sent a message Code Keen added a new video' , 'Code Keen new video alert')
    #print('working=============')
    send_notification
    try:
        room_name=Room.objects.get(slug=slug).name
        messages=Message.objects.filter(room=Room.objects.get(slug=slug))
        
        return render(request, "room.html",{"room_name":room_name,"slug":slug,'messages':messages})
    except Room.DoesNotExist:
        pass
    
    return render(request, "room.html")


def Login(request):
    #form = myForm(request.POST)
    if request.method == 'POST':
           # user=form.save()
            #user = request.user
        username = request.POST['username']
        raw_password = request.POST['password']
        user = authenticate(username = username, password = raw_password)
        if user is not None:     
            login(request, user)
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            resgistration  = ['dnEetf_WJIGJpt_B8Xhlz9:APA91bGXIBI93qq4mjUsy6BZS7ROToZ-TLfpRwLkMd1icdkjr2sRu08N-oSwW8xI1KM13Xa7FzoI5C9iYeaMOEnPdc15gvJ4AoD1bdGOJnt-BFznQcmYgDoFjKHDmsWjIIbioVc3MbQU','cnwQQ0aErqYJq_p5hhbsNr:APA91bG6dh8t-_h8IL7F9scrJVNXCNaAK2XFcZ6A4I2o0ZAC-YoTC1QmT2wd-ivhkN2W59EcIMtWjYmSIPljM5QFfYQg1eObpFqLgck1zKHqK1AdQH46jqdTUyCwb9GnZc2sW4viaGy8']
            send_notification(resgistration , 'Login Successful' , 'login successful chose a room and start a conversation!!!')
            return redirect('/')
        else:
           return render(request,"registration/login.html") 
    else:
        #form = myForm()
        return render(request,"registration/login.html")
    return render(request,"registration/login.html")

def Logout(request):
    logout(request)
    resgistration  = ['dnEetf_WJIGJpt_B8Xhlz9:APA91bGXIBI93qq4mjUsy6BZS7ROToZ-TLfpRwLkMd1icdkjr2sRu08N-oSwW8xI1KM13Xa7FzoI5C9iYeaMOEnPdc15gvJ4AoD1bdGOJnt-BFznQcmYgDoFjKHDmsWjIIbioVc3MbQU','cnwQQ0aErqYJq_p5hhbsNr:APA91bG6dh8t-_h8IL7F9scrJVNXCNaAK2XFcZ6A4I2o0ZAC-YoTC1QmT2wd-ivhkN2W59EcIMtWjYmSIPljM5QFfYQg1eObpFqLgck1zKHqK1AdQH46jqdTUyCwb9GnZc2sW4viaGy8']
    send_notification(resgistration , 'Logout Successful' , 'logout successful, please do check us back again!!!')
    return redirect('/')

'''
firebase cloud messaging functions and process begins here
'''



def send_notification(registration_ids, message_title, message_desc):
    fcm_api = "AAAAaTsSHnI:APA91bEnZZqvRVx5qQQMD2fTHU4BMoTmFdShcQUpQJTgvBZax5uokUHxG8MyqMMTznBve1ZapAH-0Cd-v0zHNHrLiIsMHkWfdPGiUPfvPaKajnLaJkdJ8ktP3KB5kXEuLhZ2YCYhGxwk"
    url = "https://fcm.googleapis.com/fcm/send"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": 'key=' + fcm_api
    }

    payload = {
        "registration_ids": registration_ids,
        "priority": "high",
        "notification": {
            "body": message_desc,
            "title": message_title,
            "image": "https://i.ytimg.com/vi/m5WUPHRgdOA/hqdefault.jpg?sqp=-oaymwEXCOADEI4CSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDwz-yjKEdwxvKjwMANGk5BedCOXQ",
            "icon": "https://yt3.ggpht.com/ytc/AKedOLSMvoy4DeAVkMSAuiuaBdIGKC7a5Ib75bKzKO3jHg=s900-c-k-c0x00ffffff-no-rj"
        }
    }

    result = requests.post(url, json=payload, headers=headers)
    print(f'{result.status_code} =================================== {result.text}')
    # print(result.json())


#esy9TptBFvOogFxVA3-8Y8:APA91bHPJEvypdIWgVLycJ0tuEArYZBPVK7gdHNpABL-Y6yw5OKFYyKW8TBQ-0M8CrICcxZjpjpPbvwNNqTWBN3XuyRZwAPBx2AF8Bw30JSvwTzuPz_Op6tXm34zYfZ5bqSi3KHlerE2

def send(request):
    resgistration  = ['dnEetf_WJIGJpt_B8Xhlz9:APA91bGXIBI93qq4mjUsy6BZS7ROToZ-TLfpRwLkMd1icdkjr2sRu08N-oSwW8xI1KM13Xa7FzoI5C9iYeaMOEnPdc15gvJ4AoD1bdGOJnt-BFznQcmYgDoFjKHDmsWjIIbioVc3MbQU']
    send_notification(resgistration , 'Code Keen added a new video' , 'Code Keen new video alert')
    return HttpResponse("sent")




def showFirebaseJS(request):
    data='importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");' \
         'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js"); ' \
         'var firebaseConfig = {' \
         '        apiKey: "AIzaSyCsD2tYq9epLFIv5Rr5uSF0mrIMsOmoqus",' \
         '        authDomain: "fir-chat-app-with-django.firebaseapp.com",' \
         '        databaseURL: "https://fir-chat-app-with-django-default-rtdb.firebaseio.com/",' \
         '        projectId: "fir-chat-app-with-django",' \
         '        storageBucket: "fir-chat-app-with-django.appspot.com",' \
         '        messagingSenderId: "451962609266",' \
         '        appId: "1:451962609266:web:ffc3ba15ef95aa2060eceb",' \
         '        measurementId: "G-YDDHCBDGY2"' \
         ' };' \
         'firebase.initializeApp(firebaseConfig);' \
         'const messaging=firebase.messaging();' \
         'messaging.setBackgroundMessageHandler(function (payload) {' \
         '    console.log(payload);' \
         '    const notification=JSON.parse(payload);' \
         '    const notificationOption={' \
         '        body:notification.body,' \
         '        icon:notification.icon' \
         '    };' \
         '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
         '});'

    return HttpResponse(data,content_type="text/javascript")
