try:
    raise Exception ("NAME", "Address")
except Exception as e:
    print("Type of instance : ", type(e))
    print("Argumnet of instance : ", e.args) # arguments stored in .args
    print("Instance print : ", e) # __str__ allows args to be printed directly,but may be overridden in exception subclasses
    a,b = e.args # unpack args
    print("a : ",a)
    print("b : ",b)