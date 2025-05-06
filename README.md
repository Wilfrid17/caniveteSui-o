# 🛠️ Canivete Suíço Python

## 🔎 Descrição

O **Canivete Suíço Python** é uma ferramenta multifuncional de linha de comando que reúne diversas utilidades em um só lugar. Com recursos que vão desde a geração de senhas até criptografia de textos, monitoramento do sistema e muito mais, é uma solução prática e versátil para desenvolvedores, administradores de sistemas e entusiastas da tecnologia.

---

## 🚀 Funcionalidades

### 🔐 1. Geração de Senhas
- **Senha Aleatória**: Criação de senhas com tamanho personalizado.  
- **Senha com Caracteres Especiais**: Inclusão opcional de símbolos e caracteres especiais.

### 🔏 2. Criptografia de Texto
- **Criptografar**: Suporte para algoritmos Base64, MD5, SHA-256 e SHA-512.  
- **Descriptografar**: Decodificação de textos criptografados com Base64.

### 💻 3. Informações do Sistema
- Exibição de dados detalhados sobre o sistema operacional, arquitetura, processador, nome do host e endereço IP.

### 📊 4. Monitoramento de Recursos
- **Uso de CPU e Memória**: Monitora e exibe o consumo em tempo real.

### 🌐 5. Verificação de Conexão
- Testa a conectividade com sites populares e retorna o status da conexão com a internet.

### 📝 6. Manipulação de Texto
- **Contador de Palavras**: Conta palavras, caracteres e linhas.  
- **Conversor de Texto**: Alterna entre maiúsculas, minúsculas, formato de título ou texto invertido.

### ➗ 7. Calculadora
- Operações básicas: adição, subtração, multiplicação e divisão.

### 🔄 8. Conversor de Unidades
- Conversão entre unidades de **comprimento**, **peso** e **temperatura**.

### 📱 9. Gerador de QR Code
- Cria QR Codes a partir de textos ou URLs fornecidos.

---

## 🧰 Tecnologias Utilizadas

- **Python 3.x**
- Bibliotecas:
  - [`rich`](https://github.com/Textualize/rich): Formatação de saída no terminal  
  - [`pyperclip`](https://github.com/asweigart/pyperclip): Copiar texto para a área de transferência  
  - [`qrcode`](https://github.com/lincolnloop/python-qrcode) + `Pillow`: Geração de QR Codes  
  - [`psutil`](https://github.com/giampaolo/psutil): Monitoramento de sistema

---

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu_usuario/canivete-suico-python.git
cd canivete-suico-python
pip install rich pyperclip qrcode[pil] psutil

