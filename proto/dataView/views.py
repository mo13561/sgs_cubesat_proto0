from django.shortcuts import render

# Create your views here.


def liveData(request):
    input_array = []
    # input array is list of dictionaries with name, value as two keys.
    return render(request, "dataView/liveDataView.html", {
        'input_array': input_array
    })
