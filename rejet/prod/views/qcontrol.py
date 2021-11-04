from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from prod.models.preprod import Preprod
from prod.forms.preprod import PreprodForm
from prod.models.qcontrol import Qcontrol
from prod.forms.qcontrol import QcontrolForm

def qcontrol_liste(request):
    selected = "qcontrol"
    qcontrol_liste = Qcontrol.objects.all()

    for prod in Preprod.objects.all():
        if not hasattr(prod,'Qprod'):
            q= Qcontrol(preprod= prod)
            q.save()
   
    paginator = Paginator(qcontrol_liste.order_by('-preprod'),10)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
        qcontrol_liste = paginator.page(page)
    except EmptyPage:
        qcontrol_liste = paginator.page(paginator.num_pages())
    return render(request,"prod/qcontrol/qcontrol_liste.html", locals())

class CreateQcontrol(CreateView):
    model = Qcontrol
    form_class = QcontrolForm
    template_name =  "prod/qcontrol/qcontrol_form.html"

    def get_success_url(self):
        return reverse_lazy("detail_qcontrol", kwargs={"pk":self.object.id})

class UpdateQcontrol(UpdateView):
    model = Qcontrol
    form_class = QcontrolForm
    template_name =  "prod/qcontrol/qcontrol_form.html"

    def get_success_url(self):
        return reverse_lazy("detail_qcontrol", kwargs={"pk":self.object.id})