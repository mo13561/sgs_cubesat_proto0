from django.shortcuts import render, redirect

# Create your views here.


def redirectLiveData(request):
    return redirect('live')


def liveData(request):
    input_array = []
    # input array is list of dictionaries with name, value as two keys.
    return render(request, "dataView/liveDataView.html", {
        'input_array': input_array
    })
