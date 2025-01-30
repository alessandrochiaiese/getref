
from django.views.generic import TemplateView


#####################
#  ADMIN TEMPLATES  #
#####################
class ChartJSView(TemplateView):
    template_name = 'dashboard/pages/charts/chartjs.html'

class DocumentationView(TemplateView):
    template_name = 'dashboard/pages/documentation/documentation.html'

class BasicElementsView(TemplateView):
    template_name = 'dashboard/pages/forms/basic_elements.html'

class IconsView(TemplateView):
    template_name = 'dashboard/pages/icons/mdi.html'

class Error500View(TemplateView):
    template_name = 'dashboard/pages/samples/error-500.html'

class Error404View(TemplateView):
    template_name = 'dashboard/pages/samples/error-404.html'

class LoginView(TemplateView):
    template_name = 'dashboard/pages/samples/login.html'

class RegisterView(TemplateView):
    template_name = 'dashboard/pages/samples/register.html'

class TableView(TemplateView):
    template_name = 'dashboard/pages/tables/basic-table.html'

class ButtonsView(TemplateView):
    template_name = 'dashboard/pages/ui-features/buttons.html'

class DropdownsView(TemplateView):
    template_name = 'dashboard/pages/ui-features/dropdowns.html'

class TypographyView(TemplateView):
    template_name = 'dashboard/pages/ui-features/typography.html'
