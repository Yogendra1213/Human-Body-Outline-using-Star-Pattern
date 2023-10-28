# print("       * *   ")
# print("     * ' ' *")
# print("     *     *")
# print("       * *  ")
# print("        *")
# print("      * * *")
# print("    *   *   *")
# print("   *    *    *")
# print("  *     *     *")
# print("        *")
# print("       * *")
# print("      *   *")
# print("     *     *")
# print("    *       *")

# Head Part
for i in range(2):
    for j in range(8-2*i):
        print(" ", end = '')
    print("*", end = '')
    for j in range(4*i+1):
        print(" ", end = '')
    print("*", end = '')
    print('')

for i in range(1, -1, -1):
    for j in range(8-2*i):
        print(" ", end = '')
    print("*", end = '')
    for j in range(4*i+1):
        print(" ", end = '')
    print("*", end = '')
    print('')

# Neck
for i in range(9):
    print(" ", end = '')
print('*')

#Body and Arms
for i in range(5):
    for j in range(8-i):
        print(' ', end= '')
    print('*', end = '')
    for k in range(i):
        print(' ', end = '')
    print("*", end = '')
    for k in range(i):
        print(' ', end = '')
    print("*", end = '')
    print('')
for i in range(9):
    print(" ", end = '')
print('*')

# Legs
for i in range(5):
    for j in range(8-i):
        print(' ', end = '')
    print('*', end = '')
    for k in range(2*i+1):
        print(' ', end = '')
    print("*", end = '')
    print('')