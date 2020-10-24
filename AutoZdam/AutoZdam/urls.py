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
from django.contrib.auth import views as auth_views
from Auto_Zdam.tokens import user_tokenizer

urlpatterns = [
    path('', az_views.MainView.as_view(), name="main"),
    path('admin/', admin.site.urls),
    path('offer/', az_views.AddOffer.as_view(), name="add_offer"),
    path('user_create/', az_views.UserCreate.as_view(), name='user_create'),
    path('equip/', az_views.EquipCreate.as_view(), name="add_equip"),
    path('user_login/', az_views.UserLoginView.as_view(), name='user-login'),
    path('user_logout/', az_views.UserLogoutView.as_view(), name='user-logout'),
    path('offer_details/<int:id>', az_views.OfferDetails.as_view(), name='offer-details'),
    path('offer_update/<int:pk>', az_views.OfferUpdate.as_view(), name="offer-update"),
    path('offer_delete/<int:pk>', az_views.OfferDelete.as_view(), name="offer-delete"),
    path('offer_msg/<int:id>', az_views.ContactFormView.as_view(), name="offer-msg"),
    path('myview', az_views.MyView.as_view(), name="my-view"),
    path('confirm-email/<str:user_id>/<str:token>/', az_views.ConfirmRegistrationView.as_view(), name='confirm_email'),
    path('reset-password/', auth_views.PasswordResetView.as_view(
      template_name='Auto_Zdam/reset_password.html',
      html_email_template_name='Auto_Zdam/reset_password_email.html',
      success_url="/",
      token_generator=user_tokenizer),
    name='reset_password'
  ),
path(
    'reset-password-confirmation/<str:uidb64>/<str:token>/',
    auth_views.PasswordResetConfirmView.as_view(
      template_name='Auto_Zdam/reset_password_update.html',
      post_reset_login=True,
      post_reset_login_backend='django.contrib.auth.backends.ModelBackend',
      token_generator=user_tokenizer,
      success_url="/"),
    name='password_reset_confirm'
  ),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
