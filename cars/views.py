from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm
from django.views import View
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search', '')
        if search:
            return cars.filter(model__icontains=search)
        return cars


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'


@method_decorator(login_required, name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'car_update.html'


    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'


@method_decorator(login_required, name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'new_car.html'
    success_url = '/cars/'


'''
    Class Based Views exemples
'''
# class CarsView(View):
#     def get(self, request):
#         cars = Car.objects.all().order_by('model')
#         search = request.GET.get('search', '')

#         if search:
#             cars = Car.objects.filter(model__icontains=search).order_by('model')

#         return render(
#             request,
#             'cars.html',
#             {'cars': cars}
#         )


'''
    Class Based Views exemples
'''
# class NewCarView(View):
#     def get(self, request):
#         new_car_form = CarForm()
#         return render(
#             request,
#             'new_car.html',
#             {'form': new_car_form}
#         )

#     def post(self, request):
#         new_car_form = CarForm(request.POST, request.FILES)

#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('cars_view')

#         return render(
#             request,
#             'new_car.html',
#             {'form': new_car_form}
#         )
