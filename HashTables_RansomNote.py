""" Hash Tables: Ransom Note """
from collections import Counter

def checkMagazine(magazine, note):
    flag = True
    c1 = Counter(magazine)
    c2 = Counter(note)
    for k,v in c2.items():
        if k in c1 and c1[k] >= v: # e.g. is "two":1 >= "two":2 ? --> NO
            continue
        else:            
            flag = False
            break
    if flag:
        print('Yes')
    else:
        print('No')
        
""" Alternative """
def checkMagazine2(magazine, note):
    c1 = Counter(magazine)
    c2 = Counter(note)
    if c2 - c1 == {}: # if all keys of c2 are present in c1 == {}
        print('Yes')
    else:
        print('No')

""" Testing """
magazine = "ive got a lovely bunch of coconuts"
note = "ive got some coconuts"

magazine = "give me one grand today night"
note = "give one grand today"

magazine = "two times three is not four"
note = "two times two is four"

magazine = magazine.rstrip().split()
note = note.rstrip().split()

checkMagazine(magazine,note)
checkMagazine2(magazine,note)