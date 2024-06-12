
from pysource_codegen import generate
import pathlib
import sys


out_file=pathlib.Path(sys.argv[2])

code=generate(int(sys.argv[1]),depth_limit=9)

# store the result in a file because we have to support system crashes
out_file.write_text(code)


