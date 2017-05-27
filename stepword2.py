import itertools

global wordlist
global letters
global ans
global alphabet
global possible_letters
global best_ans

best_ans=[]
possible_letters=[]
alphabet={'a':1,'b':1,'c':2,'d':1,'e':1,'f':2,'g':1,'h':2,'i':1,'j':3,'k':3,'l':2,'m':2,'n':1,'o':1,'p':2,'q':2,'r':1,'s':1,'t':1,'u':1,'v':2,'w':2,'x':3,'y':2,'z':3}
wordlist = {}
letters=""
ans=[]

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
    print ans


    if 'q' in letters:
        u_in_letters=letters.count("u")
        for word in ans:
            if u_in_letters-1<word.count("u") and 'q'not in word :
                ans.remove(word)
            

def makescore():
    maxscore=0
    global best_ans
    best_ans[:]=[]
    for word in ans:
        sumscore=0
        for i in word:
            sumscore+=alphabet[i]
        if sumscore>maxscore:
            maxscore=sumscore
            best_ans.append(word)
            
    "Choose the longest anagram"
    best_ans=sorted(best_ans,key=lambda x:len(x),reverse=True)
                
    print "Best answer is %s | score %d"%(best_ans[0],(maxscore+1)**2)

sortdict()
while inputletter():
    
    create_possible_letters()
    findword()
    makescore()



