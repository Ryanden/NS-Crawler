from django.shortcuts import render

__all__ = (
    'recipe_list',
)


def recipe_list(request):
    context = {
        'recipe': '레시피'
    }

    return render(request, 'products/recipe.html', context)
