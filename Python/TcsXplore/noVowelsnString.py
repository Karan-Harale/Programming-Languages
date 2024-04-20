'''Q.1
Create a function with the name find_Novowels which takes a list of strings as input. The function checks each string of the list whether it has at least one vowel or not and returns another list containing the strings not having any vowel.

Note:
The check for the vowel should be case-insensitive .
You can use the below sample input and output to verify your solution.

Sample Input:

4
almost
vtyw
sound
prtwy

Output:
Strings without vowels:
vtyw
prtwy


The first line in the sample input is the count of strings to be included in the list to be passed to the method find_Novowels .
The strings are then provided one by one as the next lines of input.
For more details, please refer to the below main section of code
You can use the below sample main section to test your code.

Sample Main Method:
if __name__=='__main__':
        count=int(input())
        inp_str=[]
        for i in range(count):
                inp_str.append(input())
        output=find_Novowels(inp_str)
        if len(output)!=0:
                print('Strings without vowels:')
                for i in output:
                        print(i)
        else:
                print('No string found')'''


#Answer:->
def find_Novowels(inp_str):
    result=[]
    b='aeiou'

    print(set(b))
    for i in inp_str:
        j=i.lower()
        # print(set(j) & set(b))
        if len(set(j)&set(b))==0:
            result.append(i)
    return result

#Sample main section.
# #Do not remove the below portion of code.
if __name__=='__main__':
    count=int(input())
    inp_str=[]
    for i in range(count):
        inp_str.append(input())
        output=find_Novowels(inp_str)
        if len(output)!=0:
            print('Strings without vowels:')
            for i in output:
                print(i)
        else:
            print('No string found')