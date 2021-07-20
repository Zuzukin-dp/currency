from accounts import views

from django.contrib.auth import views as auth_views

from django.urls import path

app_name = 'accounts'

urlpatterns = [
    # path('my-profile/<int:pk>', views.MyProfile.as_view(), name='my-profile'),
    path('my-profile/', views.MyProfile.as_view(), name='my-profile'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
