from django.shortcuts import render


def vice_versa(request):
    return render(request, 'vice_versa.html')
