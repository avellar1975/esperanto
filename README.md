# esperanto
Estudo dos elementos linguísticos e suas utilizações em textos publicados, com a finalidade de adquirir os vocabulários mais utilizados.

# Seleção e preparação de textos

A conversão dos livros encontrados em pdf para txt se dará através do comando <kbd>pdftotext</kbd>, disponível no pacote “poppler-utils” no Debian. Caso não o tenha instalado:

```
# apt-get update
# apt-get install poppler-utils
```

Conversão do '.pdf' para '.txt'. Use:

 `pdftotext arquivo.pdf novo-arquivo.txt`


## Livros utilizados>:
* Dua Libro de l' Lingvo Internacia (Autor: L. L. Zamenhof)
* Vivo de Zamenhof (Privat, Edmond)
* Karlo (Privat, Edmond)
* Fundamenta Krestomatio (L. L. Zamenhof)
* Lingvaj Respondoj (L. L. Zamenhof)
* La Batalo de l' Vivo (Charles Dickens / Trad. L. L. Zamenhof) 
* Esenco kaj estonteco de la lingvo internacia (L. L. Zamenhof)


## Limpeza e preparação dos textos
Alguns arquivos PDF contêm fontes cujas codificações são danificadas e irreconhecíveis, para estes casos após conversão para PDF foi necessário uma substituição de letras usando um editor simples de texto.

Um dos textos estavam utilizando o sistema 'x' para letras acentuadas, e por isso foi preciso realizar a substituição, pelo mesmo método acima.

Os livros do site https://www.gutenberg.org/ foi preciso realizar a limpeza dos cabeçalhos e rodapés dos arquivos, pois não faziam parte dos livros.

## Juntando todos os textos em um
Como são somente 7 arquivos não foi preciso criar um script para isso. Para cada livro utilizei o comando:

`cat arquivo.txt >> dados.txt`

Através do comando `wc` é possível verificar que o arquivo final ficou com 31041 linhas, 245380 palavras e 1577373 caracteres.

```
$ wc dados.txt 
  31041  245380 1577373 dados.txt
```
## Rodando o programa kalkuli_vortoj.py

Através do comando cat e um pipline, executamos o programa com o argumento do TOP 'x' que queremos filtrar: 

```
$ cat tekstoj/dados.txt | python kalkuli_vortoj.py 20
17651	la
7575	kaj
7244	de
4597	en
3696	al
3158	ne
2780	estas
2749	mi
2708	li
2499	ke
1985	ĉi
1761	por
1681	sed
1640	vi
1530	ni
1439	kun
1321	estis
1179	kiel
1134	sur
1111	pli
```
Essas são as 20 palavras mais usadas nos textos que utilizamos como base de nosso estudo, com a quantidade de vezes que elas aparecem.

---
### Fonte
http://www.dominiopublico.gov.br/: site que possui uma quantidade grande de livros em Esperanto no formato pdf.
https://www.gutenberg.org/browse/languages/eo: site onde é possível baixar livros em Esperanto já em txt.

