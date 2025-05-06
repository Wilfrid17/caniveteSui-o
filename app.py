import random
import string
import time
import os
import hashlib
import base64
import webbrowser
import socket
import platform
import psutil
from datetime import datetime

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.align import Align

console = Console()

def clear_screen():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    """Exibe o menu principal da aplicação"""
    clear_screen()
    console.print(Panel.fit(
        "[bold yellow]CANIVETE SUÍÇO PYTHON[/bold yellow]", 
        border_style="green",
        padding=(1, 30)
    ))
    
    table = Table(title="Menu Principal", title_justify="center")
    table.add_column("Opção", justify="center", style="cyan")
    table.add_column("Descrição", style="magenta")
    
    # Ferramentas de Segurança
    table.add_row("1", "Gerar Senha")
    table.add_row("2", "Gerar Senha com Caracteres Especiais")
    table.add_row("3", "Criptografar Texto")
    table.add_row("4", "Descriptografar Texto")
    
    # Ferramentas de Sistema
    table.add_row("5", "Informações do Sistema")
    table.add_row("6", "Uso de CPU e Memória")
    table.add_row("7", "Verificar Conexão de Internet")
    
    # Ferramentas de Texto
    table.add_row("8", "Contador de Palavras")
    table.add_row("9", "Conversor de Maiúsculas/Minúsculas")
    
    # Ferramentas de Utilidades
    table.add_row("10", "Calculadora Simples")
    table.add_row("11", "Conversor de Unidades")
    table.add_row("12", "Gerador de QR Code")
    
    # Saída
    table.add_row("0", "[bold red]Sair[/bold red]")
    
    console.print(table)

def gerar_senha(tamanho=12, com_especiais=False):
    """Gera uma senha aleatória"""
    # Define os caracteres que podem ser usados
    caracteres = string.ascii_letters + string.digits
    if com_especiais:
        caracteres += string.punctuation
    
    # Gera a senha
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def menu_gerar_senha(com_especiais=False):
    """Menu para geração de senha"""
    clear_screen()
    
    titulo = "Gerar Senha" if not com_especiais else "Gerar Senha com Caracteres Especiais"
    console.print(Panel(f"[bold cyan]{titulo}[/bold cyan]", border_style="blue"))
    
    tamanho = IntPrompt.ask("Digite o tamanho da senha", default=12)
    
    # Animação de processamento
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold green]Gerando senha segura...[/bold green]"),
        transient=True,
    ) as progress:
        task = progress.add_task("", total=100)
        for _ in range(10):
            progress.update(task, advance=10)
            time.sleep(0.1)
    
    # Gera a senha
    senha = gerar_senha(tamanho, com_especiais)
    
    # Exibe a senha
    console.print("\n[bold green]Senha gerada com sucesso![/bold green]")
    console.print(Panel(f"[bold white]{senha}[/bold white]", border_style="green", title="Sua senha"))
    
    # Pergunta se deseja copiar a senha
    if Confirm.ask("Deseja copiar a senha para a área de transferência?"):
        try:
            import pyperclip
            pyperclip.copy(senha)
            console.print("[green]Senha copiada para a área de transferência![/green]")
        except ImportError:
            console.print("[yellow]Módulo pyperclip não encontrado. Não foi possível copiar.[/yellow]")
    
    # Aguarda antes de retornar ao menu
    voltar_menu()

def criptografar_texto():
    """Criptografa um texto usando diversos métodos"""
    clear_screen()
    console.print(Panel("[bold cyan]Criptografar Texto[/bold cyan]", border_style="blue"))
    
    # Pergunta o método de criptografia
    table = Table(title="Métodos de Criptografia")
    table.add_column("Opção", justify="center", style="cyan")
    table.add_column("Método", style="magenta")
    table.add_row("1", "Base64")
    table.add_row("2", "MD5")
    table.add_row("3", "SHA-256")
    table.add_row("4", "SHA-512")
    console.print(table)
    
    metodo = Prompt.ask("Escolha o método", choices=["1", "2", "3", "4"])
    
    # Pergunta o texto a ser criptografado
    texto = Prompt.ask("Digite o texto a ser criptografado")
    
    # Criptografa o texto
    resultado = ""
    if metodo == "1":
        resultado = base64.b64encode(texto.encode()).decode()
        metodo_nome = "Base64"
    elif metodo == "2":
        resultado = hashlib.md5(texto.encode()).hexdigest()
        metodo_nome = "MD5"
    elif metodo == "3":
        resultado = hashlib.sha256(texto.encode()).hexdigest()
        metodo_nome = "SHA-256"
    elif metodo == "4":
        resultado = hashlib.sha512(texto.encode()).hexdigest()
        metodo_nome = "SHA-512"
    
    # Exibe o resultado
    console.print(f"\n[bold green]Texto criptografado com {metodo_nome}![/bold green]")
    console.print(Panel(f"[bold white]{resultado}[/bold white]", border_style="green", title="Resultado"))
    
    # Aguarda antes de retornar ao menu
    voltar_menu()

