from django.shortcuts import render

def detection_view(request):
    return render(request, 'detection.html')

def npk_view(request):
    return render(request, 'NPK.html')

def crop_view(request):
    return render(request, 'crop.html')

def chart_view(request):
    return render(request, 'chart.html')

def chart_view(request):
    return render(request, 'community.html')
