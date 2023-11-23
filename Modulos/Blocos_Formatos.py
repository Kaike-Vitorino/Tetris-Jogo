from Bloco_Unitario import*
from Posicao import *

# Classe Bloco_em_L herda da classe Bloco
class Bloco_em_L(Bloco):
    def __init__(self):
        # Inicializa a classe base (Bloco) com ID 1
        super().__init__(id=1)
        # Define as células do bloco em diferentes estados de rotação
        self.celulas = {
            0: [Posicao(0, 2), Posicao(1, 0), Posicao(1, 1), Posicao(1, 2)],
            1: [Posicao(0, 1), Posicao(1, 1), Posicao(2, 1), Posicao(2, 2)],
            2: [Posicao(1, 0), Posicao(1, 1), Posicao(1, 2), Posicao(2, 0)],
            3: [Posicao(0, 0), Posicao(0, 1), Posicao(1, 1), Posicao(2, 1)]
        }
        # Move o bloco inicialmente
        self.mover(0, 3)

# Classe Bloco_em_J herda da classe Bloco
class Bloco_em_J(Bloco):
    def __init__(self):
        # Inicializa a classe base (Bloco) com ID 2
        super().__init__(id=2)
        # Define as células do bloco em diferentes estados de rotação
        self.celulas = {
            0: [Posicao(0, 0), Posicao(1, 0), Posicao(1, 1), Posicao(1, 2)],
            1: [Posicao(0, 1), Posicao(0, 2), Posicao(1, 1), Posicao(2, 1)],
            2: [Posicao(1, 0), Posicao(1, 1), Posicao(1, 2), Posicao(2, 2)],
            3: [Posicao(0, 1), Posicao(1, 0), Posicao(1, 1), Posicao(2, 1)]
        }
        # Move o bloco inicialmente
        self.mover(0, 3)

# Classe Bloco_em_I herda da classe Bloco
class Bloco_em_I(Bloco):
    def __init__(self):
        # Inicializa a classe base (Bloco) com ID 3
        super().__init__(id=3)
        # Define as células do bloco em diferentes estados de rotação
        self.celulas = {
            0: [Posicao(1, 0), Posicao(1, 1), Posicao(1, 2), Posicao(1, 3)],
            1: [Posicao(0, 2), Posicao(1, 2), Posicao(2, 2), Posicao(3, 2)],
            2: [Posicao(2, 0), Posicao(2, 1), Posicao(2, 2), Posicao(2, 3)],
            3: [Posicao(0, 1), Posicao(1, 1), Posicao(2, 1), Posicao(3, 1)]
        }
        # Move o bloco inicialmente
        self.mover(-1, 3)

# Classe Bloco_em_O herda da classe Bloco
class Bloco_em_O(Bloco):
    def __init__(self):
        # Inicializa a classe base (Bloco) com ID 4
        super().__init__(id=4)
        # Define as células do bloco em diferentes estados de rotação
        self.celulas = {
            0: [Posicao(0, 0), Posicao(0, 1), Posicao(1, 0), Posicao(1, 1)]
        }
        # Move o bloco inicialmente
        self.mover(0, 4)

# Classe Bloco_em_S herda da classe Bloco
class Bloco_em_S(Bloco):
    def __init__(self):
        # Inicializa a classe base (Bloco) com ID 5
        super().__init__(id=5)
        # Define as células do bloco em diferentes estados de rotação
        self.celulas = {
            0: [Posicao(0, 1), Posicao(0, 2), Posicao(1, 0), Posicao(1, 1)],
            1: [Posicao(0, 1), Posicao(1, 1), Posicao(1, 2), Posicao(2, 2)],
            2: [Posicao(1, 1), Posicao(1, 2), Posicao(2, 0), Posicao(2, 1)],
            3: [Posicao(0, 0), Posicao(1, 0), Posicao(1, 1), Posicao(2, 1)]
        }
        # Move o bloco inicialmente
        self.mover(0, 3)

# Classe Bloco_em_T herda da classe Bloco
class Bloco_em_T(Bloco):
    def __init__(self):
        # Inicializa a classe base (Bloco) com ID 6
        super().__init__(id=6)
        # Define as células do bloco em diferentes estados de rotação
        self.celulas = {
            0: [Posicao(0, 1), Posicao(1, 0), Posicao(1, 1), Posicao(1, 2)],
            1: [Posicao(0, 1), Posicao(1, 1), Posicao(1, 2), Posicao(2, 1)],
            2: [Posicao(1, 0), Posicao(1, 1), Posicao(1, 2), Posicao(2, 1)],
            3: [Posicao(0, 1), Posicao(1, 0), Posicao(1, 1), Posicao(2, 1)]
        }
        # Move o bloco inicialmente
        self.mover(0, 3)

# Classe Bloco_em_Z herda da classe Bloco
class Bloco_em_Z(Bloco):
    def __init__(self):
        # Inicializa a classe base (Block) com ID 7
        super().__init__(id=7)
        # Define as células do bloco em diferentes estados de rotação
        self.cells = {
            0: [Posicao(0, 0), Posicao(0, 1), Posicao(1, 1), Posicao(1, 2)],
            1: [Posicao(0, 2), Posicao(1, 1), Posicao(1, 2), Posicao(2, 1)],
            2: [Posicao(1, 0), Posicao(1, 1), Posicao(2, 1), Posicao(2, 2)],
            3: [Posicao(0, 1), Posicao(1, 0), Posicao(1, 1), Posicao(2, 0)]
        }
        # Move o bloco inicialmente
        self.mover(0, 3)