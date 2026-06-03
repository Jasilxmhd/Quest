
'vehicle number'

import re
# with open('regex_practice_dataset.txt','r+')as f:
#     # print(f.read())
#     data = f.read()

#     vehicel_number = re.findall(r'\w{2}-\d{2}-\w{2}-\d{4}',data)
#     print(vehicel_number)






'IP address'

with open('regex_practice_dataset.txt','r+')as f:
    # print(f.read())
    data = f.read()

    ip = re.findall(r'\d{,3}\.\d{,3}\.\d{,3}\.\d{,2}',data)
    for i in ip:
        print(i)
    print()
