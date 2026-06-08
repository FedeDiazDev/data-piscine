def NULL_not_found(object: any) -> int:
    obj_type = type(object).__name__
    if obj_type == "NoneType":
        print(f"Nothing : {type(object)}")
        return 0
    elif obj_type == "float" and object != object:
        print(f"Cheese : {type(object)}")
        return 0
    elif obj_type == "int" and object == 0:
        print(f"Zero : {type(object)}")
        return 0
    elif obj_type == "bool" and object is False:
        print(f"Fake : {type(object)}")
        return 0
    elif obj_type == "str" and object == "":
        print(f"Empty : {type(object)}")
        return 0
    else:
        print("Type not found")
    return 1
