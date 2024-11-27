###File Handling
### 1 - Read the file and remove equal lines (if any).
#
with open("1.py", "r") as file:
    lines = file.readlines()
unic_lines = set(lines)
with open("1.py", "w") as file:
    file.writelines(unic_lines)
with open("1.py", "r") as file:
    processed_lines = file.readlines()
    for line in processed_lines:
        print(line)

### 2 - Print out all words with length of n-characters
n = 4   #should be specified lenght of the word
with open("1.py", "r") as file:
    lines = file.readlines()
for l in lines:
    words = l.split()
    for word in words:
        if len(word) == n:
            print(word)

    ##### 3 - Combine two files into a third file
with open("1.py", "r") as file1:
    content1= file1.read()
with open("2.py", "r") as file2:
    content2= file2.read()
with open("3.py", "w+") as file3:
    content3 = content1+content2
print(content3)


#### Regular Expressions

"""
Define if a string contains the required characters. E.g. if '7865serS3' includes '583' - True; '973' - False
Count a number of Upper case letters in the string. E.g. '7865serS3' - 'Number of Capital letters: 1'
Define if the string contains at least one Upper case letter followed by Lower case letters. E.g. '75serS3' - False; '75WseTrS3' - True;
"""