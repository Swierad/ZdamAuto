from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import User, Offer, Equip
from .forms import OfferForm, UserCreateForm, UserLoginForm, ContactForm
from .tokens import user_tokenizer
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User as DjangoUser
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .filters import OfferFilter
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.forms import AuthenticationForm






class AddOffer(LoginRequiredMixin, View):
    login_url = reverse_lazy('user-login')


    def get(self, request):
        form = OfferForm(request.user)
        current_user = request.user
        user_id = current_user.id
        return render(request, "Auto_Zdam/offer_form.html", {"form": form, "id": user_id})
    def post(self, request):
        f = OfferForm(request.user, request.POST, request.FILES)
        if f.is_valid():
            f.save()
        else:
            print(f.errors)
            return render(request, "Auto_Zdam/offer_form.html", {"form": f})
        return redirect(reverse('main'))

class UserCreate(View):
    def get(self, request):
        return render(request, "Auto_Zdam/register.html", { 'form': UserCreateForm() })

    def post(self, request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            wherefrom = form.cleaned_data['wherefrom']
            user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name, wherefrom=wherefrom )
            user.save()
            user.is_active = False
            user.save()
            token = user_tokenizer.make_token(user)
            user_id = urlsafe_base64_encode(force_bytes(user.id))
            url = 'http://localhost:8000' + reverse('confirm_email', kwargs={'user_id': user_id, 'token': token})
            message = get_template('Auto_Zdam/register_email.html').render({
                'confirm_url': url
            })
            mail = EmailMessage('Django Survey Email Confirmation', message, to=[user.email],
                                from_email='swierad-88@o2.pl')
            mail.content_subtype = 'html'
            mail.send()

            return render(request, "Auto_Zdam/user_login.html", {
                'form': AuthenticationForm(),
                'message': f'A confirmation email has been sent to {user.email}. Please confirm to finish registering'
            })

        return render(request, 'survey/register.html', {'form': form})


class ConfirmRegistrationView(View):
    def get(self, request, user_id, token):
        user_id = force_text(urlsafe_base64_decode(user_id))

        user = User.objects.get(pk=user_id)

        context = {
            'form': UserLoginForm(),
            'message': 'Registration confirmation error . Please click the reset password to generate a new confirmation email.'
        }
        if user and user_tokenizer.check_token(user, token):
            user.is_active = True
            user.save()
            context['message'] = 'Registration complete. Please login'
            return render(request, "Auto_Zdam/user_login.html", context)

        return render(request, "Auto_Zdam/user_login.html", context)

class EquipCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'Auto_Zdam.add_equipe'
    login_url = reverse_lazy('user-login')
    model = Equip
    fields = '__all__'
    success_url = reverse_lazy("/add_equip")

class MainView(View):
    def get(self, request):
        r = Offer.objects.order_by('id')
        offerFilter = OfferFilter(request.GET, queryset=r)
        r = offerFilter.qs
        ctx = {
            'r': r,
            'offerFilter': offerFilter
        }
        return render(request, "Auto_Zdam/index.html", ctx)





class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, "Auto_Zdam/user_login.html", {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():  # uruchomienie walidacji
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('main'))
                else:
                    form.add_error(None, "Konto nie jest aktywne")
            else:
                # user is None
                form.add_error(None, "Nieprawidłowy login lub hasło")
        return render(request, "Auto_Zdam/user_login.html", {'form': form})

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('main'))



class OfferDetails(View):
#    permission_required = 'Auto_Zdam.view_offer'
#   PermissionRequiredMixin,
    login_url = reverse_lazy('user-login')
    def get(self, request, id):
        r = Offer.objects.get(id=id)
        ctx = {
            "offer": r,
        }
        return render(request, "Auto_Zdam/offer-details.html", ctx)
    #def post(self, request, id ):
    #    msg = request.POST.get("msg")
    #    send_mail('Masz nową wiadomość z poratlu AutoZdam', msg, 'swierad-88@o2.pl', ['swierad@gmail.com'], fail_silently = False)
   #     r = Offer.objects.get(id=id)
    #    ctx = {
    #        "offer": r,
   #     }
  #      return render(request, "Auto_Zdam/offer-details.html", ctx)


class OfferUpdate(UpdateView):
  model = Offer
  fields = ["car_brand", "car_model", "category", "type", "year_of_production", "color", "car_mileage",
    "description", "car_equipment", "fuel_type", "doors_number", "seats_number", "engine_capacity", "user", "price",
    "photos", "photos_2", "photos_3", "photos_4", "photos_5"]
  template_name_suffix = '_update_form'
  success_url = '/'

class OfferDelete(DeleteView):
    model = Offer
    success_url = '/'

class ContactFormView(View):
    def get(self, request, id):
        form = ContactForm()
        return render(request, "Auto_Zdam/offer-msg.html", {'form': form})
    def post(self, request, id):
        form = ContactForm(request.POST)
        r = Offer.objects.get(id=id)
        if form.is_valid():
            form = request.POST.get('description')
            form_price = request.POST.get('price')
            loged_user = request.user.email
            msg = f"Wiadomość od {loged_user} w sprawie ogłoszenia {r.car_brand} {r.car_model}: " \
                  f"{form}. Kwota proponowana przez komisanta {form_price}   "
            send_mail(f'Auto_Zdam - masz nową wiadomość od {loged_user}', msg, 'swierad-88@o2.pl', ['swierad@gmail.com'], fail_silently = False)
            r = Offer.objects.get(id=id)
            ctx = {
                "offer": r,
            }
            return render(request, "Auto_Zdam/offer-details.html", ctx)


class MyView(View):
    def get(selfself, request):
        user = User.objects.get(email = request.user.email)
        offers = Offer.objects.filter(user = user)
        ctx = {
            "user":  request.user,
            "offers": offers
        }


        return render(request, "Auto_Zdam/MyView.html", ctx)


