import sys

def calc(nums):
    total = sum(nums)
    print(f"合計:{total}")
    if nums :
        ave = total/len(nums)
        print(f"平均:{ave}")
#コマンドライン引数で関数を実行する
args = sys.argv[1:]
nums = [float(num) for num in args]
calc(nums)
