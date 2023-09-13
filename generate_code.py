
from pysource_codegen import generate
import pysource_codegen._codegen

import pathlib
import sys

workdir=pathlib.Path("work")
workdir.mkdir(exist_ok=True)
out_file=workdir/"generated_code.py"

def before_compile(source):
    out_file.write_text(source)

pysource_codegen._codegen.before_compile_hook=before_compile

code=generate(int(sys.argv[1]))

# store the result in a file because we have to support system crashes
out_file.write_text(code)

compile(code,out_file,"exec")


