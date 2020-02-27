ini_path = "C:\\GameOn\\1003b_jpn\\Chatlog\\"
blog_file = "C:\\GameOn\\1003b_jpn\\Chatlog\\blog_log.txt"
friend_voice = "C:\\GameOn\\1003b_jpn\\Chatlog\\voice_log.txt"

list_name = input("リストの名前を入れてください：")

list_path = ini_path + list_name + ".txt"

name_set = set()

with open(list_path) as name_file:
    for name in name_file:
        name_set.add(name.rstrip("\n"))

voice = open(friend_voice, "w")    

with open(blog_file) as blog:
    for blog_line in blog:
        name = blog_line[7:].split(":")[0]
        if name in name_set:
            voice.write(blog_line)

voice.close()