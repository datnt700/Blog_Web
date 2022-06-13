from cProfile import Profile
from django.shortcuts import get_object_or_404, render
from django.views import generic
# UserCreationForm: A form that creates a user, with no privileges, from the given username and password.
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
# reverse lazy to wherever we want to redirect to
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from .form import ProfilePageForm, SignUpForm, EditProfileForm, PasswordChangingForm
from myblog.models import Profile
# three step process: VIEW->HTML PAGE->URL


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"
    # fields = '__all__'

    # we hijack their form and we inserted their username and userid
    def form_valid(self, form):
        form.instance.user = self.request.user
        # it tell that there's a user filling out this form let't grab that user
        return super().form_valid(form)


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'website_url', 'facebook_url',
              'twitter_url', 'instagram_url', 'pinterest_url']

    success_url = reverse_lazy('home')


class ShowProfilePageView(DetailView):
    model = Profile
    template_name: str = 'registration/user_profile.html'

    # this allow us to grab the context data that we pass in either through the view or through url as an id number
    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(ShowProfilePageView,
                        self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        # kwargs['pk']: which is getting passed in through the url
        # when got user in page user we need to now pass that into the page itself through the context variable
        context["page_user"] = page_user

        return context


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

    # success_url = reverse_lazy('home')


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):  # to tell what user we are
        return self.request.user
