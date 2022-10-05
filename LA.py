from asyncio import constants
import nltk  # For tokenization
import re    # For regular expressions

# file opening
def file(): 
    f = open('file.txt')
    prog = f.read()
   # print('original',prog)
    return prog
    f.close()

def removespaces(prog):
    #prog="".join(prog.split()) This apparoach can also be used
    prog=prog.translate(prog.maketrans('', '', ' \n\t\r'))
    print('inside removespace'+prog)
    
def removecomments(prog):
# re.sub returns a string where all matching occurrences of the specified pattern are replaced by the replace string.
    print(prog)
    Multi_Removed = re.sub("/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", prog)
    print('Comments removed',Multi_Removed)
    Single_Removed = re.sub("//.*", "", Multi_Removed)
    print('Comments removed',Single_Removed)

def checkKeyword(prog):
    RE_Keywords = "auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|string|class|struc|include|main|iostream|conio"
    if(re.match(RE_Keywords, str(prog))):
        return True
    else:
        return False

def checkIdentifier(prog):
    RE_Identifier = r"^[a-zA-Z_]+[a-zA-Z0-9_]*"
    if(re.match(RE_Identifier, prog)):
        return True
    else:
        return False

def checkConstants(prog):
    RE_Numerals = "^(\d+)$"
    if(re.match(RE_Numerals, prog)):
        return True
    else:
        return False

def checkOperators(prog):
    RE_Operator = "(\++)|(-)|(=)|(\*)|(/)|(%)|(--)|(<=)|(>=)"

    if(re.match(RE_Operator, prog)):
        return True
    else:
        return False

    
obj=file()
#removespaces(obj)    
#removecomments(obj)

tokens = nltk.word_tokenize(obj)

keyword=[]
identifier=[]
constant=[]
operator=[]

for i,token in enumerate(tokens):
    #print(i,token)
    if(checkKeyword(token)):
        keyword.append(token)
    elif(checkIdentifier(token)):   
        identifier.append(token)
    elif(checkConstants(token)):   
        constant.append(token)  
    elif(checkOperators(token)):   
        constant.append(token)        

print('identifiers', identifier)
print('keyword', keyword)
print('Contants', constant)
print('Operators', operator) 

# 
#identifier(tokens)
#print(tokens)
#tokens = nltk.word_tokenize(prog)
    