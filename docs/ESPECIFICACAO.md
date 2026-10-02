# NOVA — Linguagem de Programação (Especificação Inicial)

> Versão: 0.1 (rascunho conceitual) | Extensão de arquivo: `.nova` | CLI: `nova`

---

## 1. Filosofia da Linguagem

A NOVA nasce com três princípios:

1. **Clareza acima de tudo** — o código é lido muito mais do que é escrito. Blocos são definidos por indentação (como Python), sem chaves e sem `end`. Não há cerimonial: variáveis não precisam de declaração de tipo.
2. **Faixa única para todos os públicos** — a mesma linguagem serve ao iniciante que imprime `"Olá, mundo"` e ao profissional que expõe uma API web, renderiza um jogo 3D ou treina um modelo de vetores. O que muda é o módulo importado, não a sintaxe.
3. **Bateria inclusa de verdade** — jogos 2D/3D, web, mobile/desktop, IA e automação são módulos nativos, instalados junto com o runtime. Nada de caçar bibliotecas de terceiros para começar.

Diferenças deliberadas em relação ao Python (para quem vem de lá):

- Funções usam `func` em vez de `def`.
- Erros usam `catch` em vez de `except` (mais próximo de Java/JS, fácil de reconhecer).
- Constantes são escritas EM_MAIÚSCULAS por convenção.
- O restante — `for`, `while`, compreensões de lista, classes, decorators — segue o modelo mental do Python, reduzindo a curva de migração para zero.

---

## 2. Tipos de Dados e Estruturas Primárias

| Categoria | Tipo | Exemplo |
|---|---|---|
| Inteiro | `int` | `42` |
| Real | `float` | `3.14` |
| Texto | `str` | `"nova"` |
| Booleano | `bool` | `True`, `False` |
| Nulo | `None` | `None` |
| Lista | `list` | `[1, 2, 3]` |
| Dicionário | `dict` | `{"a": 1}` |
| Tupla | `tuple` | `(1, 2)` |
| Conjunto | `set` | `{1, 2, 3}` |

Compreensão de lista nativa:

```nova
dobros = [n * 2 for n in range(10) if n % 2 == 0]
```

---

## 3. Exemplo de Sintaxe — Programa Completo

Arquivo `demo.nova` demonstrando: variáveis, funções com parâmetro padrão, classe com herança, listas, list comprehension, tratamento de erro, manipulação de arquivo, e **um jogo 2D simples**.

```nova
# ============================================
# NOVA - Programa de demonstração completo
# ============================================

import games
import math

# --- Variáveis ---
NOME_JOGO = "Corrida NOVA"
MAX_PONTOS = 100

# --- Função com parâmetro padrão ---
func saudação(jogador = "visitante"):
    return "Bem-vindo, " + jogador + "!"

print(saudação())
print(saudação("Ana"))

# --- Classe e herança ---
class Jogador:
    func __init__(self, nome, pontos=0):
        self.nome = nome
        self.pontos = pontos

    func pontuar(self, valor):
        self.pontos = self.pontos + valor
        if self.pontos > MAX_PONTOS:
            self.pontos = MAX_PONTOS

class JogadorPro(Jogador):          # herança
    func pontuar(self, valor):
        super().pontuar(valor * 2)  # ganha pontos dobrados

# --- Listas e list comprehension ---
recordes = [55, 80, MAX_PONTOS, 30, 42]
melhores = [p for p in recordes if p >= 50]   # [80, 100]
resumo = {"media": sum(recordes) / len(recordes),
          "limite": math.ceil(sum(recordes) / len(recordes))}
print(melhores)
print(resumo)

# --- Tratamento de erro ---
try:
    pontos = int(input("Seus pontos iniciais: "))
except ValueError:
    print("Valor inválido, começando com 0.")
    pontos = 0
finally:
    print("Iniciando o jogo...")

jogador = JogadorPro("Ana", pontos)

# --- Estruturas de controle ---
while jogador.pontos < MAX_PONTOS:
    if pontos > 50:
        jogador.pontuar(10)
    elif pontos == 0:
        jogador.pontuar(5)
    else:
        jogador.pontuar(1)
    pontos = pontos - 1
    if jogador.pontos >= 80:
        break

for i, recorde in enumerate(sorted(melhores)):
    print(i, recorde)

# --- Jogo 2D simples usando o módulo nativo `games` ---
jogo = games.janela(NOME_JOGO, 800, 600)
jogador_sprite = games.retangulo(100, 100, 50, 50, cor="azul")
adversario = games.retangulo(500, 300, 50, 50, cor="vermelho")

while jogo.aberto:
    if games.tecla("esquerda"): jogador_sprite.x = jogador_sprite.x - 5
    if games.tecla("direita"):  jogador_sprite.x = jogador_sprite.x + 5
    if games.tecla("cima"):     jogador_sprite.y = jogador_sprite.y - 5
    if games.tecla("baixo"):    jogador_sprite.y = jogador_sprite.y + 5

    if jogador_sprite.colidiu(adversario):
        jogador.pontuar(10)
        adversario.x = 600   # reposiciona o adversário

    jogo.desenhar(jogador_sprite)
    jogo.desenhar(adversario)
    jogo.atualizar()

# --- Manipulação de arquivos ---
try:
    open("placar.txt", "w").write(jogador.nome + ": " + str(jogador.pontos))
    print(open("placar.txt", "r").read())
except IOError:
    print("Não foi possível salvar o placar.")
```

Versão **web** do mesmo estilo (arquivo `site.nova`):

