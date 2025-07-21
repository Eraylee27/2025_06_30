import random

play_count = 0

while(True):
    play_count += 1
    min = 1
    max = 100
    count = 0
    guess_value = random.randint(min,max)
    print("==========猜數字遊戲===========\n")
    while(True):
        try:
            count += 1
            keyin = int(input(f"猜數字範圍{min}~{max}:"))
            if min <= keyin <= max:
                if(keyin == guess_value):
                    print(f"\n🎉賓果!猜對了,答案是:{guess_value}")
                    print(f"您猜了{count}次")
                    break

                elif keyin > guess_value:
                    print(f"您猜了{keyin} → 再小一點!")
                    max = keyin - 1
                
                else:
                    print(f"您猜了{keyin} → 再大一點")
                    min = keyin + 1

                print(f"➡️您已經猜{count}次")
                
            else:
                raise Exception("請輸入提示範圍內的數字")
            
        except ValueError as e:
            print("格式錯誤",e)
        except Exception as e:
            print(e)

    choose = input("輸入 y (再玩一次)或 n (結束遊戲):")
    if choose == "y":
        print("\n～重新開始～")
        continue
    else:
        print("\n～遊戲結束～")
        break
print(f"\n您總共玩了{play_count}次")