import ast


testList = ["so","much","wow"]
print testList
convert = str(testList)
print convert

wow = ast.literal_eval(convert)
print wow

assert(isinstance(wow,list))