```nova
import web

app = web.app("MeuSite")

@app.route("/")
func inicio():
    return "<h1>Olá da NOVA!</h1>"

@app.route("/jogador/<nome>")
func pagina_jogador(nome):
    return "<h2>Jogador: " + nome + "</h2>"

app.rodar(porta=8000)
```

Inteligência artificial e automação ficariam assim:

```nova
import ia
import auto

pesos = ia.vetor([0.2, 0.5, 0.3])          # manipulação de vetores nativa
matriz = ia.matriz([[1, 2], [3, 4]])
traco = auto.ler_tela("jogos.png")          # automação de tarefas do sistema
auto.teclar("enter")
```

---

## 4. Built-ins Obrigatórios

- **Entrada/saída e informação:** `print()`, `input()`, `len()`, `type()`
- **Conversão de tipos:** `str()`, `int()`, `float()`, `bool()`, `list()`, `dict()`, `tuple()`, `set()`
- **Iteração e sequências:** `range()`, `enumerate()`, `zip()`, `map()`, `filter()`, `sorted()`, `reversed()`
- **Matemática:** `sum()`, `min()`, `max()`, `abs()`, `round()`
- **Matemática avançada:** módulo `math` nativo (`sqrt`, `sin`, `cos`, `pi`, `ceil`, `floor`, ...)

 Módulos integrados: `games` (2D/3D: janelas, física, loop de jogo), `web` (servidor e rotas), `ui` (desktop/mobile, exportação via `nova build android` / `nova build desktop`), `ia` (vetores, matrizes, modelos), `auto` (automação do sistema).

---

## 5. Extensão para VS Code (e demais editores)

Como funcionaria na prática:

### 5.1 Estrutura do pacote da extensão

```
nova-vscode/
├─ package.json                 # manifest da extensão
├─ language-configuration.json  # comentários, colchetes, indentação
├─ syntaxes/
│   └─ nova.tmLanguage.json     # grammar TextMate (highlighting)
├─ snippets/
│   └─ nova.json                # snippets (func, for, class, try...)
├─ themes/
│   └─ nova-dark.json           # tema opcional
└─ server/                      # servidor LSP
    └─ nova-lsp
```

### 5.2 `package.json` (trecho essencial)

```json
{
  "name": "nova-language",
  "contributes": {
    "languages": [{
      "id": "nova",
      "aliases": ["NOVA", "nova"],
      "extensions": [".nova"],
      "configuration": "./language-configuration.json"
    }],
    "grammars": [{
      "language": "nova",
      "scopeName": "source.nova",
      "path": "./syntaxes/nova.tmLanguage.json"
    }],
    "snippets": [{ "language": "nova", "path": "./snippets/nova.json" }],
    "themes": [{ "label": "NOVA Dark", "uiTheme": "vs-dark", "path": "./themes/nova-dark.json" }]
  }
}
```

### 5.3 `language-configuration.json`

```json
{
  "comments": { "lineComment": "#" },
  "brackets": [["{", "}"], ["[", "]"], ["(", ")"]],
  "autoClosingPairs": [
    { "open": "(", "close": ")" },
    { "open": "[", "close": "]" },
    { "open": "{", "close": "}" },
    { "open": "\"", "close": "\"" }
  ],
  "indentationRules": {
    "increaseIndentPattern": ":\\s*$",
    "decreaseIndentPattern": "^\\s*(elif|else|catch|finally)\\b"
  }
}
```

### 5.4 Grammar TextMate (trecho de `nova.tmLanguage.json`)

O highlighting funciona por regex sobre os escopos:

```json
{
  "scopeName": "source.nova",
  "patterns": [
    { "name": "comment.line.number-sign.nova", "match": "#.*$" },
    { "name": "keyword.control.nova",
      "match": "\\b(func|class|if|elif|else|for|while|try|catch|finally|return|import|from|break|continue|in|and|or|not|super)\\b" },
    { "name": "support.function.builtin.nova",
      "match": "\\b(print|input|len|type|str|int|float|bool|list|dict|tuple|set|range|enumerate|zip|map|filter|sorted|reversed|sum|min|max|abs|round)\\b" },
    { "name": "string.quoted.double.nova", "begin": "\"", "end": "\"" },
    { "name": "constant.numeric.nova", "match": "\\b\\d+(\\.\\d+)?\\b" },
    { "name": "entity.name.function.nova",
      "match": "(?<=func\\s)[A-Za-z_][A-Za-z0-9_]*" }
  ]
}
```

### 5.5 Inteligência real: o servidor LSP

TextMate cuida só das cores. Para autocompletar, sublinhar erros, ir à definição e formatar, a NOVA entrega um servidor pelo protocolo LSP (`nova lsp`). Configuração no VS Code:

```json
{
  "nova.lsp.path": "nova",
  "nova.lsp.args": ["lsp"]
}
```

### 5.6 Outros editores

- **VS Code / Visual Studio:** VS puro usa a mesma grammar TextMate (importável via *TextMate Grammar*); o LSP cobre IntelliSense.
- **PyCharm:** aceita bundles TextMate nativamente (Settings → Editor → TextMate) — o mesmo `nova.tmLanguage.json` funciona.
- **Neovim:** grammar Tree-sitter (`nova-tree-sitter`) para highlighting estrutural + `lspconfig` apontando para `nova lsp`.

### 5.7 Fluxo do desenvolvedor no dia a dia

```bash
nova new meu_jogo           # cria projeto a partir de template
nova run demo.nova          # executa
nova build android          # exporta APK
nova build desktop          # empacota executável
nova fmt demo.nova          # formata o código
nova test                   # roda testes
```

---

*Documento inicial — sujeito a discussão e iteração comunitária.*
