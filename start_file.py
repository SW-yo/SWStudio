data = ['1,2,3\n', '4,5,6\n', '7,8,9\n']
test_file = open('test_start.txt', 'w')
test_file.writelines(data)
test_file.close()

test_file = open('test_start.txt', 'r')
for line in test_file:
    temp_list = line.strip().split(',')
    output_line = '\t'.join(temp_list)
    print(output_line)
test_file.close()