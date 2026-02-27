import tkinter
import config
from interface import Interface
from operacoes import Operacoes
from banco_dados import BancoDados

class Calculadora(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title(config.TITULO)
        self.geometry(f'{config.LARGURA}x{config.ALTURA}+{config.POS_X}+{config.POS_Y}')
        
        self.banco = BancoDados()
        self.protocol("WM_DELETE_WINDOW", self.funcao_ao_fechar)

        # Configurar grid para expandir
        for i in range(7):
            self.grid_rowconfigure(i, weight=1)
        for i in range(7):
            self.grid_columnconfigure(i, weight=1)

        self.referenciado_entry = tkinter.StringVar()
        
        # Criar interface
        self.interface = Interface(self, {
            'numero': self.clicar_numero,
            'operacao': self.clicar_operacao,
            'especial': self.caracteres_especiais
        })
        
        self.entrada = self.interface.criar_entrada()
        self.entrada.config(textvariable=self.referenciado_entry)
        self.interface.criar_todos_botoes()
        
        # Botão de histórico
        botao_historico = tkinter.Button(
            self,
            text="Histórico",
            command=self.mostrar_esconder_historico,
            font=("Arial", 12, "bold"),
            bg="lightblue"
        )
        botao_historico.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
    
    def funcao_ao_fechar(self):
        self.banco.fechar()
        self.destroy()

    def mostrar_historico(self):
        # Limpa a listbox antes de preencher
        self.listbox.delete(0, tkinter.END)
        
        dados = self.banco.obter_historico()

        for i in dados:
            string = f"{i[1]} = {i[2]} ({i[3]})"
            self.listbox.insert(tkinter.END, string)
    
    def clicar_numero(self, numero):
        atual = self.referenciado_entry.get()
        self.referenciado_entry.set(atual + str(numero))
        self.entrada.focus()
        self.entrada.icursor("end")
    
    def clicar_operacao(self, operacao):
        atual = self.referenciado_entry.get()
        
        if operacao == "=":
            resultado = Operacoes.calcular(atual)
            self.referenciado_entry.set(resultado)
            
            # Remove o "=" para salvar a expressão correta
            expressao = atual[:-1]
            self.banco.adicionar_calculo(expressao=expressao, resultado=resultado)
        else:
            self.referenciado_entry.set(atual + str(operacao))

        self.entrada.focus()
        self.entrada.icursor("end")
    
    def caracteres_especiais(self, especial):
        if especial == "%":
            atual = self.referenciado_entry.get()
            self.referenciado_entry.set(atual + "%")
        
        elif especial == "C":
            self.referenciado_entry.set("")
        
        elif especial == "back":
            atual = self.referenciado_entry.get()
            self.referenciado_entry.set(atual[:-1])
        
        self.entrada.focus()
        self.entrada.icursor("end")

    def mostrar_esconder_historico(self):
        # Se o frame NÃO foi criado ainda
        if not hasattr(self, 'frame_historico'):
            # Cria o frame
            self.frame_historico = tkinter.Frame(self, bg="lightgray", width=200)
            
            
            # Cria a listbox dentro do frame
            self.listbox = tkinter.Listbox(self.frame_historico, font=("Arial", 10))
            self.listbox.pack(fill=tkinter.BOTH, expand=True, padx=5, pady=5)
            
            # Botão para limpar histórico
            botao_limpar = tkinter.Button(
                self.frame_historico,
                text="Limpar",
                command=self.limpar_historico,
                bg="red",
                fg="white"
            )
            botao_limpar.pack(fill=tkinter.X, padx=5, pady=5)
            
            botao_fechar = tkinter.Button(
                self.frame_historico,
                text="Fechar",
                command=self.animar_reverso,
                bg="orange",
                fg="white"
                )
            botao_fechar.pack(fill=tkinter.X, padx=5, pady=5)
            
            # Preenche com dados iniciais
            self.mostrar_historico()
            self.animar()
            
        else:
            # Se já existe, toggle (mostra/esconde)
            if self.frame_historico.winfo_viewable():
                self.animar_reverso()
            else:
                self.frame_historico.place(x=0, y=50, width=250, height=450)
                self.mostrar_historico()
                self.animar()
    
    def limpar_historico(self):
        self.banco.limpar_historico()
        self.mostrar_historico()

    def animar(self):
        # Move o frame um pouco
        posicao_atual = 0
        posicao_final = 60
        
        def mover():
            nonlocal posicao_atual
            
            if posicao_atual < posicao_final:
                posicao_atual += 5
                self.frame_historico.place(x=posicao_atual, y=50, width=250, height=450)
                self.after(20, mover)
        mover()
                
    def animar_reverso(self):
        posicao_atual = 60
        posicao_final = 0
        
        def mover():
            nonlocal posicao_atual
            
            if posicao_atual > posicao_final:
                posicao_atual -= 5
                self.frame_historico.place(x=posicao_atual, y=50, width=250, height=450)
                self.after(20, mover)
            else:
                self.frame_historico.place_forget()
            
        mover()
        
    

