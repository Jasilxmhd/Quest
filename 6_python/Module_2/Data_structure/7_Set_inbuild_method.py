
'issubset()'


# set1 = { 1,2,3,4,5}
# set2 = { 4,5,6,7,8}

# set3 = {1}                            # True
# set3 = {2,8}                            # False
# set3 = {2,1,5}                            # True


# print(set3.issubset(set1))






'issuperset()'


# set1 = { 1,2,3,4,5}
# set2 = { 4,5,6,7,8}

# set3 = { 1,2,3}                   # True
# set3 = {2,8}                        # False
# set3 = {2,1,5}                          # True

# print(set1.issuperset(set3))











set1 = { 1,2,3,4,5}
set2 = { 4,5,6,7,8}

set3 = { 1,2,3}                   # True
set3 = {2,8}                        # False
set3 = {2,1,5}                          # True

print(set1.isdisjoint(set3))










