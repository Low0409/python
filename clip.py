import pyperclip
#print(pyperclip.paste())　←クリップボード全部出力
copy = pyperclip.paste()
newcopy = copy.replace("0","7")#←クリップボードにある0全部を７に置き換え
print(newcopy)