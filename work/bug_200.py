class name_1[**name_0]:
    try:

        class name_3[name_3](name_4=name_0):
            name_0
    except {name_0} as name_5:
        from name_4 import name_0
    else:
        pass
    finally:
        pass

# output:
# Traceback (most recent call last):
#   File "/home/frank/projects/pysource-playground/test_code.py", line 6, in <module>
#     compile(source,sys.argv[1],"exec")
# SystemError: compiler_lookup_arg(name='name_0') with reftype=3 failed in <generic parameters of name_3>; freevars of code name_3: ('.type_params', 'name_0')
