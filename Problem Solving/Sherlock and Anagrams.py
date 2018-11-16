def sherlockAndAnagrams(s):
    subs = []
    count = 0
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            subs.append(sorted(s[i:j+1]))
            
    for i in range(len(subs)):
        count += subs.count(subs[i]) -1
    
    return count//2
