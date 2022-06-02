
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftADDSUBleftMULDIVADD BEC DIV DO ELSE END EQ GEQ GRTR ID IF LEQ LESS LPAR MUL NEQ NUM READ RPAR SEM SUB THEN WHILE WRITEProgram : StatementsStatements : StatementStatements : Statements SEM StatementStatement : If\n                 | While\n                 | Assignment\n                 | If_Else\n                 | Write\n                 | ReadIf : IF Comparison THEN Statements ENDIf_Else : IF Comparison THEN Statements ELSE Statements ENDWrite : WRITE ExpressionRead : READ IdWhile : WHILE Comparison DO Statements ENDAssignment : Id BEC ExpressionComparison : Expression Relation ExpressionRelation : EQ\n                | NEQ\n                | LESS\n                | LEQ\n                | GRTR\n                | GEQExpression : Expression ADD Expression\n                  | Expression SUB Expression\n                  | Expression MUL Expression\n                  | Expression DIV ExpressionExpression : LPAR Expression RPARExpression : NUMExpression : IdId : ID'
    
_lr_action_items = {'IF':([0,16,27,40,51,],[10,10,10,10,10,]),'WHILE':([0,16,27,40,51,],[11,11,11,11,11,]),'WRITE':([0,16,27,40,51,],[13,13,13,13,13,]),'READ':([0,16,27,40,51,],[14,14,14,14,14,]),'ID':([0,10,11,13,14,16,19,23,27,28,29,30,31,32,33,34,35,36,37,38,40,51,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,-17,-18,-19,-20,-21,-22,15,15,]),'$end':([1,2,3,4,5,6,7,8,9,15,20,21,24,25,26,41,44,45,46,47,48,50,52,54,],[0,-1,-2,-4,-5,-6,-7,-8,-9,-30,-28,-29,-12,-13,-3,-15,-23,-24,-25,-26,-27,-10,-14,-11,]),'SEM':([2,3,4,5,6,7,8,9,15,20,21,24,25,26,41,42,44,45,46,47,48,49,50,52,53,54,],[16,-2,-4,-5,-6,-7,-8,-9,-30,-28,-29,-12,-13,-3,-15,16,-23,-24,-25,-26,-27,16,-10,-14,16,-11,]),'END':([3,4,5,6,7,8,9,15,20,21,24,25,26,41,42,44,45,46,47,48,49,50,52,53,54,],[-2,-4,-5,-6,-7,-8,-9,-30,-28,-29,-12,-13,-3,-15,50,-23,-24,-25,-26,-27,52,-10,-14,54,-11,]),'ELSE':([3,4,5,6,7,8,9,15,20,21,24,25,26,41,42,44,45,46,47,48,50,52,54,],[-2,-4,-5,-6,-7,-8,-9,-30,-28,-29,-12,-13,-3,-15,51,-23,-24,-25,-26,-27,-10,-14,-11,]),'LPAR':([10,11,13,19,23,28,29,30,31,32,33,34,35,36,37,38,],[19,19,19,19,19,19,19,19,19,19,-17,-18,-19,-20,-21,-22,]),'NUM':([10,11,13,19,23,28,29,30,31,32,33,34,35,36,37,38,],[20,20,20,20,20,20,20,20,20,20,-17,-18,-19,-20,-21,-22,]),'BEC':([12,15,],[23,-30,]),'ADD':([15,18,20,21,24,39,41,43,44,45,46,47,48,],[-30,29,-28,-29,29,29,29,29,-23,-24,-25,-26,-27,]),'SUB':([15,18,20,21,24,39,41,43,44,45,46,47,48,],[-30,30,-28,-29,30,30,30,30,-23,-24,-25,-26,-27,]),'MUL':([15,18,20,21,24,39,41,43,44,45,46,47,48,],[-30,31,-28,-29,31,31,31,31,31,31,-25,-26,-27,]),'DIV':([15,18,20,21,24,39,41,43,44,45,46,47,48,],[-30,32,-28,-29,32,32,32,32,32,32,-25,-26,-27,]),'EQ':([15,18,20,21,44,45,46,47,48,],[-30,33,-28,-29,-23,-24,-25,-26,-27,]),'NEQ':([15,18,20,21,44,45,46,47,48,],[-30,34,-28,-29,-23,-24,-25,-26,-27,]),'LESS':([15,18,20,21,44,45,46,47,48,],[-30,35,-28,-29,-23,-24,-25,-26,-27,]),'LEQ':([15,18,20,21,44,45,46,47,48,],[-30,36,-28,-29,-23,-24,-25,-26,-27,]),'GRTR':([15,18,20,21,44,45,46,47,48,],[-30,37,-28,-29,-23,-24,-25,-26,-27,]),'GEQ':([15,18,20,21,44,45,46,47,48,],[-30,38,-28,-29,-23,-24,-25,-26,-27,]),'RPAR':([15,20,21,39,44,45,46,47,48,],[-30,-28,-29,48,-23,-24,-25,-26,-27,]),'THEN':([15,17,20,21,43,44,45,46,47,48,],[-30,27,-28,-29,-16,-23,-24,-25,-26,-27,]),'DO':([15,20,21,22,43,44,45,46,47,48,],[-30,-28,-29,40,-16,-23,-24,-25,-26,-27,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Program':([0,],[1,]),'Statements':([0,27,40,51,],[2,42,49,53,]),'Statement':([0,16,27,40,51,],[3,26,3,3,3,]),'If':([0,16,27,40,51,],[4,4,4,4,4,]),'While':([0,16,27,40,51,],[5,5,5,5,5,]),'Assignment':([0,16,27,40,51,],[6,6,6,6,6,]),'If_Else':([0,16,27,40,51,],[7,7,7,7,7,]),'Write':([0,16,27,40,51,],[8,8,8,8,8,]),'Read':([0,16,27,40,51,],[9,9,9,9,9,]),'Id':([0,10,11,13,14,16,19,23,27,28,29,30,31,32,40,51,],[12,21,21,21,25,12,21,21,12,21,21,21,21,21,12,12,]),'Comparison':([10,11,],[17,22,]),'Expression':([10,11,13,19,23,28,29,30,31,32,],[18,18,24,39,41,43,44,45,46,47,]),'Relation':([18,],[28,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Program","S'",1,None,None,None),
  ('Program -> Statements','Program',1,'p_program','ply-parser.py',273),
  ('Statements -> Statement','Statements',1,'p_statements_statement','ply-parser.py',277),
  ('Statements -> Statements SEM Statement','Statements',3,'p_statements_statements','ply-parser.py',281),
  ('Statement -> If','Statement',1,'p_statement','ply-parser.py',287),
  ('Statement -> While','Statement',1,'p_statement','ply-parser.py',288),
  ('Statement -> Assignment','Statement',1,'p_statement','ply-parser.py',289),
  ('Statement -> If_Else','Statement',1,'p_statement','ply-parser.py',290),
  ('Statement -> Write','Statement',1,'p_statement','ply-parser.py',291),
  ('Statement -> Read','Statement',1,'p_statement','ply-parser.py',292),
  ('If -> IF Comparison THEN Statements END','If',5,'p_if','ply-parser.py',296),
  ('If_Else -> IF Comparison THEN Statements ELSE Statements END','If_Else',7,'p_if_else','ply-parser.py',300),
  ('Write -> WRITE Expression','Write',2,'p_write','ply-parser.py',304),
  ('Read -> READ Id','Read',2,'p_read','ply-parser.py',308),
  ('While -> WHILE Comparison DO Statements END','While',5,'p_while','ply-parser.py',312),
  ('Assignment -> Id BEC Expression','Assignment',3,'p_assignment','ply-parser.py',316),
  ('Comparison -> Expression Relation Expression','Comparison',3,'p_comparison','ply-parser.py',320),
  ('Relation -> EQ','Relation',1,'p_relation','ply-parser.py',324),
  ('Relation -> NEQ','Relation',1,'p_relation','ply-parser.py',325),
  ('Relation -> LESS','Relation',1,'p_relation','ply-parser.py',326),
  ('Relation -> LEQ','Relation',1,'p_relation','ply-parser.py',327),
  ('Relation -> GRTR','Relation',1,'p_relation','ply-parser.py',328),
  ('Relation -> GEQ','Relation',1,'p_relation','ply-parser.py',329),
  ('Expression -> Expression ADD Expression','Expression',3,'p_expression_binary','ply-parser.py',333),
  ('Expression -> Expression SUB Expression','Expression',3,'p_expression_binary','ply-parser.py',334),
  ('Expression -> Expression MUL Expression','Expression',3,'p_expression_binary','ply-parser.py',335),
  ('Expression -> Expression DIV Expression','Expression',3,'p_expression_binary','ply-parser.py',336),
  ('Expression -> LPAR Expression RPAR','Expression',3,'p_expression_parenthesis','ply-parser.py',340),
  ('Expression -> NUM','Expression',1,'p_expression_num','ply-parser.py',344),
  ('Expression -> Id','Expression',1,'p_expression_id','ply-parser.py',348),
  ('Id -> ID','Id',1,'p_id','ply-parser.py',352),
]
