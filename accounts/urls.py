from django.urls import path
from accounts.views import LoginView, logout_view, RegisterView, AccountDetailView, AccountUpdateView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('<str:slug>', AccountDetailView.as_view(), name='account_detail'),
    path('<str:slug>/update', AccountUpdateView.as_view(), name='account_update'),
]

