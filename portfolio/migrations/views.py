from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Portfolio, Project

# 1. Function-Based View for Applicant List
def applicant_list_view(request):
    # Get all users who have an associated portfolio
    # This prevents listing users who are just admin accounts or haven't created a portfolio yet
    applicants = User.objects.filter(portfolio__isnull=False).select_related('portfolio').order_by('first_name')
    context = {
        'applicants': applicants,
        'position_applied_for': 'Junior Developer', # Hardcoded position
    }
    return render(request, 'portfolio/applicant_list.html', context)

# 2. Class-Based View for Portfolio Detail
class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/portfolio_detail.html'
    context_object_name = 'portfolio' # The variable name to use in the template

    def get_object(self, queryset=None):
        # Retrieve the Portfolio object based on the username in the URL
        # We need to filter by user's username
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username)
        return get_object_or_404(Portfolio, user=user)

# 3. Class-Based View for Deleting Applicant (User and Portfolio/Project)
class ApplicantDeleteView(DeleteView):
    model = User # We are deleting the User, which will cascade delete Portfolio and Project
    template_name = 'portfolio/applicant_confirm_delete.html' # You can create a simple confirmation page, though not strictly required by "No need for window confirmation"
    success_url = reverse_lazy('portfolio:applicant_list') # Redirect to the list view after deletion

    def get_object(self, queryset=None):
        # Retrieve the User object based on the username in the URL
        username = self.kwargs.get('username')
        return get_object_or_404(User, username=username)

    # Optional: Override post method to perform deletion without confirmation page
    # If no confirmation page is needed, you could delete directly in the post method
    # and not provide a template_name.
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Ensure that deleting the User cascades to Portfolio and Project due to on_delete=models.CASCADE
        self.object.delete()
        return redirect(self.get_success_url())