def descriptografar_texto():
    """Descriptografa um texto (apenas Base64)"""
    clear_screen()
    console.print(Panel("[bold cyan]Descriptografar Texto[/bold cyan]", border_style="blue"))
    
    # Avisa sobre limitações
    console.print("[yellow]Nota: Apenas texto em Base64 pode ser descriptografado. Hashes como MD5 e SHA não são reversíveis.[/yellow]\n")
    
    # Pergunta o texto a ser descriptografado
    texto = Prompt.ask("Digite o texto em Base64 a ser descriptografado")
    
    try:
        # Tenta descriptografar
        resultado = base64.b64decode(texto.encode()).decode()
        
        # Exibe o resultado
        console.print("\n[bold green]Texto descriptografado![/bold green]")
        console.print(Panel(f"[bold white]{resultado}[/bold white]", border_style="green", title="Resultado"))
    except Exception as e:
        console.print(f"[bold red]Erro ao descriptografar: {e}[/bold red]")
    
    # Aguarda antes de retornar ao menu
    voltar_menu()

def informacoes_sistema():
    """Exibe informações sobre o sistema"""
    clear_screen()
    console.print(Panel("[bold cyan]Informações do Sistema[/bold cyan]", border_style="blue"))
    
    # Coleta informações
    info = {
        "Sistema Operacional": platform.system(),
        "Versão": platform.version(),
        "Arquitetura": platform.architecture()[0],
        "Processador": platform.processor(),
        "Hostname": socket.gethostname(),
        "Endereço IP": socket.gethostbyname(socket.gethostname()),
        "Data e Hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "Python Versão": platform.python_version()
    }
    
    # Cria uma tabela
    table = Table(title="Informações do Sistema")
    table.add_column("Item", style="cyan")
    table.add_column("Valor", style="magenta")
    
    # Adiciona as informações à tabela
    for item, valor in info.items():
        table.add_row(item, str(valor))
    
    console.print(table)
    
    # Aguarda antes de retornar ao menu
    voltar_menu()

def uso_cpu_memoria():
    """Monitora o uso de CPU e memória"""
    clear_screen()
    console.print(Panel("[bold cyan]Uso de CPU e Memória[/bold cyan]", border_style="blue"))
    
    console.print("[yellow]Monitorando por 10 segundos. Pressione Ctrl+C para cancelar.[/yellow]\n")
    
    try:
        for i in range(10):
            # Coleta informações
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            
            # Limpa a tela
            clear_screen()
            console.print(Panel("[bold cyan]Uso de CPU e Memória[/bold cyan]", border_style="blue"))
            
            # Exibe informações
            console.print(f"[bold]CPU:[/bold] {cpu_percent}%")
            console.print(f"[bold]Memória:[/bold] {memory.percent}% (Usada: {memory.used / (1024**3):.2f} GB, Total: {memory.total / (1024**3):.2f} GB)")
            
            # Barras de progresso
            console.print(f"CPU: [{'#' * int(cpu_percent / 5)}{' ' * (20 - int(cpu_percent / 5))}] {cpu_percent}%")
            console.print(f"RAM: [{'#' * int(memory.percent / 5)}{' ' * (20 - int(memory.percent / 5))}] {memory.percent}%")
            
            console.print(f"\n[italic]Atualizando... ({i+1}/10)[/italic]")
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    
    # Aguarda antes de retornar ao menu
    voltar_menu()

