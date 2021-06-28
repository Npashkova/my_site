from django.shortcuts import render


def vice_versa(request):
    return render(request, 'vice_versa.html')


def reverse(request):
    dop_info = request.GET['dop_info']
    reversed_info = dop_info[::-1]
    words_number = len(dop_info.split())
    return render(request, 'reverse.html', {'info': reversed_info, 'wn': words_number})

