import time

from django import forms
from django.contrib.auth import forms as auth_forms, views as auth_views, login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from services.ses import SESservice
from watch_shop.auth_app.forms import SignUpForm
from watch_shop.auth_app.models import Profile, AppUser
from watch_shop.auth_app.tasks import send_email_to_new_users
from watch_shop.web.models import ShoppingCart, ShoppingProduct

UserModel = get_user_model()


class SignUpView(views.CreateView):
    template_name = 'auth/sign-up.html'
    form_class = SignUpForm

    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        # send_email_to_new_users.delay(pk=self.request.user.pk)

        send_email_to_new_users(self.request.user.email)
        return result


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class SignInView(auth_views.LoginView):
    template_name = 'auth/sign-in.html'
    success_url = reverse_lazy('index')

    # def form_invalid(self, form):
    #     return
    # def get_success_url(self):
    #     if self.success_url:
    #         return self.success_url
    #
    #     return self.get_redirect_url() or self.get_default_redirect_url()


class SignOutView(auth_views.LogoutView):
    template_name = 'auth/sign-out.html'


#
# def sign_in(request):
#     if request.method == 'GET':
#         form = SignInForm()
#     else:
#         form = SignInForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, **form.cleaned_data)
#
#             if user:
#                 login(request, user)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'auth/sign-in.html', context=context)
#


class UserDetailsView(views.DetailView):
    template_name = 'account/account_details.html'
    model = UserModel

    # print(model.object.get(profile=2))
    # print(get_object_or_404(UserModel, profile__first_name='Ivan'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        context['purchases'] = ShoppingCart.objects.filter(user_id=self.request.user.pk).get().product.filter() \
            if ShoppingCart.objects.filter(user_id=self.request.user.pk) else None
        context['count'] = ShoppingProduct.objects.filter(shoppingcart__user_id=self.request.user.pk).count()
        return context


class UserEditView(LoginRequiredMixin, views.UpdateView, PermissionRequiredMixin):
    template_name = 'account/account_edit.html'
    model = Profile
    fields = ('first_name', 'last_name', 'age', 'photo')

    def get(self, *args, **kwargs):
        super().get(*args, **kwargs)
        if not self.request.user.pk == self.kwargs['pk']:
            return redirect('index')
        return super().get(self.request, *args, **kwargs)
        # return super().get(self.request, *args, **kwargs)


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     pk = self.kwargs['pk']
    #     print(self.request.user.pk)
    #     print(pk)
    #     if not self.request.user.pk == pk:
    #         return reverse_lazy('index')
    #     # if pk ==self.kwargs['']
    #     return context

    # perms_check = ['auth_app.add_appuser', 'auth_app.change_appuser',
    # 'auth_app.delete_appuser', 'auth_app.view_appuser']
    # for user in AppUser.object.filter():
    #     # print(user.has_perms(perms_check))
    #     for perm in perms_check:
    #         print(user.has_perm(perm))

    # def get_queryset(self):
    #     profile = Profile.__.objects.get(user_id=self.kwargs['pk'])
    #     all_children = profile.objects.all()
    #     return profile.objects

    # author = get_object_or_404(Author, profile__user__username=username)

    # fields = (get_object_or_404(Profile, user__user_id=), 'last_name', 'email',)

    def get_success_url(self):
        return reverse_lazy('user details', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(LoginRequiredMixin, views.DeleteView):
    template_name = 'account/account_delete.html'
    model = UserModel
    success_url = reverse_lazy('index')

    def get(self, *args, **kwargs):
        super().get(*args, **kwargs)
        if not self.request.user.pk == self.kwargs['pk']:
            return redirect('index')
        return super().get(self.request, *args, **kwargs)



'''
*E_lsdk214
*A_lfgk254
'''
