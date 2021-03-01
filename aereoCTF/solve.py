fd = open("dump", "r")

section = fd.read()[0x13A9:0x172A]

print(section)
