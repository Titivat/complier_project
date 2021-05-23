
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADDITION ASSIGNMENT DIVISION EQUAL ERR EXPONENT GREATER_THAN GREATER_THAN_EQUAL INT I_DIVISION LESS_THAN LESS_THAN_EQUAL LPAREN MULTIPLICATION NOT_EQUAL NUM RPAREN SUBTRACTION VARs : VAR ASSIGNMENT expr\n         | exprexpr : expr op1 term1\n            | term1term1 : term1 op2 term2\n             | term2term2 : term2 op3 term3\n             | term3term3 : factor EXPONENT term3\n             | factorfactor : NUM\n              | VAR\n              | LPAREN expr RPARENop1 : EQUAL\n           | NOT_EQUAL\n           | GREATER_THAN\n           | GREATER_THAN_EQUAL\n           | LESS_THAN\n           | LESS_THAN_EQUALop2 : ADDITION\n           | SUBTRACTIONop3 : MULTIPLICATION\n           | DIVISION\n           | I_DIVISION'
    
_lr_action_items = {'VAR':([0,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[2,27,27,27,-14,-15,-16,-17,-18,-19,27,-20,-21,27,-22,-23,-24,27,]),'NUM':([0,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[8,8,8,8,-14,-15,-16,-17,-18,-19,8,-20,-21,8,-22,-23,-24,8,]),'LPAREN':([0,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[9,9,9,9,-14,-15,-16,-17,-18,-19,9,-20,-21,9,-22,-23,-24,9,]),'$end':([1,2,3,4,5,6,7,8,27,28,29,30,31,32,33,],[0,-12,-2,-4,-6,-8,-10,-11,-12,-1,-3,-5,-7,-9,-13,]),'ASSIGNMENT':([2,],[10,]),'EXPONENT':([2,7,8,27,33,],[-12,25,-11,-12,-13,]),'MULTIPLICATION':([2,5,6,7,8,27,30,31,32,33,],[-12,22,-8,-10,-11,-12,22,-7,-9,-13,]),'DIVISION':([2,5,6,7,8,27,30,31,32,33,],[-12,23,-8,-10,-11,-12,23,-7,-9,-13,]),'I_DIVISION':([2,5,6,7,8,27,30,31,32,33,],[-12,24,-8,-10,-11,-12,24,-7,-9,-13,]),'ADDITION':([2,4,5,6,7,8,27,29,30,31,32,33,],[-12,19,-6,-8,-10,-11,-12,19,-5,-7,-9,-13,]),'SUBTRACTION':([2,4,5,6,7,8,27,29,30,31,32,33,],[-12,20,-6,-8,-10,-11,-12,20,-5,-7,-9,-13,]),'EQUAL':([2,3,4,5,6,7,8,26,27,28,29,30,31,32,33,],[-12,12,-4,-6,-8,-10,-11,12,-12,12,-3,-5,-7,-9,-13,]),'NOT_EQUAL':([2,3,4,5,6,7,8,26,27,28,29,30,31,32,33,],[-12,13,-4,-6,-8,-10,-11,13,-12,13,-3,-5,-7,-9,-13,]),'GREATER_THAN':([2,3,4,5,6,7,8,26,27,28,29,30,31,32,33,],[-12,14,-4,-6,-8,-10,-11,14,-12,14,-3,-5,-7,-9,-13,]),'GREATER_THAN_EQUAL':([2,3,4,5,6,7,8,26,27,28,29,30,31,32,33,],[-12,15,-4,-6,-8,-10,-11,15,-12,15,-3,-5,-7,-9,-13,]),'LESS_THAN':([2,3,4,5,6,7,8,26,27,28,29,30,31,32,33,],[-12,16,-4,-6,-8,-10,-11,16,-12,16,-3,-5,-7,-9,-13,]),'LESS_THAN_EQUAL':([2,3,4,5,6,7,8,26,27,28,29,30,31,32,33,],[-12,17,-4,-6,-8,-10,-11,17,-12,17,-3,-5,-7,-9,-13,]),'RPAREN':([4,5,6,7,8,26,27,29,30,31,32,33,],[-4,-6,-8,-10,-11,33,-12,-3,-5,-7,-9,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'s':([0,],[1,]),'expr':([0,9,10,],[3,26,28,]),'term1':([0,9,10,11,],[4,4,4,29,]),'term2':([0,9,10,11,18,],[5,5,5,5,30,]),'term3':([0,9,10,11,18,21,25,],[6,6,6,6,6,31,32,]),'factor':([0,9,10,11,18,21,25,],[7,7,7,7,7,7,7,]),'op1':([3,26,28,],[11,11,11,]),'op2':([4,29,],[18,18,]),'op3':([5,30,],[21,21,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> s","S'",1,None,None,None),
  ('s -> VAR ASSIGNMENT expr','s',3,'p_start',' syntacticanalyzer.py',62),
  ('s -> expr','s',1,'p_start',' syntacticanalyzer.py',63),
  ('expr -> expr op1 term1','expr',3,'p_expr',' syntacticanalyzer.py',71),
  ('expr -> term1','expr',1,'p_expr',' syntacticanalyzer.py',72),
  ('term1 -> term1 op2 term2','term1',3,'p_term1',' syntacticanalyzer.py',81),
  ('term1 -> term2','term1',1,'p_term1',' syntacticanalyzer.py',82),
  ('term2 -> term2 op3 term3','term2',3,'p_term2',' syntacticanalyzer.py',91),
  ('term2 -> term3','term2',1,'p_term2',' syntacticanalyzer.py',92),
  ('term3 -> factor EXPONENT term3','term3',3,'p_term3',' syntacticanalyzer.py',101),
  ('term3 -> factor','term3',1,'p_term3',' syntacticanalyzer.py',102),
  ('factor -> NUM','factor',1,'p_factor',' syntacticanalyzer.py',111),
  ('factor -> VAR','factor',1,'p_factor',' syntacticanalyzer.py',112),
  ('factor -> LPAREN expr RPAREN','factor',3,'p_factor',' syntacticanalyzer.py',113),
  ('op1 -> EQUAL','op1',1,'p_op1',' syntacticanalyzer.py',121),
  ('op1 -> NOT_EQUAL','op1',1,'p_op1',' syntacticanalyzer.py',122),
  ('op1 -> GREATER_THAN','op1',1,'p_op1',' syntacticanalyzer.py',123),
  ('op1 -> GREATER_THAN_EQUAL','op1',1,'p_op1',' syntacticanalyzer.py',124),
  ('op1 -> LESS_THAN','op1',1,'p_op1',' syntacticanalyzer.py',125),
  ('op1 -> LESS_THAN_EQUAL','op1',1,'p_op1',' syntacticanalyzer.py',126),
  ('op2 -> ADDITION','op2',1,'p_op2',' syntacticanalyzer.py',143),
  ('op2 -> SUBTRACTION','op2',1,'p_op2',' syntacticanalyzer.py',144),
  ('op3 -> MULTIPLICATION','op3',1,'p_op3',' syntacticanalyzer.py',153),
  ('op3 -> DIVISION','op3',1,'p_op3',' syntacticanalyzer.py',154),
  ('op3 -> I_DIVISION','op3',1,'p_op3',' syntacticanalyzer.py',155),
]
