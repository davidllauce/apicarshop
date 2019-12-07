from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Product.models import Product

# Create your views here.

"""Toma una lista de métodos permitidos para la vista como argumento."""


# '''Marcar una función de vista como exenta de la protección de vista CSRF'''
@csrf_exempt
# """Toma una lista de métodos permitidos para la vista como argumento."""
@api_view(["POST"])
def createBasket(request):
    '''
    :param request: string name
    :return: json
    '''
    if request.method == 'POST':
        usuario = request.data['name']
        try:
            response = HttpResponse("")
            usuario = request.user
            if not request.COOKIES.get(str(usuario)):
                response.set_cookie(str(usuario), '')
            mss = {
                'msg': 'creado'
            }
            return Response(mss, status=status.HTTP_200_OK)

        except ValueError:
            mss = {
                'msg': 'fail'
            }
            return Response(mss, status=status.HTTP_400_BAD_REQUEST)


# '''Marcar una función de vista como exenta de la protección de vista CSRF'''
@csrf_exempt
# """Toma una lista de métodos permitidos para la vista como argumento."""
@api_view(["POST"])
def addProduct(request):
    """
    :param request: String code , int cantidad , String name
    :return:
    """
    actualizado = False
    articulo = request.data['code']
    cantidad = request.data['cantidad']
    usuario = request.data['name']
    response = HttpResponseRedirect(request.GET.get('next'))
    if request.COOKIES.get(str(usuario)) != '':
        carrito = request.COOKIES[str(usuario)]
        if carrito != "":
            lista = carrito.split(';')
            carrito = ""
            for element in lista:
                if element != "":
                    element = element.split('=')
                    if element[0] == articulo:
                        cantidad = int(cantidad) + int(element[1])
                        actualizado = True
                    if element[1] != 0:
                        print(str(element[1]))
                        carrito += str(element[0]) + "=" + str(cantidad) + ";"
        if actualizado is False:
            carrito += articulo + '=' + str(cantidad) + ';'
            print(carrito)
        response.set_cookie(str(usuario), carrito)
    else:
        response.set_cookie(str(usuario), articulo + '=' + str(cantidad) + ';')
    mss = {
        'msg': 'agregado'
    }
    return Response(mss,
                    status=status.HTTP_200_OK)


# '''Marcar una función de vista como exenta de la protección de vista CSRF'''

@csrf_exempt
# """Toma una lista de métodos permitidos para la vista como argumento."""
@api_view(["POST"])
def sumProduct(request):
    """
    :param request:  String name
    :return:
    """
    total = 0.0;
    usuario = request.data['name']
    if request.COOKIES.get(str(usuario)) != '':
        carrito = request.COOKIES[str(usuario)]
        if carrito != "":
            lista = carrito.split(';')
            for element in lista:
                if element != "":
                    element = element.split('=')
                    try:
                        precio = Product.objects.filter(code=str(element[0]))[0].price
                        if element[1] > 2 and element[0] == 'TSHIRT':
                            total += element[1] * (precio - 1)

                        if element[1] > 2 and element[0] == 'VOUCHER':
                            if element[1] % 2 == 0 and element[1] > 2:
                                total += element[1] / 2 * precio
                            else:
                                total += (element[1] - 1) / 2 * precio + precio
                        else:
                            total += element[1] * precio
                    except Product.DoesNotExist:
                        mss = {
                            'msg': 'error'
                        }
                        return Response(mss, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    mss = {
        'msg': 'error'
    }
    return Response(mss, status=status.HTTP_200_OK)
