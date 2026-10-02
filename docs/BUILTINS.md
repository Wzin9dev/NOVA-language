# Funções Built-ins da NOVA

## Entrada/saída e informação
| Função | Descrição |
|---|---|
| `print(x)` | Imprime no console |
| `input(msg)` | Lê entrada do usuário |
| `len(x)` | Tamanho de sequências/coleções |
| `type(x)` | Tipo de um valor |

## Conversão de tipos
`str()`, `int()`, `float()`, `bool()`, `list()`, `dict()`, `tuple()`, `set()`

## Iteração e sequências
| Função | Descrição |
|---|---|
| `range(n)` | Sequência de inteiros |
| `enumerate(seq)` | Pares (índice, valor) |
| `zip(a, b)` | Agrupa sequências |
| `map(fn, seq)` | Aplica função a cada item |
| `filter(fn, seq)` | Filtra itens |
| `sorted(seq)` | Retorna nova lista ordenada |
| `reversed(seq)` | Inverte a sequência |

## Matemática
| Função | Descrição |
|---|---|
| `sum(seq)` | Somatorio |
| `min(seq)` / `max(seq)` | Menor/maior valor |
| `abs(x)` | Valor absoluto |
| `round(x, n)` | Arredonda |

## Biblioteca `math`
`sqrt`, `sin`, `cos`, `tan`, `log`, `exp`, `pi`, `e`, `ceil`, `floor`, `pow`, `factorial`

```nova
import math
x = math.sqrt(16)
```
