try:
    pass
except:
    pass
finally:
    match name_1:
        case None:
            pass
name_1 | name_1

# output:
# python: Python/flowgraph.c:511: no_redundant_jumps: Assertion `0' failed.
