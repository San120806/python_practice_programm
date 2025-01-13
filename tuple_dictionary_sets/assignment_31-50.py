# # List Operations
# lst=[1,2,3,5,6]
# print("initial list: ",lst)
# lst.append(4)
# print("after append:",lst)
# lst.insert(3,8)
# print("after insert:",lst)
# lst.remove(1)
# print("after remove:",lst)
# lst.pop()
# print("after pop:",lst)

# # Maximum and Minimum in a List
# lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
# print("Maximum:", max(lst))
# print("Minimum:", min(lst))

# # Second Largest Element
# lst = list(map(int, input("Enter unique numbers separated by spaces: ").split()))
# lst.sort()
# print("Second Largest:", lst[-2])

# # Sum and Average of a List
# lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
# print("Sum:", sum(lst))
# print("Average:", sum(lst) / len(lst))

# # Count Positive, Negative, Zero
# lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
# pos = sum(1 for x in lst if x > 0)
# neg = sum(1 for x in lst if x < 0)
# zero = sum(1 for x in lst if x == 0)
# print(f"Positive: {pos}, Negative: {neg}, Zero: {zero}")

# # Remove Duplicates from a List
# lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
# print("List without duplicates:", list(set(lst)))

# # Concatenate Two Lists
# lst1 = list(map(int, input("Enter first list (space-separated): ").split()))
# lst2 = list(map(int, input("Enter second list (space-separated): ").split()))
# print("Concatenated List:", lst1 + lst2)

# #  List Reversal
# lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
# lst.reverse()
# print("Reversed List:", lst)

# # Find Common Elements of Two Lists
# lst1 = list(map(int, input("Enter first list (space-separated): ").split()))
# lst2 = list(map(int, input("Enter second list (space-separated): ").split()))
# print("Common Elements:", list(set(lst1) & set(lst2)))

# # Element-wise Sum of Two Lists
# lst1 = list(map(int, input("Enter first list (space-separated): ").split()))
# lst2 = list(map(int, input("Enter second list (space-separated): ").split()))
# print("Element-wise Sum:", [x + y for x, y in zip(lst1, lst2)])

# # Tuple Creation and Access
# tup = ("apple", "kiwi", "chikoo")
# index = int(input("Enter the index: "))
# print(f"Element at index {index} is {tup[index]}")

# # tuple to list
# tup= tuple(map(int,input("enter the tuple elemnts(space-seperated):").split()))
# lst=list(tup)
# lst.append(100)
# tup=tuple(lst)
# print("modified tuple: ",tup)

# # Check if Element Exists in Tuple
# m=("sanu","panu","tanu","aachu")
# elemnt=input("enter the element to check: ")
# print(f"{elemnt} exists in tuple : {elemnt in m}")

# # Dictionary: Word Count
# text = input("Enter a string: ")
# words = text.split()
# word_count = {word: words.count(word) for word in set(words)}
# print("Word Count:", word_count)

# # Dictionary: Student Grades
# grades = {"Alice": 90, "Bob": 85, "Charlie": 95}
# name = input("Enter the student's name: ")
# print(f"{name}'s grade: {grades.get(name, 'Not found')}")

# #  Dictionary: Keys and Values
# z = {"a": 1, "b": 2, "c": 3}
# print("Keys:", list(z.keys()))
# print("Values:", list(z.values()))

# # Merge Two Dictionaries
# m1 = {"a": 1, "b": 2}
# m2 = {"c": 3, "d": 4}
# merged = {**m1, **m2}
# print("Merged Dictionary:", merged)

# # Invert Dictionary
# e= {"a": 1, "b": 2, "c": 3}
# inverted = {v: k for k, v in e.items()}
# print("Inverted Dictionary:", inverted)

# # Set Operations
# lst1 = list(map(int, input("Enter first list (space-separated): ").split()))
# lst2 = list(map(int, input("Enter second list (space-separated): ").split()))
# set1, set2 = set(lst1), set(lst2)
# print("Union:", set1 | set2)
# print("Intersection:", set1 & set2)
# print("Difference (set1 - set2):", set1 - set2)

# # Set Membership Testing
# names = {"Alice", "Bob", "Charlie"}
# name = input("Enter a name: ")
# print(f"{name} is in the set: {name in names}")












