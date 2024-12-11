from errors import CritcalWarning

class expect:
    def strict(value, _type):
        if not isinstance(value, _type): CritcalWarning(f"value isnt an instance of {_type} its {type(value)}"); return False
        return True
    def jsLike(value, _type):
        try: return [True, _type(value)]
        except: CritcalWarning(f"value cant be an instance of {_type}"); return [False, value]