if __name__ == '__main__':
    source = input("source=")
    target = input("target=")

    source_index = 0
    target_index = 0
    res = 0
    find = False

    while target_index < len(target):
        if target[target_index] not in source:
            res = -1
            find = False
            break
        find = False
        while source_index < len(source):
            if source[source_index] == target[target_index]:
                source_index += 1
                find = True
                break
            source_index += 1
        if source_index == len(source) and not find:
            res += 1
            source_index = 0
        else:
            target_index += 1

    if find:
        res += 1
    print(res)

