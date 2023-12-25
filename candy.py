import turtle

t = turtle.Turtle()    #turtleオブジェクト作成
#t2 = turtle.Turtle()

#キャンディの棒を描く
t.setpos(0,-200)   #(x,y)=(0,-200)
t.home()           #原点(0,0)に移動する

for i in range(5):#外側から順番に内側の円を描く。
    t.circle(100-i*20) #描画

    #次の描画開始位置に移動する
    t.up()   #ペンあげて描画しない
    t.setpos(0, 20*(i+1)) #y座標を２０ずつ移動
    t.down()  #ペン下げて描画準備

for i in range(18): #らせんの描画
    t.circle(100, 60)   #半径１００、６０度の円弧を描画
    t.up()
    t.setpos(0, 100)   #らせんの開始点に移動する
    t.right(40)    #らせんの間隔を調整
    t.down()
    
    