# def palindrome(word,index):
#     if word==word[::-1]:
#         return (f"{word} is a palindrome")
#     else:
#         return (f"{word} is not a palindrome")
#
#
#
# print(palindrome("abcba", 0))
# print(palindrome("peter", 0))


def palindrome(word,index):
    if index==len(word)//2:
        return f'{word} is a palindrome'

    left=word[index]
    right=word[len(word)-index-1]

    if left!=right:
        return (f"{word} is not a palindrome")

    return palindrome(word,index+1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
