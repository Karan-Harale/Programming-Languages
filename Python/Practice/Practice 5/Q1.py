hindidict={
    "Pankha":"fan",
    "dabba":"box",
    "vastu":"item"

}
print("options are",hindidict.keys())
a=input("Enter the hindi World\n ")

# print("The meaning of Your Word is:", hindidict[a])#this line gives an keyerror when Word is not in dict

# below line not gives any Error it gives value none
print("The meaning of Your Word is:", hindidict.get(a))