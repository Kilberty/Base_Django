from inertia import inertia
from django.forms.models import model_to_dict

@inertia('Home')
def home(request):
  usuario_info = request.user
  usuario = model_to_dict(usuario_info, exclude=['password'])
  return {'usuario':usuario}