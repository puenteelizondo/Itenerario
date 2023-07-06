from django.shortcuts import render
import json

from django.http import HttpResponse, JsonResponse

from Registro.models import Locales
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def crear_local (request):
    if request.method == "POST":
        datos = json.loads(request.body)
        locales = Locales.objects.create(
             nombre=datos["nombre"],
             ubicacion=datos["ubicacion"],
              horario=datos["horario"],
            )
        return JsonResponse({
                 "message":"Creado correctamente",
                 
                }, status=201)
    else:
        # devolvemos el metodo de no encontrado porque necesitamos siempre devolver un status
        return JsonResponse(
            {"message": "metodo no permitido"},
            status=405,
        )
    
def lista_de_locales(request):
    # solo se permite get
    if request.method == "GET":
       
        # de la aplicacion traer todos los objetos de la tabla clientes
        # como ya se crea un id automatico en la base de datos solo lo que se hace es traerlo en el json
        response = [
            {
                "id": Registro.id,
                "name": Registro.nombre,
                "price": Registro.ubicacion,
                "category": Registro.horario,
            }
            for Registro in Locales.objects.all()
        ]
        # devolvemos en forma de diccionario los datos extraidos de response e imprimos un 200 de OK de que todo salio bien
        # bueno solo response pero agregamos otro parametro para que no de error safe=false
        return JsonResponse({"data": response}, status=200)
    else:
        # devolvemos el metodo de no encontrado porque necesitamos siempre devolver un status
        return JsonResponse(
            {"message": "metodo no permitido"},
            status=405,
        )
    

def actulizar_local(request, id: int):
    # jalamos lo que tengamos y lo metemos a la variable
    datos = json.loads(request.body)
    if request.method == "PUT":
        
        try:
            # aca traemos solo un objeto con el get
            # y en el parametro le decimos que pk=id porque pk se maneja en la base de datos
            # sino existe se va al 404
            object_to_update = Locales.objects.get(pk=id)
            # ahora que ya encontro actualizamos con la variable que tiene los datos
            object_to_update.nombre = datos["nombre"]
            object_to_update.ubicacion = datos["ubicacion"]
            object_to_update.horario = datos["horario"]
            # cuando es item por item guardamos asi
            object_to_update.save()

            return JsonResponse(
                {
                    "id": object_to_update.id,
                    "nombre": object_to_update.nombre,
                    "ubicacion": object_to_update.ubicacion,
                    "horario": object_to_update.horario,
                },
                status=200,
            )
        # sino encuentra en la base de datos ya entra aqui
        except Locales.DoesNotExist:
            # sino existe en la base de datos que devulva un mensaje que con ese id no existe
            # y el 404 es de no found
            return JsonResponse(
                {"message": f"object with {id} does not exist"}, status=404
            )
        except Exception:
            return JsonResponse({"message": "Internal server error"}, status=500)
    else:
        # devolvemos el metodo de no encontrado porque necesitamos siempre devolver un status
        # porque solo aceptamos gets
        return JsonResponse(
            {"message": "method not allowed"},
            status=405,
        )

def borrar_local(request, id: int):
    # jalamos lo que tengamos y lo metemos a la variable
    #no usamos body porque solo lo jalamos con el id
    
    if request.method == "DELETE":
       
        try:
            # aca traemos solo un objeto con el get
            # y en el parametro le decimos que pk=id porque pk se maneja en la base de datos
            # sino existe se va al 404
            object_to_update = Locales.objects.get(pk=id)
            # ahora que ya encontro borramos el objeto
            
            object_to_update.delete()

            return JsonResponse(
                {
                    "message":"se ha borrado exitosamente"
                },
                #se devuelve un 204 de no contend  quiere decir que se borro correctamente
                status=204,
            )
        # sino encuentra en la base de datos ya entra aqui
        except Locales.DoesNotExist:
            # sino existe en la base de datos que devulva un mensaje que con ese id no existe
            # y el 404 es de no found
            return JsonResponse(
                {"message": f"object with {id} does not exist"}, status=404
            )
        except Exception:
            return JsonResponse({"message": "Internal server error"}, status=500)
    else:
        # devolvemos el metodo de no encontrado porque necesitamos siempre devolver un status
        # porque solo aceptamos gets
        return JsonResponse(
            {"message": "method not allowed"},
            status=405,
        )
    