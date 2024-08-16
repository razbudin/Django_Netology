from django.urls import path
from calculator.views import home, dish_ingredients

urlpatterns = [
    # здесь зарегистрируйте вашу view-функцию
    path('', home),
    path('<str:dish>/', dish_ingredients),
]
