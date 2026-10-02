# Módulos Nativos da NOVA

## `games` — Jogos 2D e 3D
Janelas, renderização, física e loop de jogos.

```nova
import games

jogo = games.janela("Jogo", 800, 600)
bola = games.circulo(100, 100, 20, cor="verde")

while jogo.aberto:
    bola.x = bola.x + 2
    jogo.desenhar(bola)
    jogo.atualizar()
```

## `web` — Desenvolvimento Web
Servidor e rotas simples.

```nova
import web
app = web.app("Site")

@app.route("/")
func inicio():
    return "<h1>Olá!</h1>"

app.rodar(porta=8000)
```

## `ui` — Desktop e Mobile
Interfaces gráficas e exportação.

```nova
import ui

janela = ui.janela("Meu App")
ui.botao(janela, "Clique", ao_clicar=func(): print("ok"))
ui.executar(janela)
```

Exportação via CLI: `nova build android` · `nova build desktop`

## `ia` — Inteligência Artificial
Vetores, matrizes e automação inteligente.

```nova
import ia
v = ia.vetor([1, 2, 3])
m = ia.matriz([[1, 2], [3, 4]])
```

## `auto` — Automação de tarefas

```nova
import auto
auto.abrir_app("chrome")
auto.teclar("enter")
auto.clicar(200, 300)
```
