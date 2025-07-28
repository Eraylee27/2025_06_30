def get_bmi()->float:
    '''
    建立身高,體重的輸入  #「''''''」Docstring可以知道這個function用途
    計算BMI
    return
    bmi的值
    '''

    height = float(input('請輸入身高120-250cm):'))
    if not (120 <= height <= 250):
        raise Exception('身高範圍輸入錯誤')
    weight = float(input('請輸入體重30-200kg):'))
    if not (30 <= weight <=200):
         raise Exception('體重範圍輸入錯誤')
    bmi = weight / ((height  / 100) **2)
    print(f"您的身高為:{height}\n您的體重為:{weight}")
    print(f'👉你的BMI為:',round(bmi,1))
    return bmi

def get_status(bmi):
        if bmi < 18.5:
            x = '體重過輕❌'
        elif 18.5 <= bmi < 24:
            x = '正常範圍✅'
        elif 24 <= bmi < 27:
            x = '體重過重❌'
        elif 27 <= bmi < 30:
            x = '輕度肥胖❌'
        elif 30 <= bmi < 35:
            x = '中度肥胖❌'
        elif bmi >= 35:
            x = '重度肥胖❌'
        print('👉您的BMI為',x)

def main():
    while (True):
        try:
            bmi = get_bmi()
            get_status(bmi)
        except ValueError:
            print("格式錯誤")
            continue
        except Exception as e:
            print(e) 
            continue
        finally:
            print("======應用程式結束======")
            break

if __name__ == "__main__":
    main()