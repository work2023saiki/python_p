#import csv    #csvファイル利用するため　拡張子に注意。CSV（コンマ区切り）（*.csv)のほうで読み込める
import tkinter as tk   #デスクトップアプリ作成のため
import random as rd    #問題の選択、文字列のシャッフルに使用
a = ["ふくやままさはる", "すだまさき", "あらがきゆい", "あやせはるか", "まつもとひとし", "いしはらさとみ","しむらけん"]  #問題に出す元々の文字列
fnt = ("Times New Roman", 20)    #文字のフォント設定

""" 
csvfile = open('talent.csv', 'r')
gotdata = csv.reader(csvfile)
for row in gotdata:
    #各行の内容の表示
    print(row)
csvfile.close()
"""
  
class Application(tk.Frame): #tkinterフレームを作成
    def __init__(self, root=None):
        super().__init__(root, width=380, height=280,
                         borderwidth=1, relief='groove')
        self.root = root
        self.pack()
        self.pack_propagate(0)

    def create_q_label(self, tex, side1):    #問題文ラベル
        self.q = tk.Label(self, text=tex, font=fnt)     
        self.q.pack(side=side1, pady=20)
        
    def create_kekka_label(self, tex, side1):    #結果ラベル
        self.kekka = tk.Label(self, text=tex, font=fnt)     
        self.kekka.pack(side=side1, pady=20)
        
    def create_entry(self):   #入力欄
        self.entry = tk.Entry(self, font=fnt)       #入力欄をフレーム上に配置
        self.entry.focus_set()     #入力欄のカーソルを最初から表示
        self.entry.pack(side="bottom")     #入力欄の配置

    def create_button(self):       #解答ボタン
        self.bt = tk.Button(self, text="解答", font=fnt, command=self.bt_info)
        self.bt.pack(side="bottom", pady = 20)

    def bt_info(self):  #ボタン押したときの処理
      ans = self.entry.get()   #入力欄の文字列を取得
      if ans == b:        #正解だったら
        app.create_kekka_label("正解！", "bottom")    #「正解」ラベルを表示
        root.after(1500, self.riset1)    #1.5秒後に関数riset1を呼び出す
      else:                 #不正解だったら
        app.create_kekka_label("不正解！", "bottom")  #「不正解」ラベルを表示
        root.after(1500, self.riset2)   #1.5秒後に関数riset2を呼び出す   
          
    def riset1(self): #正解して問題を変える処理 
      self.kekka.destroy()   #「正解」を消す
      self.entry.delete(0, tk.END)   #入力欄に打ち込んだ文字列を消す
      q_make()     #問題を作る関数を呼び出す
      self.q["text"] = list2       #問題文のテキストだけ変更
      
    def riset2(self): #不正解のときの処理
      self.kekka.destroy()  #「不正解」のラベルを削除
      self.entry.delete(0, tk.END)   #入力欄に打ち込んだ文字列を消す

def q_make():
  global b, c, list2 
  b = rd.choice(a)     #問題に出す文字列を選択
  c = b               #cは問題作成、bは正解一致判定に使用
  list2 =list(c)       #文字列bを１文字ずつリストlist2に格納する
  rd.shuffle(list2)    #リストの要素の順番をシャッフルする   

q_make()
root = tk.Tk()       #Tkオブジェクトを作成
root.geometry("600x300")  #横600,縦400のウィンドウ
root.title("文字当てゲーム")    #タイトル設定

app = Application(root=root)    #appオブジェクトを作成
app.create_q_label(list2, "top")    #問題文を設置
app.create_entry()     #入力欄を設置
app.create_button()    #解答ボタンを設置

app.mainloop()   #実行