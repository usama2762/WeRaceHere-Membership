from django.shortcuts import render
from django.views import View
from .forms import SignupForm,UpdateForm
from django.views.generic import UpdateView
from .models import Racer
# Create your views here.


class RacerSignup(View):

    def post(self, request):

        form = SignupForm(request.POST)
        if form.is_valid():
            emptemp = form.save(commit=False)
            emptemp.save()
            return render(request, 'Signup.html', {})
        else:
            return render(request, 'Signup.html', {})

    def get(self, request):
        form = SignupForm()
        context = {'form': form}
        return render(request, 'Signup.html', context)


class PasswordUpdate(UpdateView):
    form_class = UpdateForm
    template_name = 'passwordupdate.html'

    def get_object(self, queryset=None):
        return self.request.user

    # override form_valid method
    def form_valid(self, form):
        # save cleaned post data
        form.save()
        clean = form.cleaned_data
        context = {}
        self.object = context.save(clean)
        return super(PasswordUpdate, self).form_valid(form)

class RacerUpdate(UpdateView):
    model = Racer

    template_name = 'Signup.html'

    form_class = SignupForm
