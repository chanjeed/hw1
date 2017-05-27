import itertools

global ans
global wordlist
global letters
global alphabet
global possible_letters
ans=[]
possible_letters=[]
alphabet={'a':1,'b':1,'c':2,'d':1,'e':1,'f':2,'g':1,'h':2,'i':1,'j':3,'k':3,'l':2,'m':2,'n':1,'o':1,'p':2,'q':2,'r':1,'s':1,'t':1,'u':1,'v':2,'w':2,'x':3,'y':2,'z':3}
wordlist = {}
letters=""

def sortdict():
    
    f = open("dict.txt","r")
    "print f.read()"
    for word in f:
        word=word.lower()
        sortedword="".join(sorted(word))
        sortedword=sortedword.strip("\n")
        if wordlist.has_key(sortedword):
            wordlist[sortedword]=wordlist[sortedword]+" "+word.strip("\n")
        else:
            wordlist.update({sortedword:word.strip("\n")})
    f.close()
    print wordlist
    print "Dictionary prepared"
    
def inputletter():
    global letters
    letters=raw_input("type your leters in lowercase (for Qu type qu)['stop' for exit]:")
    if letters=='stop':
        return 0
    letters="".join(sorted(letters))
    return 1

def create_possible_letters():
    global possible_letters
    possible_letters[:]=[]
    for i in range (3,len(letters)+1):
        possible_letters+= list(itertools.combinations(letters,i))
    
    for i in range(0,len(possible_letters)):
        possible_letters[i]=" ".join(sorted(possible_letters[i]))
        possible_letters[i]=possible_letters[i].replace(" ","")


    
def findword():
    global ans
    ans[:]=[]
    for word in possible_letters:
        if (word in wordlist) and (wordlist[word] not in ans) :
            ans=ans+wordlist[word].split(" ")

    if 'q' in letters:
        u_in_letters=letters.count('u')-letters.count('q')
        for i in range(0,len(ans)):

            if ( ans[i].count('u')-ans[i].count('q')) > u_in_letters and ('u' in ans[i]):
                ans[i]='0'
    ans=list(filter(lambda x:x!='0',ans))
    ans.sort(key=len,reverse=True)
    print ans
            

def makescore():
    best_index=0
    maxscore=0
    l=len(ans)
    for i in range(0,l):
        sumscore=0
        for c in ans[i]:
            sumscore+=alphabet[c]
        if sumscore>maxscore:
            maxscore=sumscore
            best_index=i
    print "Best answer is %s | score %d"%(ans[best_index],(maxscore+1)*(maxscore+1))
    

sortdict()
while inputletter():
    
    create_possible_letters()
    findword()
    makescore()
    
                



