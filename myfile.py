#BANANA

def minion_game(S):
    import re
    v_score = 0
    c_score= 0
    for x in range(1,len(S)+1):
        for part in set([S[p:p+x] for p in range(len(S)-x+1)]):
            
            if re.findall("^[AEIOU]*", part) != ['']:
                v_score += len([S[x:x+len(part)] for x in range(len(S)) if S[x:x+len(part)]==part])
            else:
                c_score += len([S[x:x+len(part)] for x in range(len(S)) if S[x:x+len(part)]==part])
    
    return f"Kevin {v_score}" if v_score > c_score else f"Stuart {c_score}"


print(minion_game("BANANA"))
