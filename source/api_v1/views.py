import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import ensure_csrf_cookie


def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
    except TypeError:
        return False


# @ensure_csrf_cookie
def add(request, *args, **kwargs):
    answer = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        for key, value in data.items():
            if is_int(value):
                pass
            else:
                return HttpResponseBadRequest('Введенный параметр не является числом!')
        a = int(data['A'])
        b = int(data['B'])
        try:
            sum = a + b
        except Exception:
            answer["error"] = "Ошибка во время расчетов!"
            answer_as_json = json.dumps(answer)
            response = HttpResponseBadRequest(answer_as_json)
            response['Content-Type'] = 'application/json'
            return response
        answer['answer'] = sum
        return JsonResponse(answer)

#@ensure_csrf_cookie
def subtract(request, *args, **kwargs):
    answer = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        for key, value in data.items():
            if is_int(value):
                pass
            else:
                return HttpResponseBadRequest('Введенный параметр не является числом!')
        a = int(data['A'])
        b = int(data['B'])
        print(b)
        try:
            sum = a - b
        except Exception:
            answer["error"] = "Ошибка во время расчетов!"
            answer_as_json = json.dumps(answer)
            response = HttpResponseBadRequest(answer_as_json)
            response['Content-Type'] = 'application/json'
            return response
        answer['answer'] = sum
        return JsonResponse(answer)

# @ensure_csrf_cookie
def multiply(request, *args, **kwargs):
    answer = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        for key, value in data.items():
            if is_int(value):
                pass
            else:
                return HttpResponseBadRequest('Введенный параметр не является числом!')
        a = int(data['A'])
        b = int(data['B'])
        try:
            sum = a * b
        except Exception:
            answer["error"] = "Ошибка во время расчетов!"
            answer_as_json = json.dumps(answer)
            response = HttpResponseBadRequest(answer_as_json)
            response['Content-Type'] = 'application/json'
            return response
        answer['answer'] = sum
        return JsonResponse(answer)

# @ensure_csrf_cookie
def divide(request, *args, **kwargs):
    answer = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        for key, value in data.items():
            if is_int(value):
                pass
            else:
                return HttpResponseBadRequest('Введенный параметр не является числом!')
        a = int(data['A'])
        b = int(data['B'])
        try:
            sum = a / b
        except ZeroDivisionError:
            answer["error"] = "Ошибка во время расчетов! Division by zero!"
            answer_as_json = json.dumps(answer)
            response = HttpResponseBadRequest(answer_as_json)
            response['Content-Type'] = 'application/json'
            return response
        answer['answer'] = sum
        return JsonResponse(answer)
