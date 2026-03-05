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


# Temas
TEMA_CLARO = {
    "bg_janela": "white",
    "bg_entrada": "white",
    "fg_entrada": "black",
    "bg_botao": "lightgray",
    "fg_botao": "black",
    "bg_frame": "lightgray"
}

TEMA_ESCURO = {
    "bg_janela": "#1e1e1e",
    "bg_entrada": "#2d2d2d",
    "fg_entrada": "white",
    "bg_botao": "#3d3d3d",
    "fg_botao": "white",
    "bg_frame": "#2d2d2d"
}