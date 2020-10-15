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
                answer["error"] = 'Введенный параметр не является числом!'
                response = JsonResponse(answer)
                response.status_code = 400
                return response
        a = int(data['A'])
        b = int(data['B'])
        try:
            sum = a + b
        except Exception:
            answer["error"] = "Ошибка во время расчетов!"
            response = JsonResponse(answer)
            response.status_code = 400
            return response
        answer['answer'] = sum
        return JsonResponse(answer)

# @ensure_csrf_cookie
def subtract(request, *args, **kwargs):
    answer = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        for key, value in data.items():
            if is_int(value):
                pass
            else:
                answer["error"] = 'Введенный параметр не является числом!'
                response = JsonResponse(answer)
                response.status_code = 400
                return response
        a = int(data['A'])
        b = int(data['B'])
        print(b)
        try:
            sum = a - b
        except Exception:
            answer["error"] = "Ошибка во время расчетов!"
            response = JsonResponse(answer)
            response.status_code = 400
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
                answer["error"] = 'Введенный параметр не является числом!'
                response = JsonResponse(answer)
                response.status_code = 400
                return response
        a = int(data['A'])
        b = int(data['B'])
        try:
            sum = a * b
        except Exception:
            answer["error"] = "Ошибка во время расчетов!"
            response = JsonResponse(answer)
            response.status_code = 400
            return response
        answer['answer'] = sum
        return JsonResponse(answer)

# @ensure_csrf_cookie
def divide(request, *args, **kwargs):
    answer = {}
    print(request.headers)
    if request.method == 'POST':
        data = json.loads(request.body)
        for key, value in data.items():
            if is_int(value):
                pass
            else:
                answer["error"] = 'Введенный параметр не является числом!'
                response = JsonResponse(answer)
                response.status_code = 400
                return response
                # return HttpResponseBadRequest('Введенный параметр не является числом!')
        a = int(data['A'])
        b = int(data['B'])
        try:
            sum = a / b
            print(a,b)
        except ZeroDivisionError:
            answer["error"] = "Ошибка во время расчетов! Division by zero!"
            response = JsonResponse(answer)
            response.status_code = 400
            return response
        answer['answer'] = sum
        return JsonResponse(answer)
