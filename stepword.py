
global wordlist
global letters
global ans
global possible_letters
global alphabet
alphabet={'a':1,'b':1,'c':2,'d':1,'e':1,'f':2,'g':1,'h':2,'i':1,'j':3,'k':3,'l':2,'m':2,'n':1,'o':1,'p':2,'q':2,'r':1,'s':1,'t':1,'u':1,'v':2,'w':2,'x':3,'y':2,'z':3}
possible_letters=[]
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
    
def inputletter():
    global letters
    letters=raw_input("type your leters in lowercase (for Qu type qu):")
   
    letters="".join(sorted(letters))
    print letters

def create_possible_letters():
    global possible_letters
    split_letters=letters.split()
    l=len(split_letters)
    for i in range(0,2**len(letters)):
        possible_letters[i]=letters
        
            
    
def findword():
    global letters
    global ans
    ans=[]
    i=0
    found=False
    for key in wordlist:
        i=0
        j=0
        check=True
        
        while check:
            if j==len(letters) or i==len(key):
                if i==len(key):
                    found=True
                    ans.append(wordlist[key])
                check=False
            if not check: break
            if key[i] == letters[j] and j!=len(letters):
                i+=1
            j+=1
            
    if found: print ans
    else: print "Not found %d"%len(letters)

def makescore():
    maxscore=0
    for word in ans:
        sumscore=0
        for i in word:
            sumscore+=alphabet[i]
        if sumscore>maxscore:
            maxscore=sumscore
            best_ans=word
        
    print "%s : score %d"%(best_ans,maxscore)


sortdict()
while True:
    inputletter()
    findword()
    makescore()



# hw1
