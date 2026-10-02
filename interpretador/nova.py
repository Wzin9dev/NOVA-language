#!/usr/bin/env python3
"""Interpretador de referência da linguagem NOVA (subconjunto).

Uso: python interpretador/nova.py arquivo.nova
"""
import re
import sys
import os

# Garante que os módulos nativos da NOVA (stubs) e o diretório do arquivo sejam importáveis
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "modulos"))

# Força UTF-8 no console do Windows (acentos e emojis)
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass


def traduzir(codigo: str) -> str:
    """Converte a sintaxe NOVA para Python executável."""
    codigo = re.sub(r"\bfunc\b", "def", codigo)
    codigo = re.sub(r"\bcatch\b", "except", codigo)
    return codigo


def executar(caminho: str) -> None:
    with open(caminho, "r", encoding="utf-8") as f:
        codigo_nova = f.read()
    codigo_py = traduzir(codigo_nova)
    diretorio = os.path.dirname(os.path.abspath(caminho))
    sys.path.insert(0, diretorio)
    try:
        exec(compile(codigo_py, caminho, "exec"), {"__name__": "__main__"})
    except Exception as e:
        print(f"[NOVA] Erro em tempo de execução: {type(e).__name__}: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: nova <arquivo.nova>")
        sys.exit(1)
    executar(sys.argv[1])
