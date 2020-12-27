i=0
while i<=5:
    print(i)
    i+=1
#Pythonでは、インクリメント・デクリメント演算子がない
#コロン(:)を忘れずに

j=1
while j<=5:
   
    text=input("数字を入力してください")
    number=int(text)
   
    if text=="999":
        print("中断します")
        break
    else:
         print(j,"回目",number**number)
    j+=1
    continue
     
print("終了しました")
    #breakで、抜け出す
    #continueで、ループの先頭からやり直す
    
    
      