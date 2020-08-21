"""
# *args: multiple arguments, writable things or lists of writable things
"""
def listWriter(*args, fileName="file", fileExtension="txt", separator="-", commentChar="--"):
    separationString = ""
    if separator != None and separator != "":
        separationString = "\n" + commentChar + " "
        for value in range(10):
            separationString += separator
    f = open(fileName + "." + fileExtension, "wt")
    index = 0
    for value in args:
        if type(value) is list:
            for item in value:
                f.write(str(item))
                f.write(str(separationString))
        else:
            f.write(value)
            f.write(separationString)
        index += 1
    f.close()

def readListFile(fileName, commentChar):
    try:
        f = open(fileName, "r")
    except:
        return False
    lines = []
    for x in f:
        txt = ""
        try:
            if x.index(commentChar) != 0:
                txt = x.rstrip("\n")
                lines.append(txt)
        except Exception as e:
            txt = x.rstrip("\n")
            lines.append(txt)
    f.close()
    return lines

def readDictFile(fileName, commentChar="#", separationChar="="):
    try:
        f = open(fileName, "r")
    except:
        return False
    lines = {}
    for x in f:
        txt = None
        try:
            if x.index(commentChar) != 0:
                txt = x.rstrip("\n")
        except Exception as e:
            txt = x.rstrip("\n")
        if txt != None:
            sep = txt.split(separationChar, 1)
            if len(sep) > 1:
                lines[sep[0]] = sep[1]
            else:
                lines[sep[0]] = sep[0]
    f.close()
    return lines
