# Linguagem de programação LOGO interpretador



Como utilizar
=============
Colocar os comandos no ficheiro input.txt, de seguida correr o main.py



Comandos válidos:
-------------
• **fd** value
• **bk** value
•** rt** value
• **lt** value
• **setpos** [ X Y ]
• **setxy** [ X Y ]
• **setx** X
• **home**
• **pd**
• **pu**
• **setpencolor** [ R G B ]
• **make** :var value
•** while** [ value operator value ] [ program ]
• **repeat** value [ program ]
•** if **comparation [ program ]
• ** ifelse ** comparation [ program ] [ program ]
• ** to func_name ** :param program end
• ** func_name ** :param

** Value: ** pode ser float, uma variável ou uma operação.
** Operator: ** <, > ou =
** Comparation: ** comparação entre dois values.

### Exemplos de programas
     to tree :size
		 ifelse :size < 5 [forward :size back :size]
			 [
			 forward :size/3
			 left 30 tree :size*2/3 right 30
			 forward :size/6
			 right 25 tree :size/2 left 25
			 forward :size/3
			 right 25 tree :size/2 left 25
			 forward :size/6
			 back :size
			 ]
		 end
	tree 150
---
    to fern :size :sign
		  if :size > 1 [
		  fd :size
		  rt 70 * :sign fern :size * 0.5 :sign * -1 lt 70 * :sign
		  fd :size
		  lt 70 * :sign fern :size * 0.5 :sign rt 70 * :sign
		  rt 7 * :sign fern :size - 1 :sign lt 7 * :sign
		  bk :size * 2  ]
	end
	pu bk 150 pd
	fern 25 1





