from .errors import FatileWarning, CritcalWarning

class pointers:

    objects = {"unreg": {}}

    def __init__(s): ...
    def newPointer(s, object: any, tag: str, _type: type):
        if not _type in s.objects and _type != "unreg": s.objects[_type] = {}
        if tag in s.objects[_type]: FatileWarning(f"Attempt to overwrite pointer {tag}")
        s.objects[_type][tag] = object
    def getPointer(s, tag: str, _type: type):
        if not _type in s.objects:      CritcalWarning(f"Pointer type not added {_type}"); return "Error: 0"
        if not tag in s.objects[_type]: CritcalWarning(f"Pointer {tag} dosent exits in {_type}"); return "Error: 1"
        return s.objects[_type][tag]
    def derefPointer(s, tag: str, _type: type):
        if not _type in s.objects:      CritcalWarning(f"Pointer type not added {_type}"); return "Error: 0"
        if not tag in s.objects[_type]: CritcalWarning(f"Pointer {tag} dosent exits in {_type}"); return "Error: 1"
        del s.objects[_type][tag]
