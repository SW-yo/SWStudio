import glob

file_list = glob.glob("C:\\GameOn\\1003b_jpn\\Chatlog\\*.txt")
chat_file = "C:\\GameOn\\1003b_jpn\\Chatlog\\chat_log.txt"

chat = open(chat_file, "w")

chat_set = set()

select_kind = input("どのチャット？(1:ch,2:ハバチャ,3:密,6:討伐):")
start_date = input("いつからのログ？(yy/mm/dd)：")

for file_name in file_list:
    try:
        with open(file_name, "r" ,errors='ignore') as file:
            for line in file:
                if line[1:2] == select_kind:
                    if line[4:12] >= start_date:
                        chat_set.add(line)
    except Exception as e:
        continue

chat_list = sorted(list(chat_set))

for line in chat_list:
    chat.write(line)

chat.close()
