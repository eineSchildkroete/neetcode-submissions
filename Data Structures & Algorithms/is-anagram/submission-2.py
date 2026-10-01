class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc = dict()
        tc = dict()

        if len(s) == len(t):

            for cs, ct in zip(s, t):
                sc[cs] = sc.get(cs, 0) + 1
                tc[ct] = tc.get(ct, 0) + 1

            if sc == tc:
                return True
            else:
                return False
        else:
            return False