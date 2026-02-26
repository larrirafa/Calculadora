import config

TITULO = "Calculadora LARRI"
LARGURA = 400
ALTURA = 500
POS_X = 700
POS_Y = 300

# Botões numéricos
BOTOES_NUMEROS = [
    (1, 2, 1), (2, 2, 2), (3, 2, 3),
    (4, 3, 1), (5, 3, 2), (6, 3, 3),
    (7, 4, 1), (8, 4, 2), (9, 4, 3),
    (0, 5, 2)
]

# Botões de operações
BOTOES_OPERACOES = [
    ("=", 4, 5, "green"),
    ("+", 3, 5, "orange"),
    ("-", 2, 5, "orange"),
    ("x", 1, 5, "orange"),
    ("/", 5, 5, "orange")
]

# Botões especiais
BOTOES_ESPECIAIS = [
    ("C", 5, 1, "red"),
    ("%", 5, 3, "blue"),
    ("back", 1, 3, "gray")
]

PADDING = 5

# Fonte da entrada
FONTE_ENTRADA = ("Arial", 24, "bold")