from django.views.generic.edit import FormView

from .forms import PropertyForm

class PropertyFormView(FormView):
    template_name = "propertyForm.html"
    form_class = PropertyForm
    success_url = "/add_property/"

    def form_valid(self, form):
        return super(PropertyFormView, self).form_valid(form)
