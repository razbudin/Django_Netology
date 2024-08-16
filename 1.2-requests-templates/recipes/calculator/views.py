from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'julienne': {
        'Филе куриное, г': 400,
        'Грибы шампиньоны, г': 300,
        'Лук репчатый, г': 100,
        'Сливки 20-30%, мл': 200,
        'Сыр твердый, г': 150,
        'Масло растительное, ст.л': 2,
    },
    'shkmeruli': {
        'Курица, г': 600,
        'Молоко, мл': 100,
        'Вода, мл': 80,
        'Чеснок, головка': 1,
        'Масло растительное, мл': 30
    },
}


def home(request):
    data = {'data': DATA}
    return render(request, 'calculator/home.html', context=data)


def dish_ingredients(request, dish):
    servings = int(request.GET.get("servings", 1))
    food = DATA.get(dish)
    ingredients = {}
    if food is not None:
        for key, value in food.items():
            ingredients[key] = round(value * servings, 3)
    data = {
        'dish': dish,
        'recipe': ingredients,
        'servings': servings
    }
    return render(request, 'calculator/index.html', context=data)
