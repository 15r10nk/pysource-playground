try:
    match name_0:
        case name_1 if {}:
            pass
except* name_1:
    pass
finally:
    from . import name_2 as name_2

# output:
# python: Python/flowgraph.c:511: no_redundant_jumps: Assertion `0' failed.
