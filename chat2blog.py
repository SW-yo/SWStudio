chat_file = "C:\\GameOn\\1003b_jpn\\Chatlog\\chat_log.txt"
blog_file = "C:\\GameOn\\1003b_jpn\\Chatlog\\blog_log.txt"

raw_file = open(chat_file, "r")
c2b_file = open(blog_file, "w")

for line in raw_file:
    blog_line = line[26:]
    c2b_file.write(blog_line)

raw_file.close()
c2b_file.close()
