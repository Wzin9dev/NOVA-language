# NOVA — Linguagem de Programação

> **Status:** Especificação inicial v0.1 · Extensão de arquivo: `.nova` · CLI: `nova`

NOVA é uma linguagem de programação pensada para ser **extremamente simples de ler e escrever**, com batteries included: jogos 2D/3D, web, mobile/desktop, IA e automação são módulos nativos do runtime.

## Filosofia

1. **Clareza acima de tudo** — indentação define blocos, sem chaves e sem `end`.
2. **Uma linguagem para todos** — o iniciante imprime `"Olá, mundo"` e o profissional expõe uma API com a mesma sintaxe.
3. **Tudo embutido** — `games`, `web`, `ui`, `ia` e `auto` vêm com o runtime.

## Exemplo rápido

```nova
func saudação(jogador = "visitante"):
    return "Bem-vindo, " + jogador + "!"

print(saudação("Ana"))
```

```nova
import web

app = web.app("MeuSite")

@app.route("/")
func inicio():
    return "<h1>Olá da NOVA!</h1>"

app.rodar(porta=8000)
```

## Documentação

- [Especificação completa](docs/ESPECIFICACAO.md)
- [Tutorial — Aprendendo NOVA](docs/TUTORIAL.md)
- [Gramática formal (BNF)](docs/GRAMATICA.md)
- [Built-ins](docs/BUILTINS.md)
- [Módulos nativos](docs/MODULOS.md)
- [Extensão do VS Code](docs/EXTENSAO_VSCODE.md)
- [Roadmap](docs/ROADMAP.md)

## Exemplos

- [`exemplos/demo.nova`](exemplos/demo.nova) — programa completo (funções, classes, listas, jogo 2D, tratamento de erro)
- [`exemplos/site.nova`](exemplos/site.nova) — servidor web com rotas

## Começando

```bash
nova new meu_projeto
nova run exemplos/demo.nova
nova build android
nova build desktop
```

## Executando programas NOVA (passo a passo)

> ⚠️ **Não use F5!** F5 é para depuração e sempre mostrará o aviso "You don't have an extension for debugging NOVA". Esse aviso é esperado enquanto o depurador não existir. Use `Ctrl + Shift + B` (dentro da pasta `nova`) ou `Ctrl + Alt + N`.

### Opção A — Pelo terminal (funciona em qualquer pasta)

```powershell
python "C:\Users\USER\Documents\Default Project\nova\interpretador\nova.py" "C:\caminho\do\seu\arquivo.nova"
```

### Opção B — Ctrl + Shift + B (pasta nova aberta no VS Code)

1. `Arquivo → Abrir Pasta → ...\Default Project\nova` (a pasta `nova`, não a raiz)
2. Abra o arquivo `.nova`
3. `Ctrl + Shift + B` → escolha "Rodar arquivo NOVA" se perguntado

### Opção C — Ctrl + Alt + N (funciona em qualquer lugar)

1. `Ctrl + Shift + P` → "Developer: Reload Window" (depois de configurar o atalho)
2. Abra o arquivo `.nova`
3. `Ctrl + Alt + N` → o arquivo roda no terminal integrado

> ⚠️ **Salve o arquivo (`Ctrl + S`) antes de executar!** Se o arquivo estiver vazio/não salvo, nada acontece (sem saída, sem erro).

## Problemas comuns

| Problema | Causa | Solução |
|---|---|---|
| Aviso ao apertar F5 | F5 = debug, NOVA ainda não tem depurador | Use `Ctrl+Shift+B` ou `Ctrl+Alt+N` |
| Pergunta "Select the build task" | `Ctrl+Shift+B` fora da pasta `nova` | Abra a pasta `nova` no VS Code ou use `Ctrl+Alt+N` |
| Pergunta "build User" / CMake | Extensão CMake Tools ativa ou pasta errada | Abra a pasta `nova`, ou desative o CMake Tools |
| Erro `No suchfile or directory` com "Default" | Caminho com espaço sem aspas | Use as aspas ao redor de todo o caminho |
| Nada acontece ao rodar | Arquivo não salvo (vazio) | `Ctrl + S` e rode de novo |
| Caracteres estranhos (��) | Encoding do console | O interpretador já força UTF-8; use o terminal do VS Code |

### Checklist do atalho `Ctrl + Alt + N`

Se o atalho não funcionar, verifique na ordem:

1. **Recarregue o VS Code**: `Ctrl + Shift + P` → "Developer: Reload Window" → Enter
2. **Abra o terminal**: `` Ctrl + ` ``
3. **Clique dentro do arquivo `.nova`** (não no terminal)
4. Aperte **`Ctrl + Alt + N`**
5. O arquivo está salvo? (`Ctrl + S`)

Se mesmo assim não funcionar, use o terminal direto:

```powershell
python "C:\Users\USER\Documents\Default Project\nova\interpretador\nova.py" "C:\caminho\do\arquivo.nova"
```

Já existe um interpretador de referência (Python) em `interpretador/`:

```powershell
python interpretador/nova.py exemplos/demo.nova
# ou pelo atalho:
.\nova.bat exemplos/demo.nova
```

Ele executa o subconjunto principal da linguagem (funções, classes, laços, compreensões, try/catch) e usa stubs dos módulos nativos (`games`, `web`, `ui`, `ia`, `auto`).

## Contribuindo

Veja [CONTRIBUTING.md](CONTRIBUTING.md).

## Licença

[MIT](LICENSE)
