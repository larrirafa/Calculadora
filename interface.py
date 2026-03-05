import tkinter
import config

class Interface:
    def __init__(self, parent, callbacks, cores):
        self.parent = parent
        self.callbacks = callbacks
        self.cores = cores
        
    def criar_entrada(self):
        entrada = tkinter.Entry(self.parent, width=1, font=config.FONTE_ENTRADA, justify="center")
        entrada.grid(row=1, column=1, columnspan=2, padx=20, pady=10, sticky="nsew")

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
                relief="ridge",
                bg=self.cores["bg_botao"],  # ← Adiciona
                fg=self.cores["fg_botao"]
            )
            # Cria variáveis pra armazenar a cor original
            cor_original = self.cores["bg_botao"]
            cor_hover = self.clarear_cor(cor_original)
            
            btn.grid(row=row, column=col, padx=0.5, pady=0.5, sticky="nsew")
            btn.bind("<Enter>", lambda e, b=btn, c=cor_hover: b.config(bg=c))
            btn.bind("<Leave>", lambda e, b=btn, c=cor_original: b.config(bg=c))
            
            
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


            cor_original = cor
            cor_hover = self.clarear_cor(cor_original)
            
            btn.grid(row=row, column=col, padx=0.5, pady=0.5, sticky="nsew")
            btn.bind("<Enter>", lambda e, b=btn, c=cor_hover: b.config(bg=c))
            btn.bind("<Leave>", lambda e, b=btn, c=cor_original: b.config(bg=c))

            
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
            
            cor_original = cor
            cor_hover = self.clarear_cor(cor_original)
            
            btn.grid(row=row, column=col, padx=0.5, pady=0.5, sticky="nsew")
            btn.bind("<Enter>", lambda e, b=btn, c=cor_hover: b.config(bg=c))
            btn.bind("<Leave>", lambda e, b=btn, c=cor_original: b.config(bg=c))

    def criar_todos_botoes(self):
        self.criar_botoes_numeros()
        self.criar_botoes_operacoes()
        self.criar_botoes_especiais()