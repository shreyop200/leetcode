class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for ch in ransomNote:
            if magazine.count(ch) < ransomNote.count(ch):
                return False
        return True