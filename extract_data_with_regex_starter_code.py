import re 
# uncomment the following line of code and fill in 
phoneNumRegex =re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d')

example = "The number is 123-456-7890."
#my shortcut
"""alt=re.findall("[0-9]",example)
print(alt,type(alt))"""

# uncomment the following line of code and fill in result =
result =phoneNumRegex.search(example)
print(result)

# uncomment the following lines of code and fill in 
if result:
    print("Phone number found:", result.group())
    print("Area code:", result.group()[0:3])