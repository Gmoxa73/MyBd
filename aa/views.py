from django.shortcuts import render
from rest_framework.generics import ListAPIView, get_object_or_404
from .models import Devices, Raions
from .serializers import DevicesSerializer


class ListView(ListAPIView):
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer


def view(request):
    raions = Raions.objects.all().order_by('raion')
    template = 'start.html'
    context = {
        'raions': raions,
    }
    return render(request, template, context)


def raion_detail(request, pk):
    raion = get_object_or_404(Raions, pk=pk)
    return render(request, 'raion_detail.html', {'raion': raion})


def device_detail(request, pk):
    device = get_object_or_404(Devices, pk=pk)
    return render(request, 'device_detail.html', {'device': device})


def destination_page(request, addr_id):
    return render(request, 'destination_page.html', {'addr_id': addr_id})
