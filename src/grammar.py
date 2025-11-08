GRAMMAR = r"""
OP_PLUS : "+"
OP_MINUS : "-"
OP_MUL : "*"
OP_DIV : "/"
OP_MOD : "%"
OP_POW : "^"
NUM : /-?([1-9]+[0-9]*|0)\.?[0-9]*/

?expr : sum "="
sum : mul (OP_PLUS mul | OP_MINUS mul)*
mul : pow (OP_MUL pow | OP_DIV pow | OP_MOD pow)*
pow : primary (OP_POW pow)?
?primary : NUM | "(" sum ")"

%ignore "\n" | "\r"| " "
"""
