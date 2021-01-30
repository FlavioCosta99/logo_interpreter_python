
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftorleftandleft+-left*/FLOAT STR VAR and bk end fd home if ifelse lt make or pd pu repeat rt setpencolor setpos setx setxy sety to while program :  command  program : program command  command : fd value command : bk value command : rt value command : lt value  command : setpos '[' value value ']'  command : setxy value value  command : setx value command : sety value command : home command : pd command : pu command : setpencolor '[' value value value ']'  command : make VAR value  command : while '[' value operator value ']' '[' program ']'    command : repeat value '[' program ']'   value  :   FLOAT\n                    |   VAR\n                    |   '(' value ')'\n                    |   value operations value  operator : '>'\n                    | '<'\n                    | '='  operations : '*'\n                       | '-'\n                       | '+'\n                       | '/'  command : if comparation '[' program ']'  command : ifelse comparation '[' program ']' '[' program ']'  comparation : value operator value\n                        | comparation and comparation\n                        | comparation or comparation  varlist :\n                   | VAR\n                   | varlist VAR   command : to STR varlist program end command : STR inc_value  inc_value :\n                      | value\n                      | inc_value value "
    
_lr_action_items = {'fd':([0,1,2,11,12,13,21,22,23,24,25,27,28,29,32,33,41,42,43,51,53,55,56,63,64,65,66,67,68,72,73,77,78,79,80,83,84,86,87,89,90,91,92,93,94,],[3,3,-1,-11,-12,-13,-39,-2,-3,-18,-19,-4,-5,-6,-9,-10,-34,-38,-40,-8,-15,3,3,3,3,-35,-41,-21,-20,3,3,3,3,-36,-7,-17,-29,-37,-14,3,3,3,3,-30,-16,]),'bk':([0,1,2,11,12,13,21,22,23,24,25,27,28,29,32,33,41,42,43,51,53,55,56,63,64,65,66,67,68,72,73,77,78,79,80,83,84,86,87,89,90,91,92,93,94,],[4,4,-1,-11,-12,-13,-39,-2,-3,-18,-19,-4,-5,-6,-9,-10,-34,-38,-40,-8,-15,4,4,4,4,-35,-41,-21,-20,4,4,4,4,-36,-7,-17,-29,-37,-14,4,4,4,4,-30,-16,]),'rt':([0,1,2,11,12,13,21,22,23,24,25,27,28,29,32,33,41,42,43,51,53,55,56,63,64,65,66,67,68,72,73,77,78,79,80,83,84,86,87,89,90,91,92,93,94,],[5,5,-1,-11,-12,-13,-39,-2,-3,-18,-19,-4,-5,-6,-9,-10,-34,-38,-40,-8,-15,5,5,5,5,-35,-41,-21,-20,5,5,5,5,-36,-7,-17,-29,-37,-14,5,5,5,5,-30,-16,]),'lt':([0,1,2,11,12,13,21,22,23,24,25,27,28,29,32,33,41,42,43,51,53,55,56,63,64,65,66,67,68,72,73,77,78,79,80,83,84,86,87,89,90,91,92,93,94,],[6,6,-1,-11,-12,-13,-39,-2,-3,-18,-19,-4,-5,-6,-9,-10,-34,-38,-40,-8,-15,6,6,6,6,-35,-41,-21,-20,6,6,6,6,-36,-7,-17,-29,-37,-14,6,6,6,6,-30,-16,]),'setpos':([0,1,2,11,12,13,21,22,23,24,25,27,28,29,32,33,41,42,43,51,53,55,56,63,64,65,66,67,68,72,73,77,78,79,80,83,84,86,87,89,90,91,92,93,94,],[7,7,-1,-11,-12,-13,-39,-2,-3,-18,-19,-4,-5,-6,-9,-10,-34,-38,-40,-8,-15,7,7,7,7,-35,-41,-21,-20,7,7,7,7,-36,-7,-17,-29,-37,-14,7,7,7,7,-30,-16,]),'setxy':([0,1,2,11,12,13,21,22,23,24,25,27,28,29,32,33,41,42,43,51,53,55,56,63,64,65,66,67,68,72,73,77,78,79,80,83,84,86,87,89,90,91,92,93,94,],[8,8,-1,-11,-12,-13,-39,-2,-3,-18,-19,-4,-5,-6,-9,-10,-34,-38,-40,-8,-15,8,8,8,8,-35,-41,-21,-20,8,8,8,8,-36,-7,-17,-29,-37,-14,8,8,8,8,-30,-16,]),'setx':([0,1,2,11,12,13,21,22,23,24,25,27,28,29,32,33,41,42,43,51,53,55,56,63,64,65,66,67,68,72,73,77,78,79,80,83,84,86,87,89,90,91,92,93,94,],[9,9,-1,-11,-12,-13,-39,-2,-3,-18,-19,-4,-5,-6,-9,-10,-34,-38,-40,-8,-15,9,9,9,9,-35,-41,-21,-20,9,9,9,9,-36,-7,-17,-29,-37,-14,9,9,9,9,-30,-16,]),'sety':([0,1,2,11,12,13,21,22,23,24,25,27,28,29,32,33,41,42,43,51,53,55,56,63,64,65,66,67,68,72,73,77,78,79,80,83,84,86,87,89,90,91,92,93,94,],[10,10,-1,-11,-12,-13,-39,-2,-3,-18,-19,-4,-5,-6,-9,-10,-34,-38,-40,-8,-15,10,10,10,10,-35,-41,-21,-20,10,10,10,10,-36,-7,-17,-29,-37,-14,10,10,10,10,-30,-16,]),'home':([0,1,2,11,12,13,21,22,23,24,25,27,28,29,32,33,41,42,43,51,53,55,56,63,64,65,66,67,68,72,73,77,78,79,80,83,84,86,87,89,90,91,92,93,94,],[11,11,-1,-11,-12,-13,-39,-2,-3,-18,-19,-4,-5,-6,-9,-10,-34,-38,-40,-8,-15,11,11,11,11,-35,-41,-21,-20,11,11,11,11,-36,-7,-17,-29,-37,-14,11,11,11,11,-30,-16,]),'pd':([0,1,2,11,12,13,21,22,23,24,25,27,28,29,32,33,41,42,43,51,53,55,56,63,64,65,66,67,68,72,73,77,78,79,80,83,84,86,87,89,90,91,92,93,94,],[12,12,-1,-11,-12,-13,-39,-2,-3,-18,-19,-4,-5,-6,-9,-10,-34,-38,-40,-8,-15,12,12,12,12,-35,-41,-21,-20,12,12,12,12,-36,-7,-17,-29,-37,-14,12,12,12,12,-30,-16,]),'pu':([0,1,2,11,12,13,21,22,23,24,25,27,28,29,32,33,41,42,43,51,53,55,56,63,64,65,66,67,68,72,73,77,78,79,80,83,84,86,87,89,90,91,92,93,94,],[13,13,-1,-11,-12,-13,-39,-2,-3,-18,-19,-4,-5,-6,-9,-10,-34,-38,-40,-8,-15,13,13,13,13,-35,-41,-21,-20,13,13,13,13,-36,-7,-17,-29,-37,-14,13,13,13,13,-30,-16,]),'setpencolor':([0,1,2,11,12,13,21,22,23,24,25,27,28,29,32,33,41,42,43,51,53,55,56,63,64,65,66,67,68,72,73,77,78,79,80,83,84,86,87,89,90,91,92,93,94,],[14,14,-1,-11,-12,-13,-39,-2,-3,-18,-19,-4,-5,-6,-9,-10,-34,-38,-40,-8,-15,14,14,14,14,-35,-41,-21,-20,14,14,14,14,-36,-7,-17,-29,-37,-14,14,14,14,14,-30,-16,]),'make':([0,1,2,11,12,13,21,22,23,24,25,27,28,29,32,33,41,42,43,51,53,55,56,63,64,65,66,67,68,72,73,77,78,79,80,83,84,86,87,89,90,91,92,93,94,],[15,15,-1,-11,-12,-13,-39,-2,-3,-18,-19,-4,-5,-6,-9,-10,-34,-38,-40,-8,-15,15,15,15,15,-35,-41,-21,-20,15,15,15,15,-36,-7,-17,-29,-37,-14,15,15,15,15,-30,-16,]),'while':([0,1,2,11,12,13,21,22,23,24,25,27,28,29,32,33,41,42,43,51,53,55,56,63,64,65,66,67,68,72,73,77,78,79,80,83,84,86,87,89,90,91,92,93,94,],[16,16,-1,-11,-12,-13,-39,-2,-3,-18,-19,-4,-5,-6,-9,-10,-34,-38,-40,-8,-15,16,16,16,16,-35,-41,-21,-20,16,16,16,16,-36,-7,-17,-29,-37,-14,16,16,16,16,-30,-16,]),'repeat':([0,1,2,11,12,13,21,22,23,24,25,27,28,29,32,33,41,42,43,51,53,55,56,63,64,65,66,67,68,72,73,77,78,79,80,83,84,86,87,89,90,91,92,93,94,],[17,17,-1,-11,-12,-13,-39,-2,-3,-18,-19,-4,-5,-6,-9,-10,-34,-38,-40,-8,-15,17,17,17,17,-35,-41,-21,-20,17,17,17,17,-36,-7,-17,-29,-37,-14,17,17,17,17,-30,-16,]),'if':([0,1,2,11,12,13,21,22,23,24,25,27,28,29,32,33,41,42,43,51,53,55,56,63,64,65,66,67,68,72,73,77,78,79,80,83,84,86,87,89,90,91,92,93,94,],[18,18,-1,-11,-12,-13,-39,-2,-3,-18,-19,-4,-5,-6,-9,-10,-34,-38,-40,-8,-15,18,18,18,18,-35,-41,-21,-20,18,18,18,18,-36,-7,-17,-29,-37,-14,18,18,18,18,-30,-16,]),'ifelse':([0,1,2,11,12,13,21,22,23,24,25,27,28,29,32,33,41,42,43,51,53,55,56,63,64,65,66,67,68,72,73,77,78,79,80,83,84,86,87,89,90,91,92,93,94,],[19,19,-1,-11,-12,-13,-39,-2,-3,-18,-19,-4,-5,-6,-9,-10,-34,-38,-40,-8,-15,19,19,19,19,-35,-41,-21,-20,19,19,19,19,-36,-7,-17,-29,-37,-14,19,19,19,19,-30,-16,]),'to':([0,1,2,11,12,13,21,22,23,24,25,27,28,29,32,33,41,42,43,51,53,55,56,63,64,65,66,67,68,72,73,77,78,79,80,83,84,86,87,89,90,91,92,93,94,],[20,20,-1,-11,-12,-13,-39,-2,-3,-18,-19,-4,-5,-6,-9,-10,-34,-38,-40,-8,-15,20,20,20,20,-35,-41,-21,-20,20,20,20,20,-36,-7,-17,-29,-37,-14,20,20,20,20,-30,-16,]),'STR':([0,1,2,11,12,13,20,21,22,23,24,25,27,28,29,32,33,41,42,43,51,53,55,56,63,64,65,66,67,68,72,73,77,78,79,80,83,84,86,87,89,90,91,92,93,94,],[21,21,-1,-11,-12,-13,41,-39,-2,-3,-18,-19,-4,-5,-6,-9,-10,-34,-38,-40,-8,-15,21,21,21,21,-35,-41,-21,-20,21,21,21,21,-36,-7,-17,-29,-37,-14,21,21,21,21,-30,-16,]),'$end':([1,2,11,12,13,21,22,23,24,25,27,28,29,32,33,42,43,51,53,66,67,68,80,83,84,86,87,93,94,],[0,-1,-11,-12,-13,-39,-2,-3,-18,-19,-4,-5,-6,-9,-10,-38,-40,-8,-15,-41,-21,-20,-7,-17,-29,-37,-14,-30,-16,]),']':([2,11,12,13,21,22,23,24,25,27,28,29,32,33,42,43,51,53,66,67,68,69,72,73,77,80,81,82,83,84,86,87,91,92,93,94,],[-1,-11,-12,-13,-39,-2,-3,-18,-19,-4,-5,-6,-9,-10,-38,-40,-8,-15,-41,-21,-20,80,83,84,85,-7,87,88,-17,-29,-37,-14,93,94,-30,-16,]),'end':([2,11,12,13,21,22,23,24,25,27,28,29,32,33,42,43,51,53,66,67,68,78,80,83,84,86,87,93,94,],[-1,-11,-12,-13,-39,-2,-3,-18,-19,-4,-5,-6,-9,-10,-38,-40,-8,-15,-41,-21,-20,86,-7,-17,-29,-37,-14,-30,-16,]),'FLOAT':([3,4,5,6,8,9,10,17,18,19,21,24,25,26,30,31,34,35,36,42,43,44,45,46,47,48,50,52,57,58,59,60,61,62,66,67,68,70,71,],[24,24,24,24,24,24,24,24,24,24,24,-18,-19,24,24,24,24,24,24,24,-40,24,-25,-26,-27,-28,24,24,24,24,24,-22,-23,-24,-41,-21,-20,24,24,]),'VAR':([3,4,5,6,8,9,10,15,17,18,19,21,24,25,26,30,31,34,35,36,41,42,43,44,45,46,47,48,50,52,57,58,59,60,61,62,64,65,66,67,68,70,71,79,],[25,25,25,25,25,25,25,35,25,25,25,25,-18,-19,25,25,25,25,25,25,65,25,-40,25,-25,-26,-27,-28,25,25,25,25,25,-22,-23,-24,79,-35,-41,-21,-20,25,25,-36,]),'(':([3,4,5,6,8,9,10,17,18,19,21,24,25,26,30,31,34,35,36,42,43,44,45,46,47,48,50,52,57,58,59,60,61,62,66,67,68,70,71,],[26,26,26,26,26,26,26,26,26,26,26,-18,-19,26,26,26,26,26,26,26,-40,26,-25,-26,-27,-28,26,26,26,26,26,-22,-23,-24,-41,-21,-20,26,26,]),'[':([7,14,16,24,25,37,38,40,67,68,74,75,76,85,88,],[30,34,36,-18,-19,55,56,63,-21,-20,-32,-33,-31,89,90,]),'*':([23,24,25,27,28,29,31,32,33,37,39,43,49,50,51,52,53,54,66,67,68,69,70,76,81,82,],[45,-18,-19,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-20,45,45,45,45,45,]),'-':([23,24,25,27,28,29,31,32,33,37,39,43,49,50,51,52,53,54,66,67,68,69,70,76,81,82,],[46,-18,-19,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-20,46,46,46,46,46,]),'+':([23,24,25,27,28,29,31,32,33,37,39,43,49,50,51,52,53,54,66,67,68,69,70,76,81,82,],[47,-18,-19,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-20,47,47,47,47,47,]),'/':([23,24,25,27,28,29,31,32,33,37,39,43,49,50,51,52,53,54,66,67,68,69,70,76,81,82,],[48,-18,-19,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-20,48,48,48,48,48,]),'>':([24,25,39,54,67,68,],[-18,-19,60,60,-21,-20,]),'<':([24,25,39,54,67,68,],[-18,-19,61,61,-21,-20,]),'=':([24,25,39,54,67,68,],[-18,-19,62,62,-21,-20,]),')':([24,25,49,67,68,],[-18,-19,68,-21,-20,]),'and':([24,25,38,40,67,68,74,75,76,],[-18,-19,57,57,-21,-20,-32,57,-31,]),'or':([24,25,38,40,67,68,74,75,76,],[-18,-19,58,58,-21,-20,-32,-33,-31,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,55,56,63,64,89,90,],[1,72,73,77,78,91,92,]),'command':([0,1,55,56,63,64,72,73,77,78,89,90,91,92,],[2,22,2,2,2,2,22,22,22,22,2,2,22,22,]),'value':([3,4,5,6,8,9,10,17,18,19,21,26,30,31,34,35,36,42,44,50,52,57,58,59,70,71,],[23,27,28,29,31,32,33,37,39,39,43,49,50,51,52,53,54,66,67,69,70,39,39,76,81,82,]),'comparation':([18,19,57,58,],[38,40,74,75,]),'inc_value':([21,],[42,]),'operations':([23,27,28,29,31,32,33,37,39,43,49,50,51,52,53,54,66,67,69,70,76,81,82,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'operator':([39,54,],[59,71,]),'varlist':([41,],[64,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> command','program',1,'p_program0','Parser.py',70),
  ('program -> program command','program',2,'p_program1','Parser.py',74),
  ('command -> fd value','command',2,'p_forward','Parser.py',80),
  ('command -> bk value','command',2,'p_back','Parser.py',84),
  ('command -> rt value','command',2,'p_right','Parser.py',88),
  ('command -> lt value','command',2,'p_left','Parser.py',92),
  ('command -> setpos [ value value ]','command',5,'p_setpos','Parser.py',96),
  ('command -> setxy value value','command',3,'p_setxy','Parser.py',100),
  ('command -> setx value','command',2,'p_setx','Parser.py',104),
  ('command -> sety value','command',2,'p_sety','Parser.py',108),
  ('command -> home','command',1,'p_home','Parser.py',112),
  ('command -> pd','command',1,'p_pd','Parser.py',116),
  ('command -> pu','command',1,'p_pu','Parser.py',120),
  ('command -> setpencolor [ value value value ]','command',6,'p_setpencolor','Parser.py',134),
  ('command -> make VAR value','command',3,'p_make','Parser.py',141),
  ('command -> while [ value operator value ] [ program ]','command',9,'p_while','Parser.py',145),
  ('command -> repeat value [ program ]','command',5,'p_repeat','Parser.py',150),
  ('value -> FLOAT','value',1,'p_value','Parser.py',154),
  ('value -> VAR','value',1,'p_value','Parser.py',155),
  ('value -> ( value )','value',3,'p_value','Parser.py',156),
  ('value -> value operations value','value',3,'p_value','Parser.py',157),
  ('operator -> >','operator',1,'p_operator','Parser.py',167),
  ('operator -> <','operator',1,'p_operator','Parser.py',168),
  ('operator -> =','operator',1,'p_operator','Parser.py',169),
  ('operations -> *','operations',1,'p_operations','Parser.py',173),
  ('operations -> -','operations',1,'p_operations','Parser.py',174),
  ('operations -> +','operations',1,'p_operations','Parser.py',175),
  ('operations -> /','operations',1,'p_operations','Parser.py',176),
  ('command -> if comparation [ program ]','command',5,'p_if','Parser.py',180),
  ('command -> ifelse comparation [ program ] [ program ]','command',8,'p_ifelse','Parser.py',184),
  ('comparation -> value operator value','comparation',3,'p_comparation','Parser.py',188),
  ('comparation -> comparation and comparation','comparation',3,'p_comparation','Parser.py',189),
  ('comparation -> comparation or comparation','comparation',3,'p_comparation','Parser.py',190),
  ('varlist -> <empty>','varlist',0,'p_varlist','Parser.py',195),
  ('varlist -> VAR','varlist',1,'p_varlist','Parser.py',196),
  ('varlist -> varlist VAR','varlist',2,'p_varlist','Parser.py',197),
  ('command -> to STR varlist program end','command',5,'p_to','Parser.py',207),
  ('command -> STR inc_value','command',2,'p_callfunc','Parser.py',212),
  ('inc_value -> <empty>','inc_value',0,'p_inc_value','Parser.py',216),
  ('inc_value -> value','inc_value',1,'p_inc_value','Parser.py',217),
  ('inc_value -> inc_value value','inc_value',2,'p_inc_value','Parser.py',218),
]