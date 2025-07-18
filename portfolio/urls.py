from django.urls import path
from .views import PortfolioDetailView, UserDeleteView

urlpatterns = [
    path('<slug:username>/', PortfolioDetailView.as_view(), name='portfolio_detail'),
    path('<slug:username>/delete/', UserDeleteView.as_view(), name='delete_user'),
]
