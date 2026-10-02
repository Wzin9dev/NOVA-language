"""Stub nativo do módulo `ui` (interfaces desktop/mobile)."""


class Janela:
    def __init__(self, titulo):
        self.titulo = titulo
        print(f"[ui] Janela '{titulo}' criada.")


def janela(titulo):
    return Janela(titulo)


def botao(janela, texto, ao_clicar=None):
    print(f"[ui] Botão '{texto}' adicionado.")


def executar(janela):
    print(f"[ui] Evento loop da janela '{janela.titulo}' (stub).")
