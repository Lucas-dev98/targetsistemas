import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import json
import os

def is_fibonacci(n):
    """Verifica se um número pertence à sequência de Fibonacci."""
    if n < 0:
        return False
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

def questao1():
    """Calcula a soma dos números de 1 a 13."""
    INDICE = 13
    soma = sum(range(1, INDICE + 1))
    messagebox.showinfo("Resultado", f"A soma dos números de 1 a {INDICE} é: {soma}")

def questao2():
    """Solicita um número e verifica se pertence à sequência de Fibonacci."""
    try:
        numero = simpledialog.askinteger("Entrada", "Informe um número:")
        if numero is not None:  # Verifica se o usuário não cancelou
            resultado = "pertence" if is_fibonacci(numero) else "não pertence"
            messagebox.showinfo("Resultado", f"O número {numero} {resultado} à sequência de Fibonacci.")
        else:
            messagebox.showwarning("Aviso", "Nenhum número foi fornecido.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {str(e)}")

def processar_faturamento(arquivo_json):
    """Carrega e processa o arquivo JSON com os dados de faturamento."""
    try:
        with open(arquivo_json, 'r') as f:
            dados = json.load(f)

        # Filtra os valores de faturamento válidos (maiores que 0)
        faturamentos_validos = [dia for dia in dados if dia['valor'] > 0]

        if not faturamentos_validos:
            messagebox.showwarning("Aviso", "Nenhum faturamento válido encontrado.")
            return

        # Encontrar o dia com o menor e maior valor de faturamento
        menor_dia = min(faturamentos_validos, key=lambda x: x['valor'])
        maior_dia = max(faturamentos_validos, key=lambda x: x['valor'])

        # Média mensal
        media_mensal = sum(dia['valor'] for dia in faturamentos_validos) / len(faturamentos_validos)

        # Dias com faturamento superior à média
        dias_acima_da_media = sum(1 for dia in faturamentos_validos if dia['valor'] > media_mensal)

        # Exibir resultados
        resultado = (
            f"Menor valor de faturamento: {menor_dia['valor']:.2f} no dia {menor_dia['dia']}\n"
            f"Maior valor de faturamento: {maior_dia['valor']:.2f} no dia {maior_dia['dia']}\n"
            f"Dias com faturamento superior à média: {dias_acima_da_media}"
        )
        messagebox.showinfo("Resultados", resultado)

    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo não encontrado. Verifique o caminho e tente novamente.")
    except json.JSONDecodeError:
        messagebox.showerror("Erro", "Erro ao ler o arquivo JSON. Verifique se o formato está correto.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {str(e)}")

def selecionar_arquivo():
    """Abre uma caixa de diálogo para selecionar um arquivo JSON."""
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal do Tkinter
    arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo de faturamento",
        filetypes=[("JSON files", "*.json")],  # Limita a seleção a arquivos JSON
    )
    
    # Verifica se o arquivo foi selecionado
    if not arquivo:  # Se o usuário clicar em cancelar, arquivo será uma string vazia
        messagebox.showwarning("Aviso", "Nenhum arquivo foi selecionado.")
    
    return arquivo

def questao3():
    """Solicita um arquivo JSON e processa o faturamento diário."""
    arquivo_json = selecionar_arquivo()  # Abre a caixa de diálogo para seleção do arquivo
    
    if arquivo_json and os.path.isfile(arquivo_json):  # Verifica se o arquivo existe
        processar_faturamento(arquivo_json)
    elif arquivo_json:  # Se o arquivo não existir
        messagebox.showerror("Erro", "O arquivo selecionado não existe. Por favor, selecione um arquivo válido.")

def questao4():
    """Calcula o percentual de representação do faturamento por estado."""
    faturamento_estados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    # Calculando o faturamento total
    faturamento_total = sum(faturamento_estados.values())

    if faturamento_total == 0:
        messagebox.showwarning("Aviso", "Faturamento total é zero, não é possível calcular percentuais.")
        return

    # Calculando o percentual de cada estado e exibindo os resultados
    resultado = "Percentual de representação por estado no faturamento total:\n"
    for estado, faturamento in faturamento_estados.items():
        percentual = (faturamento / faturamento_total) * 100
        resultado += f"{estado}: {percentual:.2f}%\n"

    messagebox.showinfo("Resultados", resultado)

def inverter_string(texto):
    """Inverte uma string sem usar funções prontas."""
    return texto[::-1]  # Usando slicing para inverter a string

def questao5():
    """Solicita uma string e a inverte."""
    texto_original = simpledialog.askstring("Entrada", "Digite uma string para inverter:")
    if texto_original:
        texto_invertido = inverter_string(texto_original)
        messagebox.showinfo("Resultado", f"String invertida: {texto_invertido}")
    else:
        messagebox.showwarning("Aviso", "Nenhuma string foi fornecida.")

def mostrar_menu():
    """Mostra um menu para o usuário escolher uma questão."""
    while True:
        opcoes = [
            "1. Questão 1: Soma dos números de 1 a 13",
            "2. Questão 2: Verifica se um número pertence à sequência de Fibonacci",
            "3. Questão 3: Processar faturamento diário a partir de um arquivo JSON",
            "4. Questão 4: Percentual de faturamento por estado",
            "5. Questão 5: Inverter uma string",
            "0. Sair"
        ]
        escolha = simpledialog.askinteger("Menu", "\n".join(opcoes) + "\nEscolha uma opção:")
        
        if escolha == 1:
            questao1()
        elif escolha == 2:
            questao2()
        elif escolha == 3:
            questao3()
        elif escolha == 4:
            questao4()
        elif escolha == 5:
            questao5()
        elif escolha == 0:
            break
        else:
            messagebox.showwarning("Aviso", "Opção inválida. Por favor, escolha uma opção válida.")
