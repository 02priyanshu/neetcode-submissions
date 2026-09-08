class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        for i in strs:
            s = s + "__" + "".join(i)
        return s

    def decode(self, s: str) -> List[str]:
        decode = [x for x in s.split("__") ]
        return decode[1:]
