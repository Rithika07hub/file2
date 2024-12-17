user1 = input("Enter name1: ")
user2 = input("Enter name2: ")
user1 = user1.lower().replace(" ", "")
user2 = user2.lower().replace(" ", "")
for char in user1[:]:  
    if char in user2:
        user1 = user1.replace(char, "", 1)
        user2 = user2.replace(char, "", 1)
tot = len(user1) + len(user2)
l = list("FLAMES")
while len(l) > 1:
    ind = (tot % len(l)) - 1
    if ind >= 0:
        l = l[ind + 1 :] + l[:ind]  
    else:
        l.pop()  # Remove the last element if ind == -1
relationship = {
    "F": "Friends",
    "L": "Love",
    "A": "Affection",
    "M": "Marriage",
    "E": "Enemies",
    "S": "Siblings",
}
print("The relationship is:", relationship[l[0]])

  
