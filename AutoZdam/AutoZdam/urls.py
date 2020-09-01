"""AutoZdam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Auto_Zdam import views as az_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', az_views.MainView.as_view(), name="main"),
    path('admin/', admin.site.urls),
    path('offer/', az_views.AddOffer.as_view(), name="add_offer"),
    path('user_create/', az_views.UserCreateView.as_view(), name='user_create'),
    path('equip/', az_views.EquipCreate.as_view(), name="add_equip"),
    path('user_login/', az_views.UserLoginView.as_view(), name='user-login'),
    path('user_logout/', az_views.UserLogoutView.as_view(), name='user-logout'),
    path('offer_details/<int:id>', az_views.OfferDetails.as_view(), name='offer-details'),
    path('offer_update/<int:pk>', az_views.OfferUpdate.as_view(), name="offer-update"),
    path('offer_delete/<int:pk>', az_views.OfferDelete.as_view(), name="offer-delete"),
    path('offer_msg/<int:id>', az_views.ContactFormView.as_view(), name="offer-msg"),
    path('myview', az_views.MyView.as_view(), name="my-view"),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
