from django.shortcuts import render


def main(request):
    context = {'message': 'My message'}
    return render(request, 'main.html', context)

