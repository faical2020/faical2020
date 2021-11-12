from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from django.utils.http import urlencode
from django.views.generic.edit import UpdateView
from prod.models.preprod import Preprod
from prod.forms.preprod import PreprodForm
from prod.models.qcontrol import Qcontrol
from prod.forms.qcontrol import QcontrolForm ,QcontrolSearchForm
from itertools import chain

def qcontrol_liste(request):
    selected = "qcontrol"
    qcontrol_liste = Qcontrol.objects.all()

    for prod in Preprod.objects.all():
        if not hasattr(prod,'Qprod'):
            q= Qcontrol(preprod= prod)
            q.save()
    
    if request.method == "POST":
        form = QcontrolSearchForm(request.POST)
        if form.is_valid():
            base_url = reverse('qcontrols')
            query_string = urlencode(form.cleaned_data)
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)
    else:
        form = QcontrolSearchForm()
        
        packid_form = request.GET.get("packid","")
        odc_form = request.GET.get("odc","")
        quantite_form = request.GET.get("quantite","")
        
        
        
        if packid_form is not None:
            qcontrol_liste = qcontrol_liste.filter(preprod__pack_id__icontains= packid_form)
            form.fields['packid'].intial = packid_form
        if odc_form is not None:
            qcontrol_liste = qcontrol_liste.filter(preprod__odc__icontains= odc_form)
            form.fields['odc'].intial = odc_form
        if quantite_form is not None:
            qcontrol_liste = qcontrol_liste.filter(preprod__quantite__icontains= quantite_form)
            form.fields['quantite'].intial = quantite_form  

    p1 = qcontrol_liste.filter(ab__isnull=True).order_by('-preprod__pack_id')
    p2 = qcontrol_liste.filter(ab__isnull=False).order_by('-preprod__pack_id')
    
    combined_results = list(chain(p1, p2))
    paginator = Paginator(combined_results,10)
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