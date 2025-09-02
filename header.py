
class Generic:
    def __init__(self):
        self.stop_iter=False

    def __iter__(self):
        yield Generic()
        yield Generic()

    def __aiter__(self):
        return Generic()

    def __anext__(self):
        if self.stop_iter:
            raise StopIteration()
        else:
            self.stop_iter=True
        return Generic()

    def __call__(self,*a,**ka):
        return Generic()

    def __getitem__(self,key):
        return Generic()

    def __setitem__(self,key,value):
        pass

    def __getattr__(self,name):
        return Generic()

    def __setattr__(self,name,value):
        pass



for i in range(10):
    globals()[f"name_{i}"]=Generic()


def loop_limit(name,cache={}):
    if name not in cache:
        cache[name]=5

    if cache[name]==0:
        raise RuntimeError("break long loop")
    else:
        cache[name]-=1

def report_error(e,reported=[]):

    s=f"{type(e).__name__} {e}"
    if s in reported:
        return
    reported.append(s)
    print("catch error:",s)


