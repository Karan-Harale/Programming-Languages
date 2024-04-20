# def sumod(n,k):
#     def tbk(number,base):
#         if number==0:
#             return[0]
#         digits=[]
#         while number>0:
#             print("n= ",number%base)
#             digits.insert(0,number%base)
#             print(digits)
#             print("number= ",number)
#             number//=base
#             print("number= ",number)
#         return digits

#     digitsk=tbk(n,k)
#     sumk=sum(digitsk)
#     return sumk
#
# n=123
# k=5
# result=sumod(n,k)
# print(result)

#
# def sumBase(n, k):
#     stri = ""
#     while True:
#         if n < k:
#             break
#         div = int(n // k)
#         stri += str(n % k)
#         n = div
#     stri += str(n)
#     stri = stri[::-1]
#     lst = [int(x) for x in stri]
#     return (sum(lst))
#
#

# def sumBase( n, k):
#     ans = 0
#     while n:
#         ans += n % k
#         print("ans= ", ans)
#         n //= k
#         print("n/= ",n )
#     return ans
# n=123
# k=5
# result=sumBase(n,k)
# print(123//5)

# # def max_divisible_by_90(cards):
#   """
#   Finds the largest possible number divisible by 90 that can be made from the given cards.
#
#   Args:
#     cards: A list of integers representing the digits on the cards.
#
#   Returns:
#     The largest possible number divisible by 90 that can be made from the cards, or -1 if no such number exists.
#   """

a=5
b=2
c=10

i=a>b
print(i)