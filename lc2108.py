def productExceptSelf(words):
    reversed_words = [word[::-1] for word in words]

    for i in range(len(words)):
        if words[i] == reversed_words[i]:
            return words[i]
    return ""

words = ["def","ghi"]
productExceptSelf(words)
print(productExceptSelf(words))