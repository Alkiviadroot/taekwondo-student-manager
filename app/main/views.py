from django.db.models import fields
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from extra_views import CreateWithInlinesView, InlineFormSetFactory
from django.urls.base import reverse_lazy
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import ListView, CreateView, TemplateView, UpdateView
from django.db.models.functions import Lower
from django.views.generic.edit import DeletionMixin, FormView, ModelFormMixin
from .models import *
from .forms import *
import itertools


def colorBelt(num):
    color1 = "white"
    color2 = "white"
    zoni = "Λευκή Ζώνη"
    if (num == 2):
        color1 = "yellow"
        zoni = "Μισή κίτρινη Ζώνη"

    elif(num == 3):
        color1 = "yellow"
        color2 = "yellow"
        zoni = "Κίτρινη Ζώνη"

    elif(num == 4):
        color1 = "green"
        color2 = "yellow"
        zoni = "Μισή πράσινη Zώνη"

    elif(num == 5):
        color1 = "green"
        color2 = "green"
        zoni = "Πράσινη Zώνη"

    elif(num == 6):
        color1 = "blue"
        color2 = "green"
        zoni = "Μισή μπλε Zώνη"

    elif(num == 7):
        color1 = "blue"
        color2 = "blue"
        zoni = "Μπλε Zώνη"

    elif(num == 8):
        color1 = "red"
        color2 = "blue"
        zoni = "Μισή κόκκινη Zώνη"

    elif(num == 9):
        color1 = "red"
        color2 = "red"
        zoni = "Κόκκινη Zώνη"

    elif(num == 10):
        color1 = "black"
        color2 = "red"
        zoni = "Μισή Μαύρη Zώνη"

    elif(num >= 11):
        color1 = "black"
        color2 = "black"
        zoni = "Μαύρη Zώνη"

    return color1, color2, zoni


class HomeView(TemplateView):
    template_name = 'main/home.html'


# inital form
class MathitisForm(CreateView, ListView):
    model = InfoMathiti
    form_class = MathitisForm
    template_name = 'main/forms/mathitisForm.html'

    queryset = InfoGroups.objects.all()
    context_object_name = 'groups'

    def get_success_url(self):
        return reverse('main:provlimata_add', args=(self.object.id,))


class GoniosForm(CreateView):
    model = InfoGonios
    form_class = GoniosForm
    template_name = 'main/forms/goniosForm.html'

    def form_valid(self, form):
        self.mathitis = get_object_or_404(InfoMathiti, id=self.kwargs['pk'])
        form.instance.mathitis = self.mathitis
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        mathitis = get_object_or_404(InfoMathiti, id=pk)
        context['mathitis'] = mathitis
        context['gonios'] = InfoGonios.objects.filter(mathitis=mathitis.id)
        return context
    success_url = "#"


class ParalaviForm(CreateView):
    model = InfoParalavi
    form_class = ParalaviForm
    template_name = 'main/forms/paralaviForm.html'

    def form_valid(self, form):
        self.mathitis = get_object_or_404(InfoMathiti, id=self.kwargs['pk'])
        form.instance.mathitis = self.mathitis
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        mathitis = get_object_or_404(InfoMathiti, id=pk)
        context['mathitis'] = mathitis
        context['gonios'] = InfoGonios.objects.filter(mathitis=mathitis.id)
        context['paralavi'] = InfoParalavi.objects.filter(mathitis=mathitis.id)

        return context
    success_url = "#"


class ProvlimataForm(CreateView):
    model = Provlimata
    form_class = ProvlimataForm
    template_name = 'main/forms/provlimataForm.html'

    def form_valid(self, form):
        self.mathitis = get_object_or_404(InfoMathiti, id=self.kwargs['pk'])
        form.instance.mathitis = self.mathitis
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        mathitis = get_object_or_404(InfoMathiti, id=pk)
        context['provlimata'] = Provlimata.objects.filter(mathitis=mathitis.id)
        return context

    success_url = "./adies"


class AdiesForm(CreateView):
    model = Adies
    form_class = AdiesForm
    template_name = 'main/forms/adiesForm.html'

    def form_valid(self, form):
        self.mathitis = get_object_or_404(InfoMathiti, id=self.kwargs['pk'])
        form.instance.mathitis = self.mathitis
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        mathitis = get_object_or_404(InfoMathiti, id=pk)
        context['adies'] = Adies.objects.filter(mathitis=mathitis.id)
        return context

    success_url = "./gonios"


# mathitis info
class MathitisDetailView(TemplateView):
    template_name = 'main/mathitisDetailView.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        mathitis = get_object_or_404(InfoMathiti, id=pk)
        context['mathitis'] = mathitis
        context['gonios'] = InfoGonios.objects.filter(mathitis=mathitis.id)
        context['provlimata'] = Provlimata.objects.filter(mathitis=mathitis.id)
        context['adies'] = Adies.objects.filter(mathitis=mathitis.id)
        context['paralavi'] = InfoParalavi.objects.filter(mathitis=mathitis.id)

        num = ProgressMathiti.objects.filter(
            mathitis=mathitis.id).filter(epitixia=True).count()
        colorsArray = colorBelt(num)
        context['zoni'] = {
            '1': colorsArray[0],
            '2': colorsArray[1],
            'name': colorsArray[2],
            'num': num
        }
        return context


