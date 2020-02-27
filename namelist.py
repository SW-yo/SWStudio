blog_file = "C:\\GameOn\\1003b_jpn\\Chatlog\\blog_log.txt"
name_list = "C:\\GameOn\\1003b_jpn\\Chatlog\\name_list.txt"

name_set = set()

with open(blog_file) as log:
    for line in log:
        name = line[7:].split(":")[0]
        name_set.add(name)

with open(name_list, "w") as lst:
    for name in name_set:
        lst.write(name + "\n")