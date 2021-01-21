paranoid_android = "Marvin, the Paranoid Android"
leters = list(paranoid_android)
for char in leters[:6]:
    print('\t', char)
print()
for char in leters[-7:]:
    print('\t'*2, char)
print()
for char in leters[12:20]:
    print('\t'*3, char)
