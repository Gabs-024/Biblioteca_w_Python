import sys
import os

from emprestimo.models import Emprestimo

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class HistoricoLivroMixin:
    def get_historico_emprestimos(self):
        from emprestimo.models import Emprestimo
        livro_id = self.kwargs.get('pk')  
        return Emprestimo.objects.filter(livro_emprestar=livro_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['historico'] = self.get_historico_emprestimos()
        return context
