class name_2[*name_0]:
    match something:
        case {**name_4}:
            name_0 = name_3 # type: ignoresome text
    with name_0: # type: ignoresome text

        class name_2[name_5](name_0):
            name_0

# output:
# Traceback (most recent call last):
#   File "/home/frank/projects/pysource-playground/test_code.py", line 6, in <module>
#     compile(source,sys.argv[1],"exec")
# SystemError: compiler_lookup_arg(name='name_0') with reftype=3 failed in <generic parameters of name_2>; freevars of code name_2: ('.type_params', 'name_0')
