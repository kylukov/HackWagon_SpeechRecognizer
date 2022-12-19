import os
import webbrowser
import sys
import subprocess
import pandas as pd
import voice
import numpy as np
import number
from extractor import NumberExtractor
import re
import test
from text_to_num import alpha2digit
from testim2 import change
try:
	import requests		#pip install requests
except:
	pass

extractor = NumberExtractor()
def factory(text):
        try:
                global dataframe
                global index
                global now
                now=3
                text= text.replace('завод','')
                text= text.replace('зовут','')
                text= text.replace('двухтысячный','2000')
                text = alpha2digit(text, 'ru')
                text=text.split()
                flag=False
                if len(text)==1:
                        u=text.replace('ий','')
                        u=u.replace('ый','')
                        u=u.replace('ой','')
                        u=u.replace('ая','')
                        dataframe.iloc[index,3] = ''.join(u)
                elif len(text)>2:
                        for i in range(1,len(text)):
                                if text[i]=='год':
                                        flag=True
                                        u=text[i-1].replace('ий','')
                                        u=u.replace('ый','')
                                        u=u.replace('ой','')
                                        u=u.replace('ая','')
                                        dataframe.iloc[index,3] = ''.join(u)
                                        dataframe.iloc[index,2] =' '.join(text)
                print('сработал завод'+ str(text))
                writer = pd.ExcelWriter('output2.xlsx')
                dataframe.to_excel(writer)
                writer.save()
        except:
                pass
def number(text):
        try:
                global dataframe
                global index
                global now
                now=1
                text= text.replace('номер','')
                text=alpha2digit(text,'ru')
                text=text.replace(' ','')
                text=text.replace('ый','')
                text=text.replace('ая','')
                text=text.split()
                print('ПРОВЕРКА номера',text)
                for i in text:
                        print(i)
                        if i.isdigit():
                                text=int(i)
                                print('конец')
                                break
                else:
                        return
                text=str(text)
                #text=change(text)
                dataframe.iloc[index,1] = text
                print('записали '+ text)
                '''Функция записи номера завода'''
                print('сработал номер' + str(text))
                writer = pd.ExcelWriter('output2.xlsx')
                dataframe.to_excel(writer)
                writer.save()
        except:
                pass
def year(text):
        try:
                global dataframe
                global index
                global now
                now=2
                text= text.replace('год','')
                text= text.replace('двухтысячный','2000')
                text=extractor.replace(text)
                text=extractor.replace_groups(text)
                text=change(text)
                #text=alpha2digit(text,'ru')

                text=text.split(' ')
                if len(text)>3:
                        factory(text[3])
                #print('ПРОВЕРКА номера',text)
                for i in text:
                        print(i)
                        if i.isdigit():
                                text=i
                                #print('конец')
                                break
                else:
                        return
                text=int(text)
                if text<22:
                        text+=2000
                elif text<100:
                        text+=1900
                elif text<700:
                        text='19'+str(text)[-2:0]
                elif text<1000:
                        text+=1000
                text=str(text)
                dataframe.iloc[index,2] = text
                print('сработал год'+ str(text))
                writer = pd.ExcelWriter('output2.xlsx')
                dataframe.to_excel(writer)
                writer.save()
        except:
                pass
def pre_next(text):
        try:
                try:
                        indexstart=re.search(r"\d", text).start()
                        print(text)
                        slovo=text[:indexstart]
                        numb=text[indexstart:]
                        return slovo,numb
                except AttributeError:
                        return text, None
        except:
                pass

def next(text):
        try:
                global dataframe
                global index
                global now
                now=0
                text= text.replace('следующий','')
                text= text.replace('следующая','')
                text= text.replace('двухтысячный','2000')
                text= text.replace('пора','пара')
                #text=extractor.replace(text)
                #text=extractor.replace_groups(text)
                #print(text)
                #text=change(text)
                #print(text)
                text=alpha2digit(text,'ru')
                #text=change(text)
                text= text.replace('номер','')
                '''Функция записи номера завода'''
                index+=1
                slov,num=pre_next(text)
                dataframe.iloc[index,0]=slov
                if type(num)==str:
                        #num=alpha2digit(num,'ru')
                        num=num.replace(' ','')
                        num=num.replace('ый','')
                        num=num.replace('ая','')
                        #num=change(num)
                        print(num)
                        number(num)
                print('сработал next' +' ' + slov +' | '+ str(num))
                writer = pd.ExcelWriter('output2.xlsx')
                dataframe.to_excel(writer)
                writer.save()
        except:
                pass
def comment(text):
        try:
                global dataframe
                global index
                global now
                now=4
                text= text.replace('комментарий','')
                text= text.replace('описание','')
                text = alpha2digit(text, 'ru')
                #text=change(text)
                dataframe.iloc[index,4]=text
                print('сработал comment' + text)
                writer = pd.ExcelWriter('output2.xlsx')
                dataframe.to_excel(writer)
                writer.save()
        except:
                pass
def mistake(text):
        try:
                global dataframe
                global index
                global now
                text= text.replace('ошибка','')
                #text=change(text)
                dataframe.iloc[index,now]=text
                print('сработал mistake' +text +'|' +str(now))
                writer = pd.ExcelWriter('output2.xlsx')
                dataframe.to_excel(writer)
                writer.save()
        except:
                pass
def name(text):
        try:
                global dataframe
                global index
                global now
                text= text.replace('название','')
                u=u.replace('следущее','')
                text= text.replace('имя','')
                text = alpha2digit(text, 'ru')
                #text=change(text)
                dataframe.iloc[index,0]=text
                print('сработал имя' + text)
                writer = pd.ExcelWriter('output2.xlsx')
                dataframe.to_excel(writer)
                writer.save()
        except:
                pass

k=np.full((2000,5),None)
dataframe=pd.DataFrame(k,columns=['наименование','номер','год','завод','комментарий'])
index=0
now=0
