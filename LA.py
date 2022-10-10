import nltk  # For tokenization
import re # For regular expression


# file opening
def file(): 
    f = open('file.txt')
    prog = f.read()
   # print('original',prog)
    return prog
    #f.close() # would be added in the clear button function

# Removing whitespaces
def removespaces(prog):
    #prog="".join(prog.split()) This apparoach can also be used
    prog=prog.translate(prog.maketrans('', '', ' \n\t\r'))
    return prog

# removing comments    
def removecomments(prog):
# re.sub returns a string where all matching occurrences of the specified pattern are replaced by the replace string.
    Multi_Removed = re.sub("/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", prog)
    Single_Removed = re.sub("//.*", "", Multi_Removed)
    return Single_Removed

# checking keywords
def checkKeyword(prog):
    RE_Keywords = "auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|string|class|struc|include|main|iostream|conio|using|namespace|std"
    if(re.search(RE_Keywords, str(prog))):
        return True
    else:
        return False

# checking identifiers
def checkIdentifier(prog):
    RE_Identifier = r"^[a-zA-Z_]+[a-zA-Z0-9_]*"
    if(re.match(RE_Identifier, prog)):
        return True
    else:
        return False

# checking constants
def checkConstants(prog):
    #print('kahao jello bello bp jello ', str(prog))
    RE_Numerals = "^(\d+)$"
    if(re.match(RE_Numerals, prog)):
        return True
    else:
        return False

# checking operators
def checkOperators(prog):
    RE_Operator = "(\++)|(-)|(=)|(\*)|(/)|(%)|(--)|(<=)|(>=)"

    if(re.match(RE_Operator, prog)):
        return True
    else:
        return False

# checking symbols
def checkSymbols(prog):
    RE_Operator = "@|#|$|_|,|!|'||'|"

    if(re.match(RE_Operator, prog)):
        return True
    else:
        return False

obj=file()
objC=file()
space_remo=''
comment_remo=''
keyword=[]
identifier=[]
constant=[]
operator=[]
symbol=[]
       
space_remo=removespaces(obj)    
comment_remo=removecomments(obj)

def start():
    #space_remo=removespaces(obj)    
    #comment_remo=removecomments(space_remo)
    tokens = nltk.word_tokenize(comment_remo)
    for i,token in enumerate(tokens):
        #print(i,token)
        tokenC=nltk.wordpunct_tokenize(token)
        print(i,tokenC)
        for i,token in enumerate(tokenC):
            if(checkKeyword(token)):
                keyword.append(token)
            elif(checkIdentifier(token)):   
                identifier.append(token)
            elif(checkConstants(token)):
                constant.append(token)  
            elif(checkOperators(token)):   
                operator.append(token)        
            elif(checkSymbols(token)):   
                symbol.append(token)
            