#LOGO interpreter



How to use
=============
Put the commands in the file input.txt, then run main.py




Valid commands:
-------------
• **fd** value <br/>
• **bk** value <br/>
• **rt** value <br/>
• **lt** value <br/>
• **setpos** [ X Y ] <br/>
• **setxy** [ X Y ] <br/>
• **setx** X <br/>
• **home** <br/>
• **pd** <br/>
• **pu** <br/>
• **setpencolor** [ R G B ] <br/>
• **make** :var value <br/>
• **while** [ value operator value ] [ program ] <br/>
• **repeat** value [ program ] <br/>
• **if** comparation [ program ] <br/>
• **ifelse** comparation [ program ] [ program ] <br/>
• **to func_name** :param program end <br/>
• **func_name** :param <br/>

**Value:** can be a float, a variable or an operation <br/>
**Operator:** <, > or = <br/>
**Comparation:** comparison between two values. <br/>

### Example of programs
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





