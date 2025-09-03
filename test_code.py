import sys
import pathlib
import ast

source=pathlib.Path(sys.argv[1]).read_text()


ast.parse(source,type_comments=True)
ast.parse(source,type_comments=False)

compile(source,"<file>","exec")

import ast

tree = ast.parse(source)
for node in ast.walk(tree):
    if hasattr(node,"lineno"):
        del node.lineno
        del node.end_lineno
        del node.col_offset
        del node.end_col_offset

tree=ast.fix_missing_locations(tree)
print(tree)
print(ast.dump(tree,annotate_fields=True,include_attributes=True))

compile(tree, "<file>", "exec")

