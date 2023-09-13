
# playground for pysource-codegen/pysource-minimize

This repository contains some script to test pysource-minimize and pysource-codegen.
The current use case is to find bugs in cpython 3.12, pysource-codegen and pysource-minimize tools.


# setup:

``` bash
git submodule update --init
/path/to/python3.12 -m venv venv
source venv/bin/activate
python -m pip install -r requirements
```

# usage:

search for bugs and store them in `work/`
``` bash
python find_issue.py --help
python find_issue.py --num 500 # search 500 seeds
```




# open issues

It is possible that pysource-codegen generates SyntaxErrors.
I am working on a complete refactoring of pysource-codegen which should solve most of the issues.



