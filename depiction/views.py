from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView
from .models import *
from django.urls import reverse_lazy
from django.views import generic
from .forms import *

class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class=EditProfileNewForm
    template_name='depiction/edit_profile_page.html'
    def get_success_url(self):
        return reverse_lazy('depiction:show_profile_page', args=[self.request.user.id])
    # success_url=reverse_lazy('depiction:show_profile_page', args=request.user.id)

class PasswordsChangeView(PasswordChangeView):
    form_class= PasswordChangingForm
    success_url= reverse_lazy('depiction:password_success')

def password_success(request):
    return render(request, 'depiction/password_success.html', {})

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'depiction/my_profile.html'

    def get_context_data(self,*args,**kwargs):
        context=super(ShowProfilePageView,self).get_context_data(*args,**kwargs)
        page_user=get_object_or_404(Profile,id=self.kwargs['pk'])
        # page_user.user_profile_id=((User.objects.get(username=page_user)).id)
        # page_user.save()
        context["page_user"] = page_user
        return context
