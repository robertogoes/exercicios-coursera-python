import bhaskara
import pytest

class TestBhaskara:


    @pytest.mark.parametrize("a,b,c, esperado", [
        (1, 0, 0, (1, 0)),
        (1, -5, 6, (2, 3, 2)),
        (10, 10, 10, 0),
        (10, 20, 10, (1, -1)),
        (12, 32, 19, (2, 1, 3))
    ])
# estou passando o valor de cada termo para a funçao testa_raiz

    def testa_raiz(self, a, b, c, esperado):
        d = bhaskara.bhaskara()
        assert d.calcula_raizes(a, b, c) == esperado

    
         