# search
class AllView(ListView):
    queryset = InfoMathiti.objects.all().order_by(Lower('onoma'))
    template_name = 'main/search/allMathites.html'
    context_object_name = 'mathites'


class SearchView(ListView):
    model = InfoMathiti
    template_name = 'main/search/searchMathites.html'
    context_object_name = 'mathites'
    

    def get_queryset(self):
        query = self.request.GET.get('search')
        postresult4 = []
        result = []
        result1=[]
        result2=[]

        if query:
            if((' ' in query) == True):
                fullname = query.split()
                result1 = InfoMathiti.objects.filter(onoma__contains=fullname[0]).filter(
                    epitheto__contains=fullname[1]).distinct()
                result2 = InfoMathiti.objects.filter(onoma__contains=fullname[1]).filter(
                    epitheto__contains=fullname[0]).distinct()

            postresult1 = InfoMathiti.objects.filter(
                onoma__contains=query).distinct()
            postresult2 = InfoMathiti.objects.filter(
                epitheto__contains=query).distinct()
            postresult3 = InfoMathiti.objects.filter(
                tilefonoS__contains=query).distinct()
            postresult5 = InfoMathiti.objects.filter(
                kinito__contains=query).distinct()
            foreignObject = InfoGonios.objects.filter(
                tilefono__contains=query).values('mathitis_id').distinct()
            if foreignObject:
                mid = set([entry['mathitis_id'] for entry in foreignObject])
                num = str(mid).replace('{', '').replace('}', '')
                numArray = num.split(",")
                for n in numArray:
                    postresult4.extend(
                        InfoMathiti.objects.filter(id=int(n)).distinct())
            result = list(set(itertools.chain(postresult1, postresult2,
                                              postresult3, postresult4, postresult5, result1, result2)))
        else:
            result = None
        return result
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('search')
        return context

# groups


class Groups(CreateView, ListView):
    model = InfoGroups
    form_class = GroupsForm
    template_name = 'main/groups.html'

    queryset = InfoGroups.objects.all()
    context_object_name = 'groups'

    success_url = "#"


class GroupsEdit(UpdateView, DeletionMixin):
    model = InfoGroups
    form_class = GroupsEditForm
    template_name = 'main/edit/groupEdit.html'

    def post(self, request, *args, **kwargs):
        if "delete" in self.request.POST:
            return self.delete(request, *args, **kwargs)

    success_url = reverse_lazy('main:groups')


# edit


class EnergosEdit(UpdateView):
    model = InfoMathiti
    form_class = EnergoiForm
    template_name = 'main/edit/energosEdit.html'
    success_url = "/all"

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        mathitis = get_object_or_404(InfoMathiti, id=pk)
        context['mathitis'] = mathitis
        num = ProgressMathiti.objects.filter(
            mathitis=mathitis.id).filter(epitixia=True).count()
        colorsArray = colorBelt(num)
        context['zoni'] = {
            '1': colorsArray[0],
            '2': colorsArray[1],
            'name': colorsArray[2],
            'num': num
        }
        return context


class MathitisEdit(UpdateView,DeletionMixin):
    model = InfoMathiti
    form_class = MathitisEditForm
    template_name = 'main/edit/mathitisEdit.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        mathitis = get_object_or_404(InfoMathiti, id=pk)
        context['groups'] = InfoGroups.objects.all()
        context['mathitis'] = mathitis
        return context
    
    def form_valid(self, form, *args, **kwargs):
        if "delete" in self.request.POST:
            return self.delete(request, *args, **kwargs)
        return super().form_valid(form)

    def get_success_url(self):
        if "delete" in self.request.POST:
            return reverse('main:home')
        return reverse('main:mathiti_detail_view', args=(self.object.id,))


class ProvlimataEdit(UpdateView):
    model = Provlimata
    form_class = ProvlimataEditForm
    template_name = 'main/edit/provlimataEdit.html'

    def form_valid(self, form):
        self.mathitis = get_object_or_404(InfoMathiti, id=self.kwargs['pk'])
        form.instance.mathitis = self.mathitis
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        mathitis = get_object_or_404(InfoMathiti, id=pk)
        context['mathitis'] = mathitis
        return context

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, id=self.kwargs['f_pk'])

    def get_success_url(self):
        return reverse('main:mathiti_detail_view', args=(self.object.id,))


class AdiesEdit(UpdateView):
    model = Adies
    form_class = AdiesEditForm
    template_name = 'main/edit/adiesEdit.html'

    def form_valid(self, form):
        self.mathitis = get_object_or_404(InfoMathiti, id=self.kwargs['pk'])
        form.instance.mathitis = self.mathitis
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        mathitis = get_object_or_404(InfoMathiti, id=pk)
        context['mathitis'] = mathitis
        return context

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, id=self.kwargs['f_pk'])

    def get_success_url(self):
        return reverse('main:mathiti_detail_view', args=(self.object.id,))


