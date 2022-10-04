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


obj=file()
#removespaces(obj)    
removecomments(obj)
#tokens = nltk.word_tokenize(prog)
    