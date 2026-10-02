# Gramática Formal da NOVA (BNF simplificada)

```bnf
programa      ::= declaracao*

declaracao    ::= funcDecl
                | classDecl
                | importDecl
                | atribuicao
                | expressao
                | blocoControle

funcDecl      ::= "func" IDENT "(" parametros? ")" ":" bloco
classDecl     ::= "class" IDENT ("(" IDENT ")")? ":" bloco
importDecl    ::= "import" IDENT (" as " IDENT)?
                | "from" IDENT "import" IDENT ("," IDENT)*

bloco         ::= NEWLINE INDENT declaracao+ DEDENT

blocoControle ::= ifDecl | forDecl | whileDecl | tryDecl
ifDecl        ::= "if" expressao ":" bloco
                  ("elif" expressao ":" bloco)*
                  ("else" ":" bloco)?
forDecl       ::= "for" IDENT "in" expressao ":" bloco
whileDecl     ::= "while" expressao ":" bloco
tryDecl       ::= "try" ":" bloco
                  "catch" (IDENT)? ":" bloco
                  ("finally" ":" bloco)?

parametros    ::= parametro ("," parametro)*
parametro     ::= IDENT ("=" expressao)?

atribuicao    ::= IDENT ("." IDENT)* "=" expressao

expressao     ::= literal
                | IDENT
                | expressao operadorBinario expressao
                | chamada
                | comprehension
                | expressao "[" expressao "]"
                | expressao "." IDENT

chamada       ::= IDENT "(" argumentos? ")"
argumentos    ::= expressao ("," expressao)*

comprehension ::= "[" expressao "for" IDENT "in" expressao
                   ("if" expressao)? "]"

operadorBinario ::= "+" | "-" | "*" | "/" | "%" | "==" | "!=" | "<"
                  | "<=" | ">" | ">=" | "and" | "or" | "in"

literal       ::= NUMERO | STRING | "True" | "False" | "None"
                | lista | dicionario | tupla | conjunto
lista         ::= "[" (expressao ("," expressao)*)? "]"
dicionario    ::= "{" (par ("," par)*)? "}"
par           ::= expressao ":" expressao
tupla         ::= "(" (expressao ("," expressao)*)? ")"
conjunto      ::= "{" expressao ("," expressao)+ "}"
```

Regras de indentação: bloco abre após `:` no fim da linha; nível de indentação crescente abre bloco e `def` de blocos decresce ao encontrar `elif`, `else`, `catch`, `finally` ou indent menor.
