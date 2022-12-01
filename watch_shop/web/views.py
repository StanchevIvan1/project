from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic as views

from watch_shop.auth_app.models import Profile, AppUser
from watch_shop.web.models import Product

UserModel = get_user_model()
#
# def index(request):
#     context = {
#         'template_name': 'index.html',
#         'request': request,
#     }
#     return render(request, 'index.html', context)


class IndexView(views.TemplateView):
    template_name = 'index.html'


class AboutView(views.TemplateView):
    template_name = 'about.html'


class ContactView(views.TemplateView):
    template_name = 'contact.html'


# ListView
class ProductsView(LoginRequiredMixin, views.ListView):
    template_name = 'products.html'
    model = Product
    context_object_name = 'products_list'

#
# class UserDetailsView(views.DetailView):
#     template_name = 'account/account_details.html'
#     model = UserModel
#     # print(model.object.get(profile=2))
#     # print(get_object_or_404(UserModel, profile__first_name='Ivan'))
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['is_owner'] = self.request.user == self.object
#         return context
#
#
# class UserEditView(LoginRequiredMixin, views.UpdateView):
#     template_name = 'account/account_edit.html'
#     model = Profile
#     fields = ('first_name', 'last_name', 'age', 'photo')
#
#     # def get_queryset(self):
#     #     profile = Profile.__.objects.get(user_id=self.kwargs['pk'])
#     #     all_children = profile.objects.all()
#     #     return profile.objects
#
#     # author = get_object_or_404(Author, profile__user__username=username)
#
#     # fields = (get_object_or_404(Profile, user__user_id=), 'last_name', 'email',)
#
#     def get_success_url(self):
#         return reverse_lazy('user details', kwargs={
#             'pk': self.request.user.pk,
#         })
#
#
# class UserDeleteView(LoginRequiredMixin, views.DeleteView):
#     template_name = 'account/account_delete.html'
#     model = UserModel
#     success_url = reverse_lazy('index')

