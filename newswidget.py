from tkinter import *
import requests
import json

root = Tk()
root.geometry("700x600")
root.overrideredirect(False)

newslabel = Label(root, text="BBC News Update", font=("Jokerman", 15, "bold"))
newslabel.place(relx=0.5, rely=0.1, anchor=CENTER)

news1 = Label(root, font=("Modern", 13, "bold"), fg="blue", wraplength=500, justify=LEFT)
news1.place(relx=0.2, rely=0.2, anchor=W)

news1_desc = Label(root, font=("arial", 11, "bold"), fg="red", wraplength=500, justify=LEFT)
news1_desc.place(relx= 0.2, rely=0.25, anchor=W)

news2 = Label(root, font=("Modern", 13, "bold"), fg="blue", wraplength=500, justify=LEFT)
news2.place(relx=0.2, rely=0.35, anchor=W)

news2_desc = Label(root, font=("arial", 11, "bold"), fg="red", wraplength=500, justify=LEFT)
news2_desc.place(relx= 0.2, rely=0.4, anchor=W)

news3 = Label(root, font=("Modern", 13, "bold"), fg="blue", wraplength=500, justify=LEFT)
news3.place(relx=0.2, rely=0.48, anchor=W)

news3_desc = Label(root, font=("arial", 11, "bold"), fg="red", wraplength=500, justify=LEFT)
news3_desc.place(relx= 0.2, rely=0.55, anchor=W)

news4 = Label(root, font=("Modern", 13, "bold"), fg="blue", wraplength=500, justify=LEFT)
news4.place(relx=0.2, rely=0.65, anchor=W)

news4_desc = Label(root, font=("arial", 11, "bold"), fg="red", wraplength=500, justify=LEFT)
news4_desc.place(relx= 0.2, rely=0.7, anchor=W)

news5 = Label(root, font=("Modern", 13, "bold"), fg="blue", wraplength=500, justify=LEFT)
news5.place(relx=0.2, rely=0.8, anchor=W)

news5_desc = Label(root, font=("arial", 11, "bold"), fg="red", wraplength=500, justify=LEFT)
news5_desc.place(relx= 0.2, rely=0.85, anchor=W)


api_request = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=adb3634a6cd6498882e12bb6cc8ae6e0")
open_bbc_page = json.loads(api_request.content)

title1 = open_bbc_page['articles'][0]['title']
desc1 = open_bbc_page['articles'][0]['description']

title2 = open_bbc_page['articles'][1]['title']
desc2 = open_bbc_page['articles'][1]['description']

title3 = open_bbc_page['articles'][2]['title']
desc3 = open_bbc_page['articles'][2]['description']

title4 = open_bbc_page['articles'][3]['title']
desc4 = open_bbc_page['articles'][3]['description']

title5 = open_bbc_page['articles'][4]['title']
desc5 = open_bbc_page['articles'][4]['description']

news1['text'] = "Title 1:" + title1
news2['text'] = "Title 2:" + title2
news3['text'] = "Title 3:" + title3
news4['text'] = "Title 4:" + title4
news5['text'] = "Title 5:" + title5

news1_desc['text'] = "Description:" + desc1
news2_desc['text'] = "Description:" + desc2
news3_desc['text'] = "Description:" + desc3 
news4_desc['text'] = "Description:" + desc4 
news5_desc['text'] = "Description:" + desc5 





root.mainloop()