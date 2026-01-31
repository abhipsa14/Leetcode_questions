class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        s=""
        for i in range(0,len(letters)):
            if ord(target)<ord(letters[i]):
                s=letters[i]
                break
        if s != "":
            return s
        else:
            return letters[0]
                
        