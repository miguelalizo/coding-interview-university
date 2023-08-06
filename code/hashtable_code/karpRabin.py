class KarpRabin():
    """
    Implements the Karp-Rabin algorithm for substring lookup 
    """
    def __init__(self, p=257, base=256):
        self.p=p
        self.base=base


    @staticmethod
    def _compare(s: str, t: str) -> bool:
        """
        Char by char comparison of s and t, returns True if strings are equal.
        Assumes equal length strings

        Parameters
        ----------
        s: str
            String to compare against t
        t: str
            String to compare against s

        Rreturns
        --------
        bool
            Returns True if strings are the same, False otherwise
        """
        for i in range(0, len(s)):
            if s[i] != t[i]:
                return False
        return True


    def search(self, s: str, t: str) -> int:
        """
        Return the starting index of a substring s if found in t

        Parameters
        ----------
        s: str
            Substring to be looked up in t
        t: str
            String to be searched

        Returns
        -------
        idx: int
            Starting index of the substring match or -1 if no match
        """
        if len(t)<len(s):
            return -1
        if KarpRabin._compare(s, t[0:len(s)]):
            return 0
        if len(s) == len(t):
            return -1
    

        # Compute hash functions
        hash_s=0
        for c in s:
            hash_s = (hash_s*self.base + ord(c))%self.p

        k=1
        rhash_st=0
        for c in t[0:len(s)]:
            rhash_st = (rhash_st*self.base + ord(c))%self.p
            # (self.base^len(s))%self.p but performed with intermediate %self.p to avoid int overflow
            k=(k*self.base)%self.p

        for i in range(0, len(t)-len(s)):
            rhash_st = ((self.base*(rhash_st))%self.p + ord(t[i+len(s)]) - (ord(t[i])*k))%self.p
            if hash_s==rhash_st:
                if (KarpRabin._compare(s, t[i+1:i+len(s)+1])):
                    return i+1
        return -1



