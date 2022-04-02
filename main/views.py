from django.shortcuts import render
from.models import Articles

def index(request):
    data = {
        'title': 'Главная старница',
        'obj': {
            'Age': 'Age=18',
            'Hobby': 'Hobby=Game,Drawing',
            'Name': 'Name=Daria'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    Ff = {
        'title': 'Стихи',
        'obj': {
            'С':"Рисуй меня пеплом наброском на камне, "
                "Обмытый водой взор покинутых душ, "
                "Будто моря плещут между морями, "
                "Теряя из виду мольберты из суш. "
                "пусть краски текут, "
                "создают новые линии; "
                "Липкие и вязким телом "
                "растушуй диссонанс "
                "выходить из воды, когда "
                "губы легкой мягкости синие."
                "Cлияние холстов - погружение в транс ",

        }
    }
    return render(request, 'main/about.html', Ff)

