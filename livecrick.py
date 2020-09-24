from tkinter import*
import time
import requests
import json

root=Tk()

root.geometry("600x100")

match_data=requests.get('https://cricapi.com/api/cricketScore?unique_id=1216508&apikey=kizOe4e241YPc712yyRjplkn3ZH3')
json_data=match_data.json()
def times():
    current_score=json_data['stat']
    score.configure(text="currnt score: "+current_score)
    score.after(200,times)

score=Label(root,font=("time",15,"bold"),bg="white")
score.grid(row=2,column=2,pady=25,padx=100)
times()

root.mainloop()