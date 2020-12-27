def apple(a,b):
    
    ans1 = a*100
    ans2 = b*200
    
    ans3=ans1+ans2
    
    return ans3
    
ans=apple(1,2)
print(ans)
    #defで、関数を定義
    #括弧（）のなかに、引数を定義
    #intなどは、いらない
    #引数の後には、セミコロン（：）を忘れずに
    
    #関数＝作った関数名（数値１、数値２）
    
def func1(name):
    print("Hello",name,)
    
def func2():
    func1("func2")

func2()

#Hello,func2と表示させる
#func2()の文は、必要