import itertools

global wordlist
global letters
global ans
global alphabet
global possible_letters

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
        word=word.rstrip()
    	wordlist.update({"".join(sorted(word)).rstrip():word.rstrip()})
    f.close()
    print wordlist
    print "Dictionary prepared"
    
def inputletter():
    global letters
    letters=raw_input("type your leters in lowercase (for Qu type qu):")
   
    letters="".join(sorted(letters))
    print letters

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
            ans.append(wordlist[word])
    print ans
            

def makescore():
    maxscore=0
    best_ans=""
    for word in ans:
        sumscore=0
        for i in word:
            sumscore+=alphabet[i]
        if sumscore>maxscore:
            maxscore=sumscore
            best_ans=word
        
    print "Best answer is %s | score %d"%(best_ans,maxscore)


sortdict()

while True:
    inputletter()
    create_possible_letters()
    findword()
    makescore()


