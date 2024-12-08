# Source: https://en.wikibooks.org/wiki/Computer_Programming/Hello_world#brainfuck
+++++ +++++             # initialize counter (cell #0) to 10
[                       # use loop to set the next four cells to 70/100/30/10
    > +++++ ++          #     add  7 to cell #1
    > +++++ +++++       #     add 10 to cell #2
    > +++               #     add  3 to cell #3
    > +                 #     add  1 to cell #4
    <<<< -              #     decrement counter (cell #0)
]
> ++ .                  # print 'H' (see the .)
> + .                   # print 'e'
+++++ ++ .              # print 'l'
.                       # print 'l'
+++ .                   # print 'o'
> ++ .                  # print ' '
<< +++++ +++++ +++++ .  # print 'W'
> .                     # print 'o'
+++ .                   # print 'r'
----- - .               # print 'l'
----- --- .             # print 'd'
> + .                   # print '!'
> .
