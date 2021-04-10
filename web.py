


def csscomp(args):
    full = []
    for i in range(len(args)):
        
        full.append(args[i] + "; ")
    return(''.join(full))

def properties(args):
    full = []
    for i  in range(len(args)):
        full.append(args[i] + " ")
    return(''.join(full))
def element(type,css = [], content = "", props=[], runCompilecss = True):
    if runCompilecss == True:
        full = "<" + type + " " + properties(props) + 'style="' + csscomp(css) + '">' + content + "</" + type + ">"
    else:
        full = "<" + type + " " + properties(props) + 'style="' + css + '">' + content + "</" + type + ">"
    return(full)
def cssDark():
    return(csscomp(["background-color: rgb(68, 68, 68)", "padding-left: 20px", "margin-left: 25px", "color: rgb(190, 190, 190)", "text-shadow: 0 4px 2px -2px rgb(135, 134, 131)", "box-shadow: 0 4px 2px -2px rgb(135, 134, 131)"]))

def compileSite(code=[], headcode=[], filename="index"):
    codefile = open(str(filename) + ".html", 'a+')
    codelist = []
    for i in range(len(code)):
        codelist.append(code[i])
        codelist.append("\n")
    headcodelist = []
    for i in range(len(headcode)):
        headcodelist.append(headcode[i])
        headcodelist.append("\n")
    codefile.write("<!DOCTYPE html>\n<html>\n<head>\n" + ''.join(headcodelist) + "\n</head>\n<body>\n" + ''.join(codelist) + "\n</body>\n</html>")
    codefile.close()

