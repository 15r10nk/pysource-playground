class name_3:

    class name_2[*name_1](lambda: name_3):
        pass

# output:
# Traceback (most recent call last):
#   File "/home/frank/projects/pysource-playground/test_code.py", line 6, in <module>
#     compile(source,sys.argv[1],"exec")
#   File "work/bug_107.py", line 3
#     class name_2[*name_1](lambda: name_3):
#                           ^^^^^^^^^^^^^^
# SyntaxError: Cannot use lambda in annotation scope within class scope
