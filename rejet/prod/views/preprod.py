
from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from prod.models.preprod import Preprod
from prod.forms.preprod import PreprodForm

def preprod_liste(request):
    selected = "preprod"
    preprod_liste = Preprod.objects.all()
    paginator = Paginator(preprod_liste.order_by('-date_mise_a_jour'),10)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
        preprod_liste = paginator.page(page)
    except EmptyPage:
        preprod_liste = paginator.page(paginator.num_pages())
    return render(request,"prod/preprod/preprod_liste.html", locals())

class CreatePreprod(CreateView):
    model = Preprod
    form_class = PreprodForm
    template_name =  "prod/preprod/preprod_form.html"

    def get_success_url(self):
        return reverse_lazy("detail_preprod", kwargs={"pk":self.object.id})

class UpdatePreprod(UpdateView):
    model = Preprod
    form_class = PreprodForm
    template_name =  "prod/preprod/preprod_form.html"

    def get_success_url(self):
        return reverse_lazy("detail_preprod", kwargs={"pk":self.object.id})
