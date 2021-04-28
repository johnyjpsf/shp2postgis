import datetime

def getVersion():
    return "0.3.0"

def listWriter(*args, fileName="file", fileExtension="txt", separator="-", commentChar="--", mode='wt'):
    separationString = ""
    if separator != None and separator != "":
        separationString = "\n" + commentChar + " "
        for value in range(10):
            separationString += separator
    f = open(fileName + "." + fileExtension, mode)
    index = 0
    for value in args:
        if type(value) is list:
            for item in value:
                f.write(str(item))
                f.write(str(separationString))
        else:
            try:
                f.write(value)
            except Exception as e:
                linha = ''
                test_file = open("test_file_" + str(datetime.datetime.now()) + ".txt", "wt")
                for letra in value:
                    try:
                        test_file.write(letra)
                    except Exception as e:
                        print(e)
                        # print("caracter com problema: " + letra)
                    else:
                        linha += letra
                test_file.close()
                try:
                    f.write(linha)
                except Exception as e:
                    raise e
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

def log(string, path):
    f = open(path, 'at')
    f.write("(" + str(datetime.datetime.now()) + "): " + string + "\n")
    f.close()
