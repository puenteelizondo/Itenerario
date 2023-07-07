from django.http import JsonResponse

from usuarios.models import usuarios
from usuario_root.models import usuario_root

#validamos que en la tabla de usuarios este el token
def validate_token(token):
    try:
        #si esta que devuelve un tru sino un false
        usuarios.objects.get(token=token)
        return True
#cualquier exepcion que se levante cae aqui
    except Exception:
        return False


def validate_token_usuario_root(token):
    try:
        #si esta que devuelve un tru sino un false
        usuario_root.objects.get(token=token)
        return True
#cualquier exepcion que se levante cae aqui
    except Exception:
        return False
    