from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from prod.models.preprod import Preprod
from prod.forms.preprod import PreprodForm
from prod.models.qcontrol import Qcontrol
from prod.forms.qcontrol import QcontrolForm
from prod.models.rejprod import Rejprod
from prod.forms.rejprod import RejprodForm

def rejprod_liste(request):
    selected = "rejprod"
    rejprod_liste = Rejprod.objects.all()
    paginator = Paginator(rejprod_liste.order_by('-date_mise_a_jour'),10)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
        rejprod_liste = paginator.page(page)
    except EmptyPage:
        rejprod_liste = paginator.page(paginator.num_pages())
    return render(request,"prod/rejprod/rejprod_liste.html", locals())

class CreateRejprod(CreateView):
    model = Rejprod
    form_class = RejprodForm
    template_name =  "prod/rejprod/rejprod_form.html"

    def get_success_url(self):
        return reverse_lazy("detail_rejprod", kwargs={"pk":self.object.id})

class UpdateRejprod(UpdateView):
    model = Rejprod
    form_class = RejprodForm
    template_name =  "prod/rejprod/rejprod_form.html"

    def get_success_url(self):
        return reverse_lazy("detail_rejprod", kwargs={"pk":self.object.id})