#!/usr/bin/env python
# coding: utf-8

# In[153]:


import time
import os
import pyautogui as pag
import pyperclip


# In[155]:


try:#測試 類似if判斷但不設條件
    while True:#無限執行
        print("Press Ctrl-C to end")
        x,y=pag.position()#滑鼠座標
        pos = "position: "+str(x).rjust(4)+','+str(y).rjust(4)
        print(pos)
        time.sleep(1)#延遲幾秒
        os.system('clear')#清除結果
except KeyboardInterrupt: #手動停止 複製跟停止都是Ctrl-C 時會出現KeyboardInterrupt的錯誤except用於跳過此錯誤
    print('end!')


# In[139]:


content = """   
哈哈哈哈哈哈
"""#訊息內容用content存


# In[152]:


time.sleep(5)
for line in list(content.split("\n"))*3:
    if line:
        pyautogui.click(1001, 881)  #滑鼠在座標上點擊
        pyperclip.copy(line)    #複製
        pyautogui.hotkey("ctrl","v") #貼上
        pyautogui.typewrite("\n")   #傳送
        time.sleep(0.1) #間隔

