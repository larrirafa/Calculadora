# 🧮 Calculadora

Uma calculadora moderna e elegante com interface escura, histórico de cálculos e exportação de dados.

## ✨ Características

- **Interface Dark/Light Mode**: Alterne entre tema escuro elegante e tema claro
- **Histórico de Cálculos**: Visualize todos os cálculos realizados
- **Animação Suave**: O histórico desliza da esquerda para a direita
- **Exportação de Dados**: Exporte seu histórico em CSV, TXT ou PDF
- **Atalhos de Teclado**: 
  - `Enter` para calcular
  - `Delete` para limpar
  - Números do teclado funcionam normalmente
- **Design Responsivo**: Interface que se adapta a diferentes tamanhos de janela
- **Banco de Dados SQLite**: Histórico salvo localmente

## 🚀 Como Usar

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/larrirafa/Calculadora.git
cd Calculadora
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o programa:
```bash
python main.py
```

### Uso Básico

#### Operações Matemáticas
- Digite números clicando nos botões ou usando o teclado numérico
- Clique nos botões de operação (+, -, x, /) ou digite-os no teclado
- Pressione `=` ou `Enter` para calcular o resultado
- O resultado é salvo automaticamente no histórico

#### Funções Especiais
- **C (Clear)**: Limpa a tela (também pressione `Delete`)
- **%**: Calcula porcentagem (exemplo: 15 % 5 = 7.5)
- **back**: Apaga o último dígito digitado

#### Histórico
- Clique no botão **Histórico** para abrir o painel
- Veja todos os seus cálculos anteriores com data e hora
- Clique **Exportar** para baixar o histórico em:
  - CSV (para planilhas)
  - TXT (arquivo de texto)
  - PDF (documento formatado)
- Clique **Limpar** para deletar todo o histórico
- Clique **Fechar** para esconder o painel

#### Tema
- Clique no botão **🌙** (lua) no canto superior direito para alternar entre modo escuro e claro

## 🎨 Design

A calculadora foi desenvolvida com um design moderno e elegante:
- **Modo Escuro**: Fundo preto azulado (#0f0f1e) com acentos roxo/rosa (#c084fc)
- **Modo Claro**: Fundo branco com tons suaves e roxo destacado (#8b5cf6)
- **Fonte**: Segoe UI para uma aparência profissional
- **Hover Effects**: Botões mudam de cor ao passar o mouse

## 📂 Estrutura do Projeto

```
Calculadora/
├── main.py              # Arquivo principal
├── calculadora.py       # Classe principal da aplicação
├── interface.py         # Gerenciamento da interface gráfica
├── config.py            # Configurações e temas
├── operacoes.py         # Funções matemáticas
├── banco_dados.py       # Gerenciamento do banco de dados
├── exportar.py          # Exportação de dados
├── requirements.txt     # Dependências
├── README.md            # Este arquivo
└── .gitignore           # Arquivos a ignorar no Git
```

## 🔧 Tecnologias Utilizadas

- **Python 3.8+**
- **Tkinter**: Interface gráfica
- **SQLite3**: Banco de dados local
- **ReportLab**: Exportação para PDF
- **CSV**: Exportação de dados

## ⌨️ Atalhos de Teclado

| Atalho | Função |
|--------|--------|
| `0-9` | Digita números |
| `+` | Adição |
| `-` | Subtração |
| `*` | Multiplicação |
| `/` | Divisão |
| `Enter` | Calcula resultado |
| `Delete` | Limpa a tela |

## 📊 Exemplos de Uso

### Cálculo Simples
1. Digite: `5`
2. Clique: `+`
3. Digite: `3`
4. Pressione: `Enter`
5. Resultado: `8`

### Cálculo com Porcentagem
1. Digite: `15`
2. Clique: `%`
3. Digite: `20`
4. Pressione: `Enter`
5. Resultado: `3` (20% de 15)

### Exportar Histórico
1. Clique em **Histórico**
2. Clique em **Exportar**
3. Escolha o formato (CSV, TXT ou PDF)
4. Selecione onde salvar
5. Arquivo baixado com sucesso!

## 🗄️ Banco de Dados

O histórico é armazenado em um banco de dados SQLite local (`calculadora.db`). Cada cálculo contém:
- ID único
- Expressão (ex: "5 + 3")
- Resultado (ex: "8")
- Data e hora do cálculo

## 📦 Dependências

```
tkinter (incluído com Python)
sqlite3 (incluído com Python)
reportlab (para exportação PDF)
```

Para instalar reportlab:
```bash
pip install reportlab
```

## 🎯 Funcionalidades Futuras

- [ ] Funções trigonométricas
- [ ] Histórico sincronizado na nuvem
- [ ] Temas adicionais
- [ ] Suporte a múltiplos idiomas
- [ ] Calculadora científica

## 📝 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## 👨‍💻 Autor

Desenvolvido por **Larri** como um projeto educacional de Python.

## 💬 Contribuições

Contribuições são bem-vindas! Sinta-se livre para:
- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar a documentação
- Enviar pull requests

## 📞 Suporte

Se tiver dúvidas ou problemas, abra uma issue no repositório.

---

**Aproveite sua calculadora! 🧮✨**