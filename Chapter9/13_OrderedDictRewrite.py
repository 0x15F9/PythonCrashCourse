from collections import OrderedDict
glossary = OrderedDict()

glossary["Iteration"]   = "The act of looping"
glossary["Conditional"] = "The act of selecting"
glossary["Paradigm"]    = "Approach to reach a solution"

for k, v in glossary.items():
    print("{} : {}".format(k, v))
