
fileName = "notes.txt"

#f.readlines() reads all lines
#f.readline() reads one line
#for line in f:
#    print(line, end='')   reads all lines 1 by 1
#f.tell() returns where are you in the file
#f.seek(x) goes to the x position in the file


def getBeginOfNotes(sourceFile):
    '''(file) -> list
    This function reads the file and figure out how many note there are
    '''
    file.seek(0)                            #just in case, fix pointer position
    beginOfNotes = [0]                      #first line always begins at 0
    posCounter = 0
    for line in file:
        for i in line:
            if i == '\n':
                beginOfNotes.append(posCounter+1)  #next position is the beginning of next note
            posCounter = posCounter + 1
    beginOfNotes.pop()                      #remove the last one cause it is eof
    file.seek(0)                            #leave the pointer at the begining
    return beginOfNotes


#first try to open if there is existing file
#if not, then create a new one
try:
    file = open(fileName, "r+")  
                
except FileNotFoundError:
    print("No saved notes found; if it is not expected, check notes.txt file is in correct directory")
    file = open("notes.txt", "a+")

#get line beginning positions to know where to write new data
lineBeginningsPos = getBeginOfNotes(file)

#ask user action
selection = input("1: New note\n2: Edit note\n3: Delete note\n0: Exit\n")
if selection == '1':
    newNote = input("Type your note and press Enter\n") #new line added to go second line in the txt
    file.seek(0,2)          #go to end of the file
    file.write(newNote)


print("YOUR NOTES\n")
file.seek(0)
for line in file:
    print(line, end='')








file.close()
