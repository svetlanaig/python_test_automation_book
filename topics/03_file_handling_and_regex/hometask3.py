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
# 1 - Define if a string contains the required characters.
import re
def check_string(x, y):
    return all(re.search(a, y) for a in x)
result1 = check_string('583', '7865serS3')
result2 = check_string('973', '7865serS3')
if result1:
    print(f'Found: {result1}')
else:
    print("Not all characters were found")
if result2:
    print(result2)
else:
    print("Not all characters were found")

# 2 - Count a number of Upper case letters in the string. E.g. '7865serS3' - 'Number of Capital letters: 1'

my_pattern = '[A-Z]'
my_string = '7865serS3IO'
import re
result = re.findall(my_pattern, my_string)
capital_letters=len(result)
print(f'number of pattern in the string {capital_letters}')

# 3 Define if the string contains at least one Upper case letter followed by Lower case letters. E.g. '75serS3' - False; '75WseTrS3' - True;

my_pattern = '[A-Z][a-z]'
my_string1 = '75serS3'
my_string2 = '75WseTrS3'
import re
result1 = re.search(my_pattern, my_string1)
result2 = re.search(my_pattern, my_string2)
print(result1)
print(result2)
