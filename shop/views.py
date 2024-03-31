from django.shortcuts import render


def main(request):

    context = {
        'page': 'main'
    }

    return render(request, 'shop/main.html', context=context)


def shops(request):

    context = {
        'page': 'shops'
    }

    return render(request, 'shop/shops.html', context=context)


def categories(request):

    context = {
        'page': 'categories'
    }

    return render(request, 'shop/categories.html', context=context)
