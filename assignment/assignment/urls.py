from django.urls import include, path
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', views.UserViewSet)
router.register('investment', views.InvestmentViewSet)
router.register('bill', views.BillViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('investments_per_user/<int:pk>/', views.investments_per_user),
    path('bills_per_user/<int:pk>/', views.bills_per_user),
    path('edit_investment/<int:pk>/', views.edit_investment),
]
