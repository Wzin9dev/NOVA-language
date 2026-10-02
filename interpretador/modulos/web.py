"""Stub nativo do módulo `web` (servidor e rotas)."""


class App:
    def __init__(self, nome):
        self.nome = nome
        self.rotas = {}

    def route(self, caminho):
        def decorador(func):
            self.rotas[caminho] = func
            return func
        return decorador

    def rodar(self, porta=8000):
        print(f"[web] '{self.nome}' rodando em http://localhost:{porta}")
        for rota in self.rotas:
            print(f"[web]   rota registrada: {rota}")


def app(nome):
    return App(nome)