def verificar_conexao():
    """Verifica a conexão de internet"""
    clear_screen()
    console.print(Panel("[bold cyan]Verificar Conexão de Internet[/bold cyan]", border_style="blue"))
    
    hosts = ["www.google.com", "www.github.com", "www.youtube.com"]
    
    # Testa a conexão
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold green]Verificando conexão...[/bold green]"),
        transient=True,
    ) as progress:
        task = progress.add_task("", total=len(hosts))
        resultados = {}
        
        for host in hosts:
            try:
                # Tenta resolver o DNS
                ip = socket.gethostbyname(host)
                resultados[host] = {"status": "Online", "ip": ip}
            except Exception:
                resultados[host] = {"status": "Offline", "ip": "N/A"}
            
            progress.update(task, advance=1)
            time.sleep(0.5)
    
    # Exibe os resultados
    table = Table(title="Resultado da Verificação")
    table.add_column("Host", style="cyan")
    table.add_column("Status", style="magenta")
    table.add_column("IP", style="yellow")
    
    for host, info in resultados.items():
        status_color = "green" if info["status"] == "Online" else "red"
        table.add_row(host, f"[{status_color}]{info['status']}[/{status_color}]", info["ip"])
    
    console.print(table)
    
    # Verifica se todos estão online
    todos_online = all(info["status"] == "Online" for info in resultados.values())
    if todos_online:
        console.print("\n[bold green]Sua conexão com a internet parece estar funcionando bem![/bold green]")
    else:
        console.print("\n[bold yellow]Sua conexão com a internet pode estar instável ou com problemas.[/bold yellow]")
    
    # Aguarda antes de retornar ao menu
    voltar_menu()

def contador_palavras():
    """Conta palavras, caracteres e linhas em um texto"""
    clear_screen()
    console.print(Panel("[bold cyan]Contador de Palavras[/bold cyan]", border_style="blue"))
    
    console.print("[yellow]Digite ou cole o texto abaixo. Pressione Enter e depois Ctrl+D (Unix) ou Ctrl+Z+Enter (Windows) para finalizar.[/yellow]\n")
    
    linhas = []
    try:
        while True:
            linha = input()
            linhas.append(linha)
    except (EOFError, KeyboardInterrupt):
        pass
    
    texto = "\n".join(linhas)
    
    # Realiza a contagem
    num_caracteres = len(texto)
    num_caracteres_sem_espacos = len(texto.replace(" ", ""))
    num_palavras = len(texto.split())
    num_linhas = len(linhas)
    
    # Exibe os resultados
    table = Table(title="Resultado da Contagem")
    table.add_column("Item", style="cyan")
    table.add_column("Quantidade", style="magenta")
    
    table.add_row("Caracteres (com espaços)", str(num_caracteres))
    table.add_row("Caracteres (sem espaços)", str(num_caracteres_sem_espacos))
    table.add_row("Palavras", str(num_palavras))
    table.add_row("Linhas", str(num_linhas))
    
    console.print(table)
    
    # Aguarda antes de retornar ao menu
    voltar_menu()

def conversor_texto():
    """Converte texto para maiúsculas, minúsculas ou título"""
    clear_screen()
    console.print(Panel("[bold cyan]Conversor de Maiúsculas/Minúsculas[/bold cyan]", border_style="blue"))
    
    # Pergunta o texto
    texto = Prompt.ask("Digite o texto a ser convertido")
    
    # Pergunta o tipo de conversão
    table = Table(title="Tipos de Conversão")
    table.add_column("Opção", justify="center", style="cyan")
    table.add_column("Tipo", style="magenta")
    table.add_row("1", "MAIÚSCULAS")
    table.add_row("2", "minúsculas")
    table.add_row("3", "Título")
    table.add_row("4", "iNVERTER")
    console.print(table)
    
    tipo = Prompt.ask("Escolha o tipo de conversão", choices=["1", "2", "3", "4"])
    
    # Converte o texto
    if tipo == "1":
        resultado = texto.upper()
        tipo_nome = "MAIÚSCULAS"
    elif tipo == "2":
        resultado = texto.lower()
        tipo_nome = "minúsculas"
    elif tipo == "3":
        resultado = texto.title()
        tipo_nome = "Título"
    elif tipo == "4":
        resultado = texto.swapcase()
        tipo_nome = "Invertido"
    
    # Exibe o resultado
    console.print(f"\n[bold green]Texto convertido para {tipo_nome}![/bold green]")
    console.print(Panel(f"[bold white]{resultado}[/bold white]", border_style="green", title="Resultado"))
    
    # Aguarda antes de retornar ao menu
    voltar_menu()

