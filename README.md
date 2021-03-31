
主要兩大塊為：執行畫面和遊戲大廳

1、mainPage表示執行畫面的func，再分爲登入（login）和新帳號（creatNewAccount）和離開。
   需要輸入這三個值才會開始跑迴圈。
   
   如果登入的帳號密碼錯誤，或者，新帳號的帳號重複，則return False會再跑一次。
   如果登入成功，或者，建立新帳號，則會return （使用者ID） = 下面的start
   
   start用於找出All資料裡面的使用者所有資訊，包含Id、password、balance。

2、遊戲畫面，使用while，除非輸入“離開”，否則會一直執行。
   當執行畫面時，輸入離開，則不會執行while；
   當遊戲畫面，輸入離開，也不會執行while。
   
   遊戲畫面,分爲：撲克牌、骰子、儲值。
   使用function： get_poker()、check_result(banker,player)、rollDice(first = False)、
       bigORsmall()、twoDice()、threeDice()來執行游戲
       printResult(result)  撲克牌結果
       printResult1(result) Craps 結果
       PrintResult(result)  比大小 結果
       printResult2(result) 兩骰 結果
       printResult3(result) 三骰 結果
    
 遊戲開始時，如金額不足，則跳回遊戲畫面。
