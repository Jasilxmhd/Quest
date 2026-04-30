"""replace()"""

# s="Python Django"
# s="Python Django Django Django"
# print(s)


# update=s.replace('D','d')                     #Python django
# update=s.replace('Django','Development')      #Python Development

# update=s.replace(' ','_')                      #Python_Django_Django_Django
# update=s.replace('Django','Development',2)     #Python Development Development Django.  //change first 2

# print(update)

"""strip()"""
# string="     hello django        "
# print(string)
# print(string.strip())

# string="--------hello django--------"
# print(string.strip('-'))

# string="0000000hello django00000000"
# print(string.strip('0'))

# string="aaaaaaa hello django aaaaaa"
# print(string)
# print(string.strip('a'))

# string="abcabcabc hello django aaaaaa"
# print(string)
# print(string.strip('abc'))


"""lstrip()"""
# # remove lefts

# string="abcabcabc hello django aaaaaa"
# print(string)
# print(string.lstrip('abc'))


"""rstrip()"""
# remove rights
# string="aaaaaaaa hello django aaaaaa"
# print(string)
# print(string.rstrip('abc'))


"""removeprefix()"""
# left to right
# name='Mr.jasil'
# print(name.removeprefix('Mr.'))
# print(name.removeprefix('m'))


"""removesuffix()"""
# right to left

# name='Mr.jasil'
# print(name.removesuffix('Mr.'))
# print(name.removesuffix('il'))

name='Mr.jasil Mr.'
print(name.removesuffix('Mr.'))