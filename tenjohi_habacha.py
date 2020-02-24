import glob

#天上碑のチャットログフォルダからファイルの一覧を取得する
file_list = glob.glob("C:\\GameOn\\1003b_jpn\\Chatlog\\*.txt")
for file in file_list:
    line = open(file, "r")
    for test in line:
        print(test.rstrip("\n"))
