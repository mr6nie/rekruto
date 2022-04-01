from django.shortcuts import render
from django.http import JsonResponse


def hello_rekruto(request):
    if request.method == "GET":

        name = request.GET.get("name")
        message = request.GET.get("message")

        return render(
            request, "hello_rekruto.html", context={"name": name, "message": message}
        )

        # --------------- Для получения данных в JSON -----------------

        # data = {"hello": "Hello", "name": name, "message": message}
        # return JsonResponse(data)
