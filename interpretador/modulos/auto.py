"""Stub nativo do módulo `auto` (automação do sistema)."""


def abrir_app(nome):
    print(f"[auto] Abrindo {nome}...")


def teclar(tecla):
    print(f"[auto] Tecla pressionada: {tecla}")


def clicar(x, y):
    print(f"[auto] Clique em ({x}, {y})")


def ler_tela(caminho="tela.png"):
    print(f"[auto] Captura de tela salva em {caminho}")
    return caminho
