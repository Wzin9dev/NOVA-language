"""Stub nativo do módulo `games` (jogos 2D/3D)."""


class Janela:
    def __init__(self, titulo, largura, altura):
        self.titulo = titulo
        self.largura = largura
        self.altura = altura
        self.aberto = False  # no stub, a janela abre e fecha imediatamente
        print(f"[games] Janela '{titulo}' ({largura}x{altura}) criada.")

    def desenhar(self, obj):
        pass

    def atualizar(self):
        pass


class Retangulo:
    def __init__(self, x, y, w, h, cor="branco"):
        self.x, self.y, self.w, self.h, self.cor = x, y, w, h, cor

    def colidiu(self, outro):
        return False


def janela(titulo, largura, altura):
    return Janela(titulo, largura, altura)


def retangulo(x, y, w, h, cor="branco"):
    return Retangulo(x, y, w, h, cor)


def tecla(nome):
    return False
