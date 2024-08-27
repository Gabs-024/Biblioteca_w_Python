from .models import Devolver

class DevolucaoMixin:
    def get_devolucao(self):
        return Devolver.objects.all()