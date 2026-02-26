import tkinter
import config

class Interface:
    def __init__(self, parent, callbacks):
        self.parent = parent
        self.callbacks = callbacks
        
    def criar_entrada(self):
        entrada = tkinter.Entry(self.parent, width=10, font=config.FONTE_ENTRADA, justify="center")
        entrada.grid(row=1, columnspan=3, ipadx=5, ipady=5, sticky="nsew")

        return entrada
    

    def clarear_cor(self, cor):
        """Deixa a cor mais clara"""
        cores = {
            "green": "#90EE90",
            "orange": "#FFD700",
            "red": "#FF6B6B",
            "blue": "#87CEEB",
            "gray": "#D3D3D3"
        }
        return cores.get(cor, cor)
    
    def criar_botoes_numeros(self):
        for numero, row, col in config.BOTOES_NUMEROS:
            btn = tkinter.Button(
                self.parent,
                text=numero,
                command=lambda n=numero: self.callbacks['numero'](n),
                font=("Arial", 16, "bold"),
                width=8,
                height=3,
                bd=5, 
                relief="ridge"
            )
            btn.grid(row=row, column=col, padx=0.5, pady=0.5, sticky="nsew")
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="lightgray"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg="SystemButtonFace"))

    def criar_botoes_operacoes(self):
        for operacao, row, col, cor in config.BOTOES_OPERACOES:
            btn = tkinter.Button(
                self.parent,
                text=operacao,
                command=lambda op=operacao: self.callbacks['operacao'](op),
                bg=cor,
                fg='white',
                font=("Arial", 18, "bold"),
                width=5,
                height=2,
                bd=3, 
                relief="ridge", # Estilo da borda
                foreground="lightgray"
            )

            btn.grid(row=row, column=col, padx=config.PADDING, pady=config.PADDING, sticky="nsew")
            btn.bind("<Enter>", lambda e, b=btn, c=cor: b.config(bg=self.clarear_cor(c)))
            btn.bind("<Leave>", lambda e, b=btn, c=cor: b.config(bg=c))

            
    def criar_botoes_especiais(self):
        for especial, row, col, cor in config.BOTOES_ESPECIAIS:
            btn = tkinter.Button(
                self.parent,
                text=especial,
                command=lambda esp=especial: self.callbacks['especial'](esp),
                bg=cor,
                fg='white',
                font=("Arial", 18, "bold"),
                width=5,
                height=2,
                bd=3, 
                relief="ridge" # Estilo da borda
            )
            btn.grid(row=row, column=col, padx=config.PADDING, pady=config.PADDING, sticky="nsew")
            btn.bind("<Enter>", lambda e, b=btn, c=cor: b.config(bg=self.clarear_cor(c)))  # ✅ Aqui
            btn.bind("<Leave>", lambda e, b=btn, c=cor: b.config(bg=c))

    def criar_todos_botoes(self):
        self.criar_botoes_numeros()
        self.criar_botoes_operacoes()
        self.criar_botoes_especiais()