def calculadora_simples():
    """Calculadora simples com operações básicas"""
    clear_screen()
    console.print(Panel("[bold cyan]Calculadora Simples[/bold cyan]", border_style="blue"))
    
    # Pergunta o primeiro número
    num1 = float(Prompt.ask("Digite o primeiro número"))
    
    # Pergunta a operação
    table = Table(title="Operações")
    table.add_column("Opção", justify="center", style="cyan")
    table.add_column("Operação", style="magenta")
    table.add_row("+", "Adição")
    table.add_row("-", "Subtração")
    table.add_row("*", "Multiplicação")
    table.add_row("/", "Divisão")
    table.add_row("^", "Potência")
    table.add_row("%", "Módulo (resto da divisão)")
    console.print(table)
    
    operacao = Prompt.ask("Escolha a operação", choices=["+", "-", "*", "/", "^", "%"])
    
    # Pergunta o segundo número
    num2 = float(Prompt.ask("Digite o segundo número"))
    
    # Realiza a operação
    try:
        if operacao == "+":
            resultado = num1 + num2
            operacao_nome = "Adição"
        elif operacao == "-":
            resultado = num1 - num2
            operacao_nome = "Subtração"
        elif operacao == "*":
            resultado = num1 * num2
            operacao_nome = "Multiplicação"
        elif operacao == "/":
            if num2 == 0:
                raise ZeroDivisionError("Divisão por zero")
            resultado = num1 / num2
            operacao_nome = "Divisão"
        elif operacao == "^":
            resultado = num1 ** num2
            operacao_nome = "Potência"
        elif operacao == "%":
            if num2 == 0:
                raise ZeroDivisionError("Módulo por zero")
            resultado = num1 % num2
            operacao_nome = "Módulo"
        
        # Exibe o resultado
        console.print(f"\n[bold green]Resultado da {operacao_nome}:[/bold green]")
        console.print(Panel(f"[bold white]{num1} {operacao} {num2} = {resultado}[/bold white]", border_style="green", title="Resultado"))
    except Exception as e:
        console.print(f"[bold red]Erro: {e}[/bold red]")
    
    # Aguarda antes de retornar ao menu
    voltar_menu()

def conversor_unidades():
    """Conversor de unidades"""
    clear_screen()
    console.print(Panel("[bold cyan]Conversor de Unidades[/bold cyan]", border_style="blue"))
    
    # Pergunta o tipo de conversão
    table = Table(title="Tipos de Conversão")
    table.add_column("Opção", justify="center", style="cyan")
    table.add_column("Tipo", style="magenta")
    table.add_row("1", "Comprimento")
    table.add_row("2", "Peso/Massa")
    table.add_row("3", "Temperatura")
    console.print(table)
    
    tipo = Prompt.ask("Escolha o tipo de conversão", choices=["1", "2", "3"])
    
    # Configura as unidades com base no tipo
    if tipo == "1":  # Comprimento
        unidades = {
            "1": {"nome": "Metros", "para": {"1": 1, "2": 100, "3": 1000, "4": 0.001, "5": 0.000001}},
            "2": {"nome": "Centímetros", "para": {"1": 0.01, "2": 1, "3": 10, "4": 0.00001, "5": 0.00000001}},
            "3": {"nome": "Milímetros", "para": {"1": 0.001, "2": 0.1, "3": 1, "4": 0.000001, "5": 0.000000001}},
            "4": {"nome": "Quilômetros", "para": {"1": 1000, "2": 100000, "3": 1000000, "4": 1, "5": 0.001}},
            "5": {"nome": "Megametros", "para": {"1": 1000000, "2": 100000000, "3": 1000000000, "4": 1000, "5": 1}}
        }
    elif tipo == "2":  # Peso/Massa
        unidades = {
            "1": {"nome": "Quilogramas", "para": {"1": 1, "2": 1000, "3": 1000000, "4": 0.001, "5": 2.20462}},
            "2": {"nome": "Gramas", "para": {"1": 0.001, "2": 1, "3": 1000, "4": 0.000001, "5": 0.00220462}},
            "3": {"nome": "Miligramas", "para": {"1": 0.000001, "2": 0.001, "3": 1, "4": 0.000000001, "5": 0.00000220462}},
            "4": {"nome": "Toneladas", "para": {"1": 1000, "2": 1000000, "3": 1000000000, "4": 1, "5": 2204.62}},
            "5": {"nome": "Libras", "para": {"1": 0.453592, "2": 453.592, "3": 453592, "4": 0.000453592, "5": 1}}
        }
    elif tipo == "3":  # Temperatura
        unidades = {
            "1": {"nome": "Celsius", "para": {"1": lambda x: x, "2": lambda x: x * 9/5 + 32, "3": lambda x: x + 273.15}},
            "2": {"nome": "Fahrenheit", "para": {"1": lambda x: (x - 32) * 5/9, "2": lambda x: x, "3": lambda x: (x - 32) * 5/9 + 273.15}},
            "3": {"nome": "Kelvin", "para": {"1": lambda x: x - 273.15, "2": lambda x: (x - 273.15) * 9/5 + 32, "3": lambda x: x}}
        }
    
    # Exibe as unidades disponíveis
    table = Table(title="Unidades Disponíveis")
    table.add_column("Opção", justify="center", style="cyan")
    table.add_column("Unidade", style="magenta")
    
    for key, unit in unidades.items():
        table.add_row(key, unit["nome"])
    
    console.print(table)
    
    # Pergunta a unidade de origem
    de = Prompt.ask("Converter de", choices=list(unidades.keys()))
    
    # Pergunta a unidade de destino
    para = Prompt.ask("Converter para", choices=list(unidades.keys()))
    
    # Pergunta o valor
    valor = float(Prompt.ask("Digite o valor a ser convertido"))
    
    # Realiza a conversão
    try:
        if tipo == "3":  # Temperatura (caso especial)
            resultado = unidades[de]["para"][para](valor)
        else:  # Outros tipos
            resultado = valor * unidades[de]["para"][para]
        
        # Exibe o resultado
        console.print(f"\n[bold green]Resultado da Conversão:[/bold green]")
        console.print(Panel(
            f"[bold white]{valor} {unidades[de]['nome']} = {resultado} {unidades[para]['nome']}[/bold white]", 
            border_style="green", 
            title="Resultado"
        ))
    except Exception as e:
        console.print(f"[bold red]Erro: {e}[/bold red]")
    
    # Aguarda antes de retornar ao menu
    voltar_menu()

