from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.views.generic import DetailView


class PortfolioDetailView(DetailView):
    model = User
    template_name = 'portfolio/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolio'] = self.object.portfolio
        return context

class UserDeleteView(DeleteView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    success_url = reverse_lazy('list_view')

# Create your views here.
