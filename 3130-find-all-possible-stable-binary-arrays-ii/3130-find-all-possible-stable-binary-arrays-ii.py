class Solution:
    def numberOfStableArrays(self, z: int, o: int, l: int) -> int:
        f = cache(lambda q,p:q>0 and (f(q-1,p)+f(p,q-1)-f(p,q-1-l) if p else q<=l))
        res = f(z,o)+f(o,z)
        f.cache_clear()
        return res%(10**9+7)