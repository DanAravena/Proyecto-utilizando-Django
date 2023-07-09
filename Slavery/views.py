from django.http import HttpResponse

#Request: para realizar peticiones.
#HttpResponse: para enviar la respuesta al protocolo HTTP.

#esto es una vista
def Bienvenido(request):
    return HttpResponse("Bienvenido a este curso de Django.=)")