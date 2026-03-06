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
    ("=", 4, 5, "#c084fc"),
    ("+", 3, 5, "#c084fc"),
    ("-", 2, 5, "#c084fc"),
    ("x", 1, 5, "#c084fc"),
    ("/", 5, 5, "#c084fc")
]

# Botões especiais
BOTOES_ESPECIAIS = [
    ("C", 5, 1, "#FF0000"),
    ("%", 5, 3, "#0000FF"),
    ("back", 1, 3, "#A9A9A9")
]

PADDING = 5

# Fonte da entrada
FONTE_ENTRADA = ("Segoe UI", 24, "bold")
FONTE_BOTAO = ("Segoe UI", 14, "bold")


# Temas
TEMA_CLARO = {
    "bg_janela": "#f5f5f5",
    "bg_entrada": "#ece9e9",
    "fg_entrada": "#1a1a1a",
    "bg_botao": "#e0e0e0",
    "fg_botao": "#1a1a1a",
    "bg_frame": "#ffffff",
    "cor_destaque": "#8b5cf6"  # Roxo
}

TEMA_ESCURO = {
    "bg_janela": "#0f0f1e",      # Preto azulado
    "bg_entrada": "#1a1a2e",     # Cinza escuro
    "fg_entrada": "#e0e0e0",     # Branco suave
    "bg_botao": "#16213e",       # Azul escuro
    "fg_botao": "#c084fc",       # Roxo claro
    "bg_frame": "#0f0f1e",
    "cor_destaque": "#c084fc"    # Roxo/Rosa
}