# def my_abs(arg) :
#     if (arg < 0) :
#         result = arg * -1
#     else:
#         result = arg
#     return result
#
# output = my_abs()
# print(output)

def print_personnel(name, position='staff', nationality='korea') :
    print('name = {0}'.format(name))
    print('name = {0}'.format(position))
    print('name = {0}'.format(nationality))

print_personnel(name='이소정')
print_personnel(name='이소정', nationality='usa')
print_personnel('이소정', position='학생')