class GoniosEdit(UpdateView, DeletionMixin):
    model = InfoGonios
    form_class = GoniosEditForm
    template_name = 'main/edit/goniosEdit.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        mathitis = get_object_or_404(InfoMathiti, id=pk)
        context['mathitis'] = mathitis
        return context

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, id=self.kwargs['f_pk'])

    def get_success_url(self):
        self.mathitis = get_object_or_404(InfoMathiti, id=self.kwargs['pk'])
        return reverse('main:mathiti_detail_view', args=(self.mathitis.id,))

    def form_valid(self, form, *args, **kwargs):
        self.mathitis = get_object_or_404(InfoMathiti, id=self.kwargs['pk'])
        form.instance.mathitis = self.mathitis
        if "delete" in self.request.POST:
            return self.delete(request, *args, **kwargs)
        return super().form_valid(form)


class ParalaviEdit(UpdateView, DeletionMixin):
    model = InfoParalavi
    form_class = ParalaviEditForm
    template_name = 'main/edit/paralaviEdit.html'

    def form_valid(self, form, *args, **kwargs):
        self.mathitis = get_object_or_404(InfoMathiti, id=self.kwargs['pk'])
        form.instance.mathitis = self.mathitis
        if "delete" in self.request.POST:
            return self.delete(request, *args, **kwargs)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        mathitis = get_object_or_404(InfoMathiti, id=pk)
        context['mathitis'] = mathitis
        return context

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, id=self.kwargs['f_pk'])

    def get_success_url(self):
        self.mathitis = get_object_or_404(InfoMathiti, id=self.kwargs['pk'])
        return reverse('main:mathiti_detail_view', args=(self.mathitis.id,))


# add
class GoniosAdd(CreateView):
    model = InfoGonios
    form_class = GoniosAdd
    template_name = 'main/add/goniosAdd.html'

    def form_valid(self, form):
        self.mathitis = get_object_or_404(InfoMathiti, id=self.kwargs['pk'])
        form.instance.mathitis = self.mathitis
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        mathitis = get_object_or_404(InfoMathiti, id=pk)
        context['mathitis'] = mathitis
        context['gonios'] = InfoGonios.objects.filter(mathitis=mathitis.id)

        return context
    success_url = "#"


class ParalaviAdd(CreateView):
    model = InfoParalavi
    form_class = ParalaviAdd
    template_name = 'main/add/paralaviAdd.html'

    def form_valid(self, form):
        self.mathitis = get_object_or_404(InfoMathiti, id=self.kwargs['pk'])
        form.instance.mathitis = self.mathitis
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        mathitis = get_object_or_404(InfoMathiti, id=pk)
        context['mathitis'] = mathitis
        context['gonios'] = InfoGonios.objects.filter(mathitis=mathitis.id)
        context['paralavi'] = InfoParalavi.objects.filter(mathitis=mathitis.id)

        return context
    success_url = "#"


# exetasi
class ProgressForm(CreateView):
    model = ProgressMathiti
    form_class = ProgressForm
    template_name = 'main/exam.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        mathitis = get_object_or_404(InfoMathiti, id=pk)
        context['mathitis'] = mathitis
        context['progress'] = ProgressMathiti.objects.filter(
            mathitis=mathitis.id)
        num = ProgressMathiti.objects.filter(
            mathitis=mathitis.id).filter(epitixia=True).count()
        colorsArray = colorBelt(num)
        context['colors'] = {
            '1': colorsArray[0],
            '2': colorsArray[1],
            'num': num
        }
        return context

    def form_valid(self, form):
        self.mathitis = get_object_or_404(InfoMathiti, id=self.kwargs['pk'])
        form.instance.mathitis = self.mathitis
        return super().form_valid(form)
    success_url = "#"


class ProgressEdit(UpdateView, DeletionMixin):
    model = ProgressMathiti
    form_class = ProgressEditForm
    template_name = 'main/edit/examEdit.html'

    def form_valid(self, form, *args, **kwargs):
        self.mathitis = get_object_or_404(InfoMathiti, id=self.kwargs['pk'])
        form.instance.mathitis = self.mathitis
        if "delete" in self.request.POST:
            return self.delete(request, *args, **kwargs)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        mathitis = get_object_or_404(InfoMathiti, id=pk)
        context['mathitis'] = mathitis
        return context

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, id=self.kwargs['f_pk'])

    def get_success_url(self):
        self.mathitis = get_object_or_404(InfoMathiti, id=self.kwargs['pk'])
        return reverse('main:progress', args=(self.mathitis.id,))

    
def ParousiologioView(request, pk):
    template_name = 'main/parousiologio.html'
    ParousiologioFormset = formset_factory(ParousiologioForm,extra=InfoMathiti.objects.filter(group=pk).count())
    if request.method == 'GET':
        formset = ParousiologioFormset(request.GET or None)
    elif request.method == 'POST':
        formset = ParousiologioFormset(request.POST)
        
        if formset.is_valid():
            for form in formset:
                form.save()
            return redirect('/')
    return render(request, template_name, {
        'formset': formset,
        'mathites': InfoMathiti.objects.filter(group=pk).order_by(Lower('onoma'))
        }
    )