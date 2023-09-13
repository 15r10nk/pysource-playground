name_2
global name_5, name_2

# output:
# Traceback (most recent call last):
#   File "/home/frank/projects/pysource-playground/test_code.py", line 6, in <module>
#     compile(source,sys.argv[1],"exec")
#   File "work/bug_276.py", line 2
#     global name_5, name_2
#     ^^^^^^^^^^^^^^^^^^^^^
# SyntaxError: name 'name_2' is used prior to global declaration
