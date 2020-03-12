list_tohoku = [5349, 5478, 5344, 4644, 4968, 6259]
list_shikoku = [3148, 2991, 2966, 2457]

avg_tohoku = 0

for val in list_tohoku:
    #print(val)
    avg_tohoku += val

avg_tohoku /= len(list_tohoku)

avg_shikoku = 0

for val in list_shikoku:
    avg_shikoku += val

avg_shikoku /= len(list_shikoku)

print(avg_tohoku)
print(avg_shikoku)

dict_tohoku = {'aomori':5349, 'akita':4644, 'sendai':5344,'yamagata':4968, 'hukushima':6259, 'morioka':5478}

avg_tohoku = 0

for val in dict_tohoku:
    #print(val)
    avg_tohoku += dict_tohoku[val]

avg_tohoku /= len(dict_tohoku)
print(avg_tohoku)
