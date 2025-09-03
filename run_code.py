from multiprocessing import get_context

import sys
import subprocess as sp
import pathlib
import textwrap
import argparse
import shutil
import re
import os
import random
import ast

curdir = pathlib.Path(__file__).parent
extra_path = [str(curdir / "pysource-codegen"), str(curdir / "pysource-minimize/src")]

sys.path += extra_path


os.environ["PYTHONPATH"] = (
    os.environ.get("PYTHONPATH", "") + os.pathsep + os.pathsep.join(extra_path)
)

from pysource_codegen import generate

class AddTryCatch(ast.NodeTransformer):

        def __init__(self):
            self.loop_number=0

        def visit(self, stmt):
            if isinstance(stmt, (ast.Import, ast.ImportFrom)):
                return ast.Pass()
            if isinstance(stmt, ast.stmt):
                result=self.generic_visit(stmt)

                if isinstance(result, (ast.While, ast.For)):
                    result.body = [
                            ast.Expr(
                        ast.Call(
                            func=ast.Name(id="loop_limit"),
                            args=[ast.Constant(value=self.loop_number)],
                            keywords=[],
                        )),

                        *result.body,
                    ]
                    self.loop_number += 1

                if isinstance(result,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)):
                    result.decorators=[]

                result=ast.Try(
                    body=[result],
                    handlers=[
                        ast.ExceptHandler(
                            type=ast.Name(id="BaseException", ctx=ast.Load()),
                            name="e",
                            body=ast.parse("report_error(e)").body,
                        )
                    ],
                )

            else:
                result = self.generic_visit(stmt)


            return result

def test_seed(seed):

    print(f"test seed {seed}")

    code = generate(seed=seed)

    tree = ast.parse(code)
    tree = AddTryCatch().visit(tree)


    footer="\nfor i in range(1000):\n"
    for n in range(8):
        for arg_count in range(8):
            args=", ".join("Generic()" for n in range(arg_count))

            footer+=f"""
    try:
        name_{n}({args})
        # print("called name_{n}({args})",i)
    except:
        pass
"""

    code = pathlib.Path("header.py").read_text() + ast.unparse(tree)+footer

    pathlib.Path("crash.py").write_text(code)

    print("run")
    sp.run([sys.executable,"crash.py"],check=True)


for seed in range(327,1000):
    test_seed(seed)
