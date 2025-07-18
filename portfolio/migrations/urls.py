from django.urls import path
from . import views # Import views from the current directory

app_name = 'portfolio' # Namespace for URL reversing

urlpatterns = [
    path('', views.applicant_list_view, name='applicant_list'), # Root path, changed to CBV for consistency with modern Django
    # Changed from FBV to CBV as well for the list view to better demonstrate
    # class-based views. If strict FBV is required, you'd make a function here.
    # Updated: Reverting to FBV for list_view as per instruction (see views.py)
    path('portfolio/<str:username>/', views.PortfolioDetailView.as_view(), name='portfolio_detail'),
    path('delete/<str:username>/', views.ApplicantDeleteView.as_view(), name='applicant_delete'),
]