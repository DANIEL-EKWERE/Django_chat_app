from django.urls import path

from . import views


urlpatterns = [
    path("", views.rooms, name="rooms"),
    path('logout/',views.Logout,name='logout'),
    path('login/', views.Login, name='login'),
    path("<str:slug>/", views.room, name="room"),
    path('send/' , views.send),
    path('firebase-messaging-sw.js',views.showFirebaseJS,name="show_firebase_js"),
]