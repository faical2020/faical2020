
from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from django.utils.http import urlencode
from django.views.generic.edit import UpdateView
from prod.models.preprod import Preprod
from prod.models.qcontrol import Qcontrol
from prod.forms.preprod import PreprodForm, PreprodSearchForm

def preprod_liste(request):
    selected = "preprods"
    preprod_liste = Preprod.objects.all()

    if request.method == "POST":
        form = PreprodSearchForm(request.POST)
        if form.is_valid():
            base_url = reverse('preprods')
            query_string = urlencode(form.cleaned_data)
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)
    else:
        form = PreprodSearchForm()
        date_form = request.GET.get("date","")
        packid_form = request.GET.get("packid","")
        odc_form = request.GET.get("odc","")
        quantite_form = request.GET.get("quantite","")
        
        if date_form is not None:
            preprod_liste = preprod_liste.filter(date_mise_a_jour__icontains= date_form)
            form.fields['date'].intial = date_form 
        
        if packid_form is not None:
            preprod_liste = preprod_liste.filter(pack_id__icontains= packid_form)
            form.fields['packid'].intial = packid_form
        if odc_form is not None:
            preprod_liste = preprod_liste.filter(odc__icontains= odc_form)
            form.fields['odc'].intial = odc_form
        if quantite_form is not None:
            preprod_liste = preprod_liste.filter(quantite__icontains= quantite_form)
            form.fields['quantite'].intial = quantite_form    

    paginator = Paginator(preprod_liste.order_by('-pack_id'),10)
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
