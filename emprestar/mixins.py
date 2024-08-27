from .models import Emprestar

class EmprestarMixin:
    def get_emprestimos(self):
        return Emprestar.objects.all()