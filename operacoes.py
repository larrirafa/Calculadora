class Operacoes:
    @staticmethod
    def calcular(expressao):
        try:
            if "%" in expressao:
                return Operacoes.calcular_porcentagem(expressao)
            else:
                expressao = expressao.replace("x", "*")
                resultado = eval(expressao)
                return resultado
        except:
            return "Erro"
    
    @staticmethod
    def calcular_porcentagem(expressao):
        try:
            partes = expressao.split("%")
            resultado = (int(partes[0]) * int(partes[1])) / 100
            return resultado
        except:
            return "Erro"