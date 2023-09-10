
from pysource_codegen import generate
import pysource_codegen._codegen

import pathlib
import sys

workdir=pathlib.Path("work")
workdir.mkdir(exist_ok=True)


def before_compile(source):
    (workdir/"generated_code.py").write_text(source)

pysource_codegen._codegen.before_compile_hook=before_compile

code=generate(int(sys.argv[1]))

# store the result in a file because we have to support system crashes



try:
    compile(code,"<file>","exec")
except:
    sys.exit(1)


