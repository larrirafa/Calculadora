import tkinter
import config

class Interface:
    def __init__(self, parent, callbacks, cores):
        self.parent = parent
        self.callbacks = callbacks
        self.cores = cores
        
    def criar_entrada(self):
        entrada = tkinter.Entry(
            self.parent,
            width=20,
            font=config.FONTE_ENTRADA,
            justify="center",
            bg=self.cores["bg_entrada"],
            fg=self.cores["fg_entrada"],
            insertbackground=self.cores["cor_destaque"],  # Cursor roxo
            relief=tkinter.FLAT,  # Sem borda
            bd=0
        )
        
        entrada.grid(row=1, column=1, columnspan=2, padx=20, pady=10, sticky="nsew")
        

        return entrada
    

    def clarear_cor(self, cor):
        """Deixa a cor mais clara"""
        cores = {
            "green": "#90EE90",
            "orange": "#FFD700",
            "red": "#FF6B6B",
            "blue": "#87CEEB",
            "gray": "#D3D3D3",
            "purple": "#a482f5"
        }
        return cores.get(cor, cor)
    
    def criar_botoes_numeros(self):
        for numero, row, col in config.BOTOES_NUMEROS:
            btn = tkinter.Button(
                self.parent,
                text=numero,
                command=lambda n=numero: self.callbacks['numero'](n),
                font=(config.FONTE_BOTAO),
                width=8,
                height=3, 
                bg=self.cores["bg_botao"],  # ← Adiciona
                fg=self.cores["fg_botao"],
                activebackground=self.cores["cor_destaque"],  # Roxo ao clicar
                activeforeground="#ffffff",
                relief=tkinter.FLAT,
                bd=0,
                cursor="hand2"
            )
            # Cria variáveis pra armazenar a cor original
            cor_original = self.cores["bg_botao"]
            cor_hex = self.converter_cor_para_hex(cor_original)
            cor_hover = self.clarear_cor_dinamico(cor_hex)
            
            btn.grid(row=row, column=col, padx=0.5, pady=0.5, sticky="nsew")
            btn.bind("<Enter>", lambda e, b=btn, c=cor_hover: b.config(bg=c))
            btn.bind("<Leave>", lambda e, b=btn, c=cor_original: b.config(bg=c))
            
            
    def criar_botoes_operacoes(self):
        for operacao, row, col, cor in config.BOTOES_OPERACOES:
            btn = tkinter.Button(
                self.parent,
                text=operacao,
                command=lambda op=operacao: self.callbacks['operacao'](op),
                bg=self.cores["cor_destaque"],  # Roxo
                fg='white',
                font=config.FONTE_BOTAO,
                activebackground="#d946ef",  # Roxo mais claro ao hover
                activeforeground="white",
                width=5,
                height=2,
                relief=tkinter.FLAT,
                bd=0,
                cursor="hand2"
            )

            cor_original = self.cores["cor_destaque"]
            cor_hex = self.converter_cor_para_hex(cor_original)
            cor_hover = self.clarear_cor_dinamico(cor_hex)
            
            btn.grid(row=row, column=col, padx=0.5, pady=0.5, sticky="nsew")
            btn.bind("<Enter>", lambda e, b=btn, c=cor_hover: b.config(bg=c))
            btn.bind("<Leave>", lambda e, b=btn, c=cor_original: b.config(bg=c))

    def converter_cor_para_hex(self, cor):
        """Converte nome da cor para hex"""
        cores_nomes = {
            "red": "#FF0000",
            "green": "#00FF00",
            "blue": "#0000FF",
            "orange": "#FFA500",
            "yellow": "#FFFF00",
            "purple": "#800080",
            "white": "#FFFFFF",
            "black": "#000000",
            "gray": "#A9A9A9"
        }
        
        if cor.startswith("#"):
            return cor
    
        return cores_nomes.get(cor, cor)
            
    def clarear_cor_dinamico(self, cor_hex):
        """Deixa qualquer cor mais clara"""
        # Remove o '#'
        cor_hex = cor_hex.lstrip('#')

        # Converte hex para RGB
        r, g, b = tuple(int(cor_hex[i:i+2], 16) for i in (0, 2, 4))
        
        # Aumenta o brilho em 40%
        r = min(int(r * 0.6), 255)
        g = min(int(g * 0.6), 255)
        b = min(int(b * 0.6), 255)
        
        # Converte de volta para hex
        return f'#{r:02x}{g:02x}{b:02x}'
    
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
                bd=0, 
                relief=tkinter.FLAT # Estilo da borda
            )
            
            cor_original = cor
            cor_hex = self.converter_cor_para_hex(cor)
            cor_hover = self.clarear_cor_dinamico(cor_hex)
            
            btn.grid(row=row, column=col, padx=0.5, pady=0.5, sticky="nsew")
            btn.bind("<Enter>", lambda e, b=btn, c=cor_hover: b.config(bg=c))
            btn.bind("<Leave>", lambda e, b=btn, c=cor_original: b.config(bg=c))


        
    
    def criar_todos_botoes(self):
        self.criar_botoes_numeros()
        self.criar_botoes_operacoes()
        self.criar_botoes_especiais()