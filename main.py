'''
write a  python program to calculate vowels in a given string ?
'''
print("guvi geeks private limited")

data =input("enter a string:")
count = 0
# iterate over the string
for data in data:
    if data == 'a'or data == 'u'or data =='e'or data =='i'or data =='o':
        count = count + 1

#print the total vowels in a string:
        print ("number of vowels in the string : ",count) 




'''
creat a pyramid of numbers from 1 to 20
'''           
for i in range(21):
    print(i)


    
'''
function to remove vowels
'''
str =input("enter string")
vowel_string="aeiouAEIPOU"

print("input string",str)

for char in str:
    if char in vowel_string:
        str=str.replace(char, "")

print("output string without vowels",str) 




'''
define a function to the number of unique characters in a string:
'''

string='guvi technology'
count=0
temp=[]
for i in string:
    if(i not in temp):
        count+=1
        temp.append(i)
print('Total Unique Characters count:',count)    
    


