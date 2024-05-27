# Trabalho de Teoria da Computação

## Descrição do Trabalho
O trabalho consiste na implementação de um "tradutor" de modelos de máquinas de Turing. A entrada será um arquivo texto com extensão .in, contendo um programa de máquina de Turing conforme a sintaxe do simulador. A primeira linha do arquivo indicará o modelo utilizado:

    ;S para o modelo de Sipser (fita com início à esquerda)
    ;I para o modelo de fita duplamente infinita
A saída deve ser um arquivo texto com extensão .out, contendo um programa para o modelo oposto ao de entrada, pronto para ser executado no simulador. Esse programa de saída pode incluir movimentos estacionários.

#### Os arquivos de entrada terão o seguinte formato:

Primeira linha: comentário indicando o modelo
Linhas subsequentes: comandos no formato <current state> <current symbol> <new symbol> <direction> <new state>

## Restrições
- O estado inicial será sempre nomeado como 0.
- O alfabeto da fita incluirá apenas letras (maiúsculas e minúsculas) e dígitos.
- Símbolos auxiliares como #, &, %, £, ¢, § podem ser utilizados.
- Apenas máquinas de Turing determinísticas e com codificação válida para o simulador serão consideradas.
- Todos os programas de entrada reconhecerão linguagens sobre o alfabeto {0,1}.
O programa de saída deve reconhecer a mesma linguagem sobre o alfabeto {0,1}.


## Executar programa:
##### Trabalho desenvolvido em python 3.10.12

#### Instruções:

**1. Baixar repositório localmente**
```bash
    git clone trabalhoTec
```
**2. Entrar no repositório**
```bash
    cd trabalhoTec
```
**3. rodar o comando** 
```python 
    python trabsonTec.py
```

### Testes:

Para alterar os arquivos para testes, apenas altere o nome do arquivo na primeira linha do código

![img file name](./trabTec.png)