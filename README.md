# Nagłówek
~~Przekreślony paragraf~~
**Pogrubiony paragraf**
*Pragraf w kuryswie*
>Cytat
1. Zagnieżdżona
  1.1. Lista
  1.2. Numeryczna
- Zagnieżdżona
  - Lista
  - Nienumeryczna

`
#!/bin/bash
read -r -d '' tekst
echo -e "$tekst"
`
```
#!/bin/bash
read -p "Podaj liczbę:" number
if [[ "$number" =~ ^[0-9]+\.?[0-9]*$ ]]; then
echo "True"
else
echo "False"
fi
```
![git](picture/git.jpg)
