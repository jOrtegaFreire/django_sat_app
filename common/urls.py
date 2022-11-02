"""satApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
urlpatterns = [
    path('',views.login),
    path('register.html',views.register),
    path('index.html',views.index),
    path('stock.html',views.stock),
    path('edit_component.html',views.edit_component),
    path('add_component.html',views.add_component),
    path('ingress.html',views.ingress),
    path('ingress_all.html',views.show_all),
    path('ingress_recieved.html',views.show_received),
    path('ingress_inspecting.html',views.show_inspecting),
    path('ingress_awaiting_approval.html',views.show_awaiting_approval),
    path('ingress_repairing.html',views.show_repairing),
    path('ingress_repaired.html',views.show_repaired),
    path('ingress_delivered.html',views.show_delivered),
    path('ingress_pending_return.html',views.show_pending_return),
    path('ingress_returned.html',views.show_returned),
    path('ingress_edit.html',views.ingress_edit),
    path('logout.html',views.logout)

]
