import glob

file_list = glob.glob("C:\\GameOn\\1003b_jpn\\Chatlog\\*.txt")
habacha_file = "C:\\GameOn\\1003b_jpn\\Chatlog\\chat_log.txt"

habacha = open(habacha_file, "w")

habacha_set = set()

select_kind = input("どのチャット？(1:ch,2:ハバチャ,3:密,6:討伐):")
start_date = input("いつからのログ？(yy/mm/dd)：")

for file_name in file_list:
    try:
        with open(file_name, "r" ,errors='ignore') as file:
            for line in file:
                if line[1:2] == select_kind:
                    if line[4:12] >= start_date:
                        habacha_set.add(line)
    except Exception as error:
        continue

habacha_list = sorted(list(habacha_set))

for line in habacha_list:
    habacha.write(line)

habacha.close()
