class name_0:
    type name_2 = lambda: name_5

# output:
# Traceback (most recent call last):
#   File "/home/frank/projects/pysource-playground/test_code.py", line 6, in <module>
#     compile(source,sys.argv[1],"exec")
#   File "work/bug_417.py", line 2
#     type name_2 = lambda: name_5
#                   ^^^^^^^^^^^^^^
# SyntaxError: Cannot use lambda in annotation scope within class scope
