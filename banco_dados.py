import sqlite3
from datetime import datetime

class BancoDados:
    def __init__(self, nome_db="calculadora.db"):
        self.conexao = sqlite3.connect(nome_db)
        self.cursor = self.conexao.cursor()
        self.criar_tabela()
    
    

    def criar_tabela(self):
        """Cria a tabela de histórico se não existir"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS historico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                expressao TEXT NOT NULL,
                resultado TEXT NOT NULL,
                data_hora TEXT NOT NULL
            )
        ''')
        self.conexao.commit()
    
    def adicionar_calculo(self, expressao, resultado):
        """Adiciona um novo cálculo ao banco"""
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.cursor.execute('''
            INSERT INTO historico (expressao, resultado, data_hora)
            VALUES (?, ?, ?)
        ''', (expressao, resultado, data_hora))
        self.conexao.commit()
    
    def obter_historico(self):
        """Retorna todos os cálculos"""
        self.cursor.execute('SELECT * FROM historico ORDER BY id DESC')
        return self.cursor.fetchall()
    
    def limpar_historico(self):
        """Limpa todos os cálculos"""
        self.cursor.execute('DELETE FROM historico')
        self.conexao.commit()
    
    def fechar(self):
        """Fecha a conexão"""
        self.conexao.close()