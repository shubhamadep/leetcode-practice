class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if not word or not abbr:
            return False
        
        word_len = len(word)
        
        if str(word_len) == abbr:
            return True
        
        wordp = 0
        abbrp = 0
        
        while wordp < len(word) and abbrp < len(abbr):
            
            if abbr[abbrp].isdigit():
                
                if abbr[abbrp] == '0':
                    return False
                
                numb = 0
                while abbrp < len(abbr) and abbr[abbrp].isdigit():
                    numb = (numb * 10) + int(abbr[abbrp])
                    abbrp +=1
                    
                wordp += numb
            else:
                
                if word[wordp] != abbr[abbrp]:
                    return False
                
                wordp += 1
                abbrp += 1
        
        
        return len(word) == wordp and len(abbr) == abbrp
                
                    