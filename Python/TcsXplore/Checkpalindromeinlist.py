'''reate a function with the name check_palindrome which takes a list of strings as input. The function checks each string of the list whether it is a palindrome or not and returns another list containing the palindrome from the input string.

Note:

i. A palindrome is a a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam
ii. The check for the string to be palindrome should be case-insensitive , e.g. madam and Madam both should be considered as palindrome.
You can use the below sample input and output to verify your solution.

Sample Input:
3
Hello
Malayalam
Radar

Output:

Malayalam
Radar

The first line in the sample input is the count of strings to be included in the list as the 1st input.
The strings are then provided one by one as the next lines of input.
For more details, please refer to the below main section of code
You can use the below sample main section to test your code.

Sample Main Method:

if __name__=='__main__':
         count=int(input())
         inp_str=[]
         for i in range(count):
                 inp_str.append(input())
         output=check_palindrome(inp_str)
         if len(output)!=0:
                 for i in output:
                         print(i)
         else:
                 print('No palindrome found')'''




def check_palindrome (l1):

    output=[]

    for i in l1:
        j=i[::-1]
         if (i)==(j):
            output.append(i)
        else:
            pass
    return output








if __name__=='__main__':
         count=int(input())
         inp_str=[]
         for i in range(count):
                 inp_str.append(input())
         output=check_palindrome(inp_str)
         if len(output)!=0:
                 for i in output:
                         print("Output: ",i)
         else:
                 print('No palindrome found')



