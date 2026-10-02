# Tutorial — Aprendendo NOVA

## 1. Seu primeiro programa

Crie um arquivo `ola.nova`:

```nova
print("Olá, mundo!")
```

## 2. Variáveis

Não precisa declarar tipo:

```nova
nome = "Ana"
idade = 25
altura = 1.68
ativo = True
```

## 3. Tipos de dados

```nova
# Lista (mutável)
frutas = ["maçã", "banana", "uva"]
frutas.append("laranja")

# Dicionário
pessoa = {"nome": "Ana", "idade": 25}
print(pessoa["nome"])

# Tupla (imutável)
ponto = (10, 20)

# Conjunto (sem duplicados)
tags = {"jogo", "web", "jogo"}

# Compreensão de lista
quadrados = [n * n for n in range(5)]
```

## 4. Condicionais

```nova
nota = 8

if nota >= 9:
    print("A+")
elif nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")
```

## 5. Laços

```nova
for i in range(5):
    print(i)

while idade < 30:
    idade = idade + 1
```

## 6. Funções

```nova
func saudacao(nome = "visitante"):
    return "Olá, " + nome + "!"

print(saudacao("Ana"))
print(saudacao())
```

## 7. Classes (POO)

```nova
class Cachorro:
    func __init__(self, nome):
        self.nome = nome

    func latir(self):
        print(self.nome + " diz: au au!")

rex = Cachorro("Rex")
rex.latir()

class CachorroFalante(Cachorro):
    func falar(self):
        print(self.nome + " diz: olá!")
```

## 8. Tratamento de erro

```nova
try:
    numero = int(input("Digite um número: "))
catch ValueError:
    print("Isso não é um número!")
finally:
    print("Fim.")
```

## 9. Arquivos e módulos

```nova
open("dados.txt", "w").write("conteúdo")
texto = open("dados.txt", "r").read()

import math
print(math.sqrt(16))
```

## 10. Web em 5 linhas

```nova
import web

app = web.app("MeuSite")

@app.route("/")
func inicio():
    return "<h1>Meu site em NOVA!</h1>"

app.rodar(porta=8000)
```

## 11. Instalando no VS Code

1. Vá até `editores/vscode/` neste repositório.
2. Empacote a extensão:
   ```powershell
   npm install -g @vscode/vsce
   vsce package
   code --install-extension nova-language-0.1.0.vsix
   ```
   Ou copie a pasta para `C:\Users\USER\.vscode\extensions\nova-language-0.1.0`.
3. Crie um arquivo `.nova` e pronto: highlighting, snippets e o tema **NOVA Dark** ficam disponíveis.

## 11.1 Como EXECUTAR um programa NOVA (passo a passo)

> ⚠️ **Não use F5!** Esse aviso *"You don't have an extension for debugging NOVA"* aparece sempre que você tenta depurar. É esperado — use os atalhos abaixo.

1. Abra a pasta no VS Code: `Arquivo → Abrir Pasta → ...\nova`
2. Crie/abra o arquivo `.nova` (ex.: `exemplos/jogo.nova`)
3. **Salve com `Ctrl + S`** (se não salvar, nada acontece)
4. Execute com uma das opções:
   - `Ctrl + Shift + B` → "Rodar arquivo NOVA" (dentro da pasta `nova`)
   - `Ctrl + Alt + N` → roda de qualquer lugar
   - Terminal: `` Ctrl + ` `` e depois:
     ```powershell
     python "C:\Users\USER\Documents\Default Project\nova\interpretador\nova.py" "exemplos\jogo.nova"
     ```

### Problemas que você pode encontrar (e como resolver)

| Problema | Solução |
|---|---|
| Aviso ao apertar F5 | Use `Ctrl+Shift+B` ou `Ctrl+Alt+N` |
| "Select the build task" | Você está fora da pasta `nova` — abra-a ou use `Ctrl+Alt+N` |
| "build User" / CMake | Abra a pasta `nova` (não a raiz) ou desative o CMake Tools |
| `No suchfile or directory` com "Default" | Coloque aspas em volta de todo o caminho |
| Nada acontece | Salve o arquivo (`Ctrl + S`) |
| Acentos/emojis estranhos | Rode no terminal do VS Code (já força UTF-8) |

### Se o atalho `Ctrl + Alt + N` não funcionar

1. `Ctrl + Shift + P` → "Developer: Reload Window" → Enter
2. Abra o terminal: `` Ctrl + ` ``
3. Clique dentro do arquivo `.nova`
4. Aperte `Ctrl + Alt + N`
5. Arquivo salvo? (`Ctrl + S`)

Fallback direto no terminal:

```powershell
python "C:\Users\USER\Documents\Default Project\nova\interpretador\nova.py" "C:\caminho\do\arquivo.nova"
```

## 12. Exercícios

1. Crie uma função que receba dois números e retorne a soma.
2. Crie uma lista com 5 números e imprima apenas os pares usando list comprehension.
3. Crie uma classe `Carro` com atributos `marca` e `ano` e um método `info()`.
4. Escreva um programa que leia um nome do usuário e salve em um arquivo `nome.txt`.
5. Crie uma rota web `/saudacao/<nome>` que retorne uma mensagem personalizada.
