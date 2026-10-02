# Extensão para VS Code

A NOVA é suportada em qualquer editor moderno através de dois mecanismos:

1. **Grammar TextMate** — syntax highlighting.
2. **Servidor LSP** (`nova lsp`) — autocomplete, diagnósticos, hover, definição.

## Estrutura

```
editores/vscode/
├─ package.json
├─ language-configuration.json
├─ syntaxes/nova.tmLanguage.json
├─ snippets/nova.json
└─ themes/nova-dark.json
```

Os arquivos reais estão em [`editores/vscode/`](../editores/vscode).

## Outros editores

| Editor | Como instalar |
|---|---|
| VS Code | Extensão empacotada (.vsix) |
| Visual Studio | Importar a grammar TextMate em Settings → Text Editor |
| PyCharm | Settings → Editor → TextMate Bundles |
| Neovim | Tree-sitter + `lspconfig` apontando para `nova lsp` |

## LSP

No VS Code, adicione ao `settings.json`:

```json
{
  "nova.lsp.path": "nova",
  "nova.lsp.args": ["lsp"]
}
```
