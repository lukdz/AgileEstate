from django.views.generic.edit import FormView

from .forms import PropertyForm

class PropertyFormView(FormView):
    template_name = "add-property.html"
    form_class = PropertyForm
    success_url = "/success/"

    def form_valid(self, form):
        return super(PropertyFormView, self).form_valid(form)
