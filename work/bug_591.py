try:
    pass
except* name_1:
    pass
finally:
    match name_4:
        case _ if name_3:
            pass
(name_3,)

# output:
# python: Python/flowgraph.c:511: no_redundant_jumps: Assertion `0' failed.
