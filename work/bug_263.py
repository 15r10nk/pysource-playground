class name_0[name_2]:
    (name_2 := name_1)

    def name_5[*name_4]() -> name_2: # type: ignoresome text
        name_2

# output:
# Traceback (most recent call last):
#   File "/home/frank/projects/pysource-playground/test_code.py", line 6, in <module>
#     compile(source,sys.argv[1],"exec")
# SystemError: compiler_lookup_arg(name='name_2') with reftype=3 failed in <generic parameters of name_5>; freevars of code name_5: ('name_2',)
