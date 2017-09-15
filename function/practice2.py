def sequential_search(str, key):
    count = 0
    while count < len(str):
        if str[count] == key:
            return count
        else:
            count += 1
    return 0

print(sequential_search("개구리고양이", "개"))
print(sequential_search("개구리고양이", "구"))
print(sequential_search("개구리고양이", "리"))
print(sequential_search("개구리고양이", "고"))
print(sequential_search("개구리고양이", "양"))
print(sequential_search("개구리고양이", "이"))
print(sequential_search("개구리고양이", "말"))
