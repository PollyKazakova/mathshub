from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def init(request):
    name = "Казакова Полина Геннадьевна"
    return HttpResponse(f'''
    <h1>"Изучаем django"</h1>
<strong>Автор</strong>: <i>{name}</i>''')


def about(request):
    first_name = "Полина"
    middle_name = "Геннадьевна"
    last_name = "Казакова"
    phone = "8-912-701-21-73"
    mail = "kozlovapolya@gmail.com"
    return HttpResponse(f'''
<strong>Имя</strong>: <i>{first_name}</i><br> 
<strong>Отчество</strong>: <i>{middle_name}</i><br>
<strong>Фамилия</strong>: <i>{last_name}</i><br>
<strong>телефон</strong>: <i>{phone}</i><br>
<strong>email</strong>: <i>{mail}</i><br>''')

items = [
   {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
   {"id": 2, "name": "Куртка кожаная", "quantity": 2},
   {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
   {"id": 7, "name": "Картофель фри", "quantity": 0},
   {"id": 8, "name": "Кепка", "quantity": 124}
]
def item(request, id):
    global items
    dictionary = {}
    for i in range(len(items)):
        dictionary[items[i]["id"]] = i
    if id not in dictionary.keys():
        return HttpResponse(f'''
        <h1>"Товар с id={id} не найден"</h1>''')
    else:
        return HttpResponse(f'''
    <strong>Название</strong>: <i>{items[dictionary[id]]["name"]}</i><br>
    <strong>Количество</strong>: <i>{items[dictionary[id]]["quantity"]}</i><br>
    <a href="http://127.0.0.1:8000/items">
    назад к списку товаров</a>
    ''')

def items_list(response):
    global items
    dictionary = {}
    for i in range(len(items)):
        dictionary[items[i]["id"]] = items[i]["name"]
    return HttpResponse(f'''
<ol>
<li>{list(dictionary.values())[0]}: <a href="http://127.0.0.1:8000/item/{list(dictionary.keys())[0]}">
ссылка на товар</a></li>
<li>{list(dictionary.values())[1]}: <a href="http://127.0.0.1:8000/item/{list(dictionary.keys())[1]}">
ссылка на товар</a></li></li>
<li>{list(dictionary.values())[2]}: <a href="http://127.0.0.1:8000/item/{list(dictionary.keys())[2]}">
ссылка на товар</a></li></li>
<li>{list(dictionary.values())[3]}: <a href="http://127.0.0.1:8000/item/{list(dictionary.keys())[3]}">
ссылка на товар</a></li></li>
<li>{list(dictionary.values())[4]}: <a href="http://127.0.0.1:8000/item/{list(dictionary.keys())[4]}">
ссылка на товар</a></li></li>
</ol>
''')
