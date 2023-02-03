# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 19:16:27 2019

@author: seaso
"""

#Library
import os
import json
import random
from random import randint  

#========================================
#functions
#執行畫面
def mainPage():
    selected1 = False
    while selected1 == False:
        selected1 = str(input("新帳號 or 登入 or 離開: "))           
        if selected1 == "登入":
            selected1 = login()
        elif selected1 == "新帳號":
            selected1 = creatNewAccount()
        elif selected1 == "離開":
            selected1 == "離開"
    return selected1 

#登入
def login():
    with open(filepath,'r') as file_object:
        All = json.load(file_object)
    Id = str(input("請輸入帳號："))
    a = All.get(Id)
    if a == None:
        print("查無帳號或密碼錯誤")
        return False
    password = str(input("請輸入密碼："))
    if All[Id]['password'] != password:
        print("查無帳號或密碼錯誤")
        return False
    else:
        balance = All[Id]['balance']
        print("歡迎進入遊戲大廳! 目前餘額為%.2f " % balance)
        return Id
    
#新帳號
def creatNewAccount(): 
    ID = str(input("請輸入新帳號："))
    if os.path.isfile(filepath):
        with open(filepath,'r') as file_object:
                All = json.load(file_object)
                a = All.get(ID)
                if a == None:
                    Id = {}
                    Id['ID'] = ID
                    Id['password'] = str(input("請輸入密碼："))
                    Id['balance'] = 1000
                    All[ID] = Id
                    print("獲得1000元初始金")
                    with open(filepath,'w') as file_object:
                        json.dump(All,file_object)
                    return ID     
                else:
                    print("帳號已被使用")
                    return False
    else:
        All = {}
        Id = {}
        Id['ID'] = ID
        Id['password'] = str(input("請輸入密碼："))
        Id['balance'] = 1000
        All[ID] = Id
        print("獲得1000元初始金")
        with open(filepath,'w') as file_object:
            json.dump(All,file_object)
        return ID

#撲克牌
#撲克牌分牌
def get_poker():
    face = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    suits = ["♣","♦","♥","♠"]
    pokers = []
    for i in suits:
        for j in face:
            poker=[]
            poker.append(i)
            poker.append(j)
            pokers.append(poker)   
    random.shuffle(pokers)
    return pokers

#撲克牌比大小
def check_result(banker,player):
    suits = ["♣","♦","♥","♠"]
    face = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    if face.index(banker[1]) > face.index(player[1]):
        return False
    elif face.index(banker[1]) < face.index(player[1]):
        return True
    else:
        if suits.index(banker[0]) > suits.index(player[0]):
            return False
        elif suits.index(banker[0]) < suits.index(player[0]):
            return True

#撲克牌結果
def printResult(result):
    if result:
        print("玩家勝, 贏得 %.2f元" % money)              
        account['balance'] = account['balance'] + money  
        All[start]['balance'] = account['balance']

    else:
        print("玩家敗, 損失 %.2f元" %  money)
        account['balance'] = account['balance'] - money  
        All[start]['balance'] = account['balance']

#Craps
#骰子
def dice():
    d = randint(1, 6)                      
    return d                               

#raps 游戲
def rollDice(first = False):
    dice1 = dice()                         
    dice2 = dice()
    dicesum = dice1 + dice2                
    
    if first:                              
        print("第一次擲骰: %d" % dicesum)   
    else:
        print("非第一次擲骰: %d" % dicesum)
         
    return dicesum                         

#Craps結果
def printResult1(Result):
    if Result:                                                         
        print("玩家勝, 贏得 %.2f元" % ((0.5) * money))                 
        account["balance"] = account["balance"] + int((0.5) * money) 
        All[start]['balance'] = account['balance']

    else:
        print("玩家敗, 損失 %.2f元" % money)
        account["balance"] = account["balance"] - money
        All[start]['balance'] = account['balance']
        
#骰子游戲
def bigORsmall():#比大小
    result = "Unknow"
    if diceSum in (3,18):
        result = "Lose"
    elif diceSum >= 11: #看總和再看選擇
        if Game1choice == 1:
            result = "Win"
        else:
            result = "Lose"
    else:
        if Game1choice == 2:
            result = "Win"
        else:
            result = "Lose"
    return result
   
def twoDice():#兩骰組合
    result = "Unknow"
    if a in (dice1,dice2,dice3) and b in (dice1,dice2,dice3):
        result = "Win"
    else:
        result = "Lost"
    return result

def threeDice():#三骰組合
    result = "Unknow"
    if (dice1 == a and dice2 == a and dice3 == a):
        result = "Win"
    else:
        result = "Lost"
    return result

#骰子-比大小 結果
def PrintResult(result):
    if result == "Win":
        print("玩家勝, 贏得 %.2f元" % money)              
        account['balance'] = account['balance'] + money  
        All[start]['balance'] = account['balance']

    else:
        print("玩家敗, 損失 %.2f元" %  money)
        account['balance'] = account['balance'] - money  
        All[start]['balance'] = account['balance']

#骰子-兩骰組合 結果
def printResult2(result2):                                     
    if result2 == "Win":                                                
        print("玩家勝, 贏得%d元" % (money * 10))
        account['balance'] = account['balance'] + money * 10  
        All[start]['balance'] = account['balance']
    else:
        print("玩家敗, 損失%d元" % money)
        account['balance'] = account['balance'] - money
        All[start]['balance'] = account['balance']

#骰子-三骰組合 結果
def printResult3(result3):                                     
    if result3 == "Win":                                                
        print("玩家勝, 贏得%d元" % (money * 30))
        account['balance'] = account['balance'] + money * 30  
        All[start]['balance'] = account['balance']
    else:
        print("玩家敗, 損失%d元" % money)
        account['balance'] = account['balance'] - money
        All[start]['balance'] = account['balance']

#================================================
#main
filepath = "user_info.json" #文件名稱

start = mainPage() 

if start == "離開": #此爲跳到遊戲畫面的過程
    selected2 = "離開"
    print("謝謝，歡迎再次遊玩!")
else:
    selected2 = "Unknown" #此時start為使用者ID
    
    
while selected2 != "離開":
    with open("user_info.json", 'r') as file_object:            
        All = json.load(file_object)
    account = All[start] #此爲使用者Id、password、balance的資訊
    selected2 = str(input("撲克牌 or 骰子 or 儲值 or 離開: "))
    
    if selected2 == "撲克牌":
        money = int(input("請輸入下注金額: "))    
        if account['balance'] < money:           
            print("餘額不足")
        else:
            Poker = get_poker()
            banker = Poker[0]                         
            player = Poker[1]                         
            print("玩家 -> %s" % player)
            print("莊家 -> %s" % banker)
            game1 = check_result(banker, player)  
            if game1 == True:                     
                printResult(True)
            else:
                printResult(False)
    
    elif selected2 == "骰子":
        choice = str(input("Craps or 骰寶: "))              
        if choice == "Craps":                               
            money = int(input("請輸入下注金額: "))
            if account['balance'] < money:                 
                print("餘額不足")
            else:
                gameStatus = True        
                firstPoint = rollDice(True)                  
                
                while ( gameStatus == True ):
                    if firstPoint in (7, 11):                
                        print("玩家勝, 贏得 %.2f元" % money)
                        account["balance"] = account["balance"] + money   
                        All[start]['balance'] = account['balance']
                        break
                    elif firstPoint in (2, 3, 12):           
                        printResult1(False)
                        break    
                    else:
                        tmp = rollDice()                    
                        if tmp == 7:                        
                            printResult1(False)
                            break
                        elif tmp == firstPoint:             
                            printResult1(True)
                            break
        elif choice == "骰寶":
            dice1 = dice()
            dice2 = dice()
            dice3 = dice()
            diceSum = dice1 + dice2 + dice3
            
            print("請選擇下注項目")
            print("(1)比大小")
            print("(2)兩骰組合")
            print("(3)三骰組合")
            firstchoice = int(input("請選擇 1 or 2 or 3:"))
    
            if firstchoice == 1: # 游戲1 比大小
                print("（1）大")
                print("（2）小")
                Game1choice = int(input("請選擇大小 1 or 2:"))
                result = bigORsmall()
                    
                money = int(input("請輸入下注金額："))
                if account['balance'] < money:          
                    print("餘額不足")
                else:    
                    print("擲骰結果：[%d,%d,%d]" % (dice1,dice2,dice3))
                    if result == "Win" :
                        PrintResult("Win") 
                    else:
                        PrintResult("Lose") 
                
            elif firstchoice == 2: # 遊戲2 兩骰組合
                a = int(input("請輸入點數1(1-6):"))
                b = int(input("請輸入點數2(1-6):"))
                result = twoDice()
                
                money = int(input("請輸入下注金額："))
                if account['balance'] < money:     
                    print("餘額不足")
                else:    
                    print("擲骰結果：[%d,%d,%d]" % (dice1,dice2,dice3))
                    if result == "Win" :
                        printResult2("Win")                        
                    else:
                        printResult2("Lose")
                
            elif firstchoice == 3: # 遊戲3 三骰組合
                a = int(input("請輸入點數(1-6):"))
                result = threeDice()
                
                money = int(input("請輸入下注金額："))
                if account['balance'] < money:          
                    print("餘額不足")
                else:    
                    print("擲骰結果：[%d,%d,%d]" % (dice1,dice2,dice3))
                    if result == "Win" :
                        printResult3("Win")                        
                    else:
                        printResult3("Lose")
                        
    elif selected2 == "儲值":
        money = int(input("請輸入儲值金額: "))
        account['balance'] = account['balance'] + money
        All[start]['balance'] = account['balance']  
        with open ("user_info.json", 'w') as file_object:
            json.dump(All, file_object)
        print("儲值成功，目前餘額為%s" % All[start]['balance'])

    with open ("user_info.json", 'w') as file_object:            
        json.dump(All, file_object)

