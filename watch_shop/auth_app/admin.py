from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from watch_shop.auth_app.forms import SignUpForm, UserEditForm
from watch_shop.auth_app.models import Profile

UserModel = get_user_model()


class ProfileInLine(admin.StackedInline):
    model = Profile


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    ordering = ('email',)
    list_display = ['email', 'date_joined', 'last_login']
    list_filter = ("is_staff", "is_superuser", "groups")
    readonly_fields = ['date_joined']
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    form = UserEditForm
    add_form = SignUpForm

    fieldsets = (
        ('Personal info', {
            'classes': ('wide',),
            'fields': ('email', 'password'),
        }),
        (
            'Permissions',
            {
                'fields': (
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        ('Important dates',
         {'fields':
             (
                 'last_login',
                 'date_joined'
             )}),
    )
    inlines = [ProfileInLine]
    # add_fieldsets = (
    #     (
    #         None,
    #         {
    #             "classes": ("wide",),
    #             "fields": ("email", "password1", "password2"),
    #         },
    #     ),   (None,
    #     {
    #             "classes": ("wide",),
    #             "fields": ("first_name", "last_name", "age"),
    #         },
    #     )
    # )

    # inlines = [ProfileInLine]

    #
    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     ('Personal info', {'fields': ('date_joined',)}),
    #     ('Permissions', {'fields': ('is_staff',)}),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'date_joined', 'password1', 'password2'),
    #     }),
    # )
    #

# ------------------------------
# @admin.register(get_user_model())
# class PetstagramUserAdmin(UserAdmin):
#     form = PetstagramUserEditForm
#     add_form = PetstagramUserCreationForm
#
#     fieldsets = (
#         (None,
#          {
#              'fields': (
#                  'username', 'password'
#              )
#          }),
#         (
#             'Personal info',
#             {'fields': (
#                 'first_name',
#                 'last_name',
#                 'email',
#                 'gender',
#             )}),
#         (
#             'Permissions',
#             {
#                 'fields': (
#                     'is_active',
#                     'is_staff',
#                     'is_superuser',
#                     'groups',
#                     'user_permissions',
#                 ),
#             },
#         ),
#         ('Important dates',
#          {'fields':
#              (
#                  'last_login',
#                  'date_joined'
#              )}),
#     )
