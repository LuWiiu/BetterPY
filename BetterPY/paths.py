from .errors import infoWarning, ErrorWarning, CritcalWarning
from .expectType import expect
from .wrappers import expectFunc

class pathing:

    paths = {}

    @expectFunc
    def addPath(name: str, pathHeadID: str, isFile: bool):
        if not expect.strict(name, str): CritcalWarning (f"name is'nt str its {type(name)}"); return 0
        if not expect.strict(pathHeadID, str): ErrorWarning(f"path is'nt str its {type(pathHeadID)}")
        if   isFile: pathing.paths[name] = pathing.paths[pathHeadID] + name
        elif isFile: pathing.paths[name] = pathing.paths[pathHeadID] + f"{name}\\"
        return [pathing.paths[name], str]

    def delPath(name: str):
        if not expect.strict(name, str): infoWarning (f"name is'nt str its {type(name)}")
        if not name in pathing.paths: CritcalWarning(f"{name} is'nt in paths!"); return 0
        del pathing.paths[name]

    def getFilePath(_file_= __file__):
        FilePath = _file_.split('\\')
        FilePath.pop()
        return "\\".join(FilePath) + '\\'
    @expectFunc
    def getPath(name: str):
        if not name in pathing.paths: CritcalWarning(f"{name} is'nt in paths!"); return 0
        return[pathing.paths[name], str]

    def setRoot(path: str):
        pathing.paths["root"] = pathing.getFilePath(path)

if __name__ == "__main__":
    pathing.addPath("hi.txt", "root", True)
    a = pathing.getPath("hi.txt")
    b = open(a).read()
    print(b)
