# Roadmap da NOVA

## v0.1 — Especificação (atual)
- [x] Definição da sintaxe
- [x] Built-ins obrigatórios
- [x] Módulos nativos (`games`, `web`, `ui`, `ia`, `auto`)
- [x] Extensão VS Code (highlighting + LSP básico)

## v0.2 — Interpretador de referência
- [x] Parser conforme a gramática BNF
- [x] Executor (transpilador NOVA → Python em `interpretador/`)
- [ ] Testes de conformidade

## v0.3 — Módulos nativos
- [ ] `games`: janela, sprites, colisão
- [ ] `web`: servidor HTTP, rotas, templates
- [ ] `ui`: janela desktop, botões, exportação
- [ ] `ia`: vetores, matrizes, operações
- [ ] `auto`: automação de teclado/mouse

## v1.0
- [ ] Compilador para bytecode
- [ ] Empacotador desktop/Android
- [ ] Package manager (`nova pkg`)
