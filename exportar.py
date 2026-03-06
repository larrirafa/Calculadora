import csv
from datetime import datetime

class Exportador:
    def __init__(self, banco):
        self.banco = banco
    
    def exportar_csv(self, caminho):
        """Exporta histórico para CSV"""
        dados = self.banco.obter_historico()
        
        with open(caminho, 'w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(['ID', 'Expressão', 'Resultado', 'Data/Hora'])
            
            for linha in dados:
                writer.writerow(linha)
        
        return True
    
    def exportar_txt(self, caminho):
        """Exporta histórico para TXT"""
        dados = self.banco.obter_historico()
        
        with open(caminho, 'w', encoding='utf-8') as arquivo:
            arquivo.write("HISTÓRICO DA CALCULADORA\n")
            arquivo.write("=" * 50 + "\n\n")
            
            for id, expressao, resultado, data_hora in dados:
                arquivo.write(f"{expressao} = {resultado} ({data_hora})\n")
        
        return True
    
    def exportar_pdf(self, caminho):
        """Exporta histórico para PDF"""
        try:
            from reportlab.lib.pagesizes import letter
            from reportlab.lib import colors
            from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
            from reportlab.lib.styles import getSampleStyleSheet
            
            dados = self.banco.obter_historico()
            
            # Cria o PDF
            doc = SimpleDocTemplate(caminho, pagesize=letter)
            elements = []
            
            # Título
            styles = getSampleStyleSheet()
            titulo = Paragraph("Histórico da Calculadora", styles['Title'])
            elements.append(titulo)
            
            # Tabela
            tabela_dados = [['Expressão', 'Resultado', 'Data/Hora']]
            for id, expressao, resultado, data_hora in dados:
                tabela_dados.append([expressao, resultado, data_hora])
            
            tabela = Table(tabela_dados)
            tabela.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 14),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            
            elements.append(tabela)
            doc.build(elements)
            return True
        except ImportError:
            return False