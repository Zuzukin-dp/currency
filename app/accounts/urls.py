from accounts import views

from django.urls import path

app_name = 'accounts'

urlpatterns = [
    # path('my-profile/<int:pk>', views.MyProfile.as_view(), name='my-profile'),
    path('my-profile/', views.MyProfile.as_view(), name='my-profile'),
    path('signup/', views.SingUp.as_view(), name='signup'),
    path('activate/account/<uuid:username>/<token>', views.ActivateAccount.as_view(), name='activate-account'),
]
