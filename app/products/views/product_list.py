from django.shortcuts import render

__all__ = (
    'product_list',
)


def product_list(request):
    return render(request, 'index.html')
