# if __name__ == '__main__':
#     arr = [[52.0, 'Test1'], [53.0, 'Test2'], [53.0, 'Test3']]
#
#     arr.sort()
#     print(arr)
#
#     index = 0
#     secondLowest = 0
#     p = 0
#     while p < len(arr) - 1:
#         if arr[p][0] < arr[p + 1][0]:
#             index = p + 1
#             secondLowest = arr[p + 1][0]
#             break
#
#         p += 1
#
#     print(arr[index][1])
#
#     index += 1
#     while index < len(arr):
#         if arr[index][0] == secondLowest:
#             print(arr[index][1])
#         else:
#             break
#
#         index += 1

def count_substring(string, sub_string):
    counter = 0

    for x in range(0, len(string)):
        if string[x] == sub_string[0]:
            if string[x:x+3].find(sub_string) != -1:
                counter += 1

    return counter

print(count_substring("ABCDCDC", "CDC"))