def gerador_qrcode():
    """Gera um QR Code para um texto ou URL"""
    clear_screen()
    console.print(Panel("[bold cyan]Gerador de QR Code[/bold cyan]", border_style="blue"))
    
    try:
        import qrcode
        from PIL import Image
        
        # Pergunta o texto ou URL
        texto = Prompt.ask("Digite o texto ou URL para o QR Code")
        
        # Pergunta o nome do arquivo
        nome_arquivo = Prompt.ask("Digite o nome do arquivo (sem extensão)", default="qrcode")
        nome_arquivo = f"{nome_arquivo}.png"
        
        # Gera o QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(texto)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(nome_arquivo)
        
        # Exibe o resultado
        console.print(f"\n[bold green]QR Code gerado com sucesso![/bold green]")
        console.print(f"Arquivo salvo como: [cyan]{nome_arquivo}[/cyan]")
        
        # Pergunta se deseja abrir o arquivo
        if Confirm.ask("Deseja abrir o arquivo?"):
            webbrowser.open(nome_arquivo)
    
    except ImportError:
        console.print("[bold red]Erro: Módulos qrcode e/ou PIL não encontrados.[/bold red]")
        console.print("[yellow]Instale-os com: pip install qrcode pillow[/yellow]")
    
    except Exception as e:
        console.print(f"[bold red]Erro: {e}[/bold red]")
    
    # Aguarda antes de retornar ao menu
    voltar_menu()

def voltar_menu():
    """Função para voltar ao menu principal"""
    console.print("\n[italic]Pressione Enter para voltar ao menu principal...[/italic]")
    input()

def main():
    """Função principal do programa"""
    while True:
        menu_principal()
        escolha = Prompt.ask("Escolha uma opção", choices=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "0"])
        
        if escolha == "1":
            menu_gerar_senha(com_especiais=False)
        elif escolha == "2":
            menu_gerar_senha(com_especiais=True)
        elif escolha == "3":
            criptografar_texto()
        elif escolha == "4":
            descriptografar_texto()
        elif escolha == "5":
            informacoes_sistema()
        elif escolha == "6":
            uso_cpu_memoria()
        elif escolha == "7":
            verificar_conexao()
        elif escolha == "8":
            contador_palavras()
        elif escolha == "9":
            conversor_texto()
        elif escolha == "10":
            calculadora_simples()
        elif escolha == "11":
            conversor_unidades()
        elif escolha == "12":
            gerador_qrcode()
        elif escolha == "0":
            clear_screen()
            console.print(Panel("[bold yellow]Obrigado por usar o Canivete Suíço Python![/bold yellow]", border_style="green"))
            time.sleep(1.5)
            clear_screen()
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        console.print("[bold yellow]Programa encerrado pelo usuário.[/bold yellow]")