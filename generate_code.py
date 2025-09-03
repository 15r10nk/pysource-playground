
from pysource_codegen import generate
from pysource_codegen._codegen import generate_ast
import pathlib
import sys
import ast


out_file=pathlib.Path(sys.argv[2])

# ast_file=pathlib.Path("ast_out.py")

# tree=generate_ast(int(sys.argv[1]),depth_limit=13) 

# ast_file.write_text(
# f"""
# from ast import *
# tree={ast.dump(tree,indent=2)}

# compile(ast.unparse(tree),"file","exec")
# """
# )

code=generate(int(sys.argv[1]),depth_limit=13)

#store the result in a file because we have to support system crashes
out_file.write_text(code)


