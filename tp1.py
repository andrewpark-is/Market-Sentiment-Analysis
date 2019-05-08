# Mode Demo
# all these libraries are new, not from me lol
from tkinter import *
from alpha_vantage.timeseries import TimeSeries
import requests
import alpha_vantage
import json
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import requests
import nltk
import math
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

####################################
# init
####################################

def init(data):
    data.mode = "loginScreen"
    data.labels = []
    data.sizes = []
    data.key = 'CF43U1Q2LD1PGDKW'
    data.ticker = ''
    data.ratings = dict()
    data.stocks = ['Cash']
    data.sizes = [100]
    data.url = "https://www.alphavantage.co/query" 
    data.totalCash = 100000
    data.articles = []
    data.margin = 30
    data.ratio = 0
    data.wrong = False
    data.currUser = ""
    data.value = 0
    data.fileStocks = []
    data.colors = []
    data.gif1 = PhotoImage(file='login.gif')
    data.gif2 = PhotoImage(file='table.gif')
    data.growth = 0
    
####################################
# matplot
####################################

def portfolioShow(data): # modified from matplotlib library to include dynamic user input
    
    fig1, ax1 = plt.subplots()
    ax1.pie(data.sizes, labels=data.stocks, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
    
def stockChart(stock): # modified from the API to include user input
    ts = TimeSeries(key = 'CF43U1Q2LD1PGDKW', output_format='pandas')
    data, meta_data = ts.get_daily(symbol=stock, outputsize='full')
    data['4. close'].plot()
    plt.title('Trading History')
    plt.show()
    
####################################
# file IO; modified from lecture notes
####################################

def readFile(path):
    with open(path, "rt") as f:
        return f.read()
        
def readUser(path):
    with open(path, "rt") as f:
        lines = f.readlines()
        return lines[0]

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)
        
def appendToFile(path, newContent):
    with open(path, "a") as f:
        f.write("\n")
        f.write(newContent)

####################################
# mode dispatcher; modified from lecture notes
####################################

def mousePressed(event, data):
    if (data.mode == "loginScreen"): 
        loginScreenMousePressed(event, data)
    elif (data.mode == "table"):   
        tableMousePressed(event, data)
    elif (data.mode == "pair"):       
        pairTradingMousePressed(event, data)
    elif (data.mode == "sentiment"):       
        sentimentMousePressed(event, data)
    elif (data.mode == "trade"):
        tradeMousePressed(event, data)
    elif (data.mode == "portfolio"):
        portfolioMousePressed(event, data)
    elif (data.mode == "help"):
        helpMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode == "loginScreen"): 
        loginScreenKeyPressed(event, data)
    elif (data.mode == "table"):   
        tableKeyPressed(event, data)
    elif (data.mode == "pair"):       
        pairTradingKeyPressed(event, data)
    elif (data.mode == "sentiment"):
        sentimentKeyPressed(event, data)
    elif (data.mode == "trade"):
        tradeKeyPressed(event, data)
    elif (data.mode == "portfolio"):
        portfolioKeyPressed(event, data)
    elif (data.mode == "help"):
        helpKeyPressed(event, data)

def timerFired(data):
    if (data.mode == "loginScreen"): 
        loginScreenTimerFired(data)
    elif (data.mode == "table"):   
        tableTimerFired(data)
    elif (data.mode == "pair"):    
        pairTradingTimerFired(data)
    elif (data.mode == "sentiment"):
        sentimentTimerFired(data)
    elif (data.mode == "trade"):
        tradeTimerFired(data)
    elif (data.mode == "portfolio"):
        portfolioTimerFired(data)
    elif (data.mode == "help"):
        helpTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "loginScreen"): 
        loginScreenRedrawAll(canvas, data)
    elif (data.mode == "table"):   
        tableRedrawAll(canvas, data)
    elif (data.mode == "pair"):       
        pairTradingRedrawAll(canvas, data)
    elif (data.mode == "sentiment"):
        sentimentRedrawAll(canvas, data)
    elif (data.mode == "trade"):
        tradeRedrawAll(canvas, data)
    elif (data.mode == "portfolio"):
        portfolioRedrawAll(canvas, data)
    elif (data.mode == "help"):
        helpRedrawAll(canvas, data)

####################################
# Login screen
####################################

def loginScreenMousePressed(event, data):
    pass

def loginScreenKeyPressed(event, data):
    if event.keysym == "space":
        signupWidget(data)
    elif event.keysym == "Return":
        loginWidget(data)

def loginScreenTimerFired(data):
    pass
    
def loginWidget(data):
    master = Tk()
    
    L1 = Label(master, text="Username")
    L1.pack(side = TOP)
    
    e = Entry(master)
    e.pack()
    e.focus_set()
    
    L2 = Label(master, text="Password")
    L2.pack(side = TOP)
    
    e2 = Entry(master)
    e2.pack()
    e2.focus_set()
    
    def callback():
        try:
            check = readUser(e.get() + ".txt")
            if "\n" in check:
                check = check[:-1]
            print("1", check)
            print("2", e.get() + " " + e2.get())
            if (e.get() + " " + e2.get()) == check:
                data.currUser = e.get() 
                data.wrong = False
                data.mode = "table"
        except:
            data.wrong = True
                
    b2 = Button(master, text="Login", width=20, command=callback)
    b2.pack()
    
    mainloop()
    
def signupWidget(data):
    master = Tk()
    
    L1 = Label(master, text="New Username")
    L1.pack(side = TOP)
    
    e = Entry(master)
    e.pack()
    e.focus_set()
    
    L2 = Label(master, text="New Password")
    L2.pack(side = TOP)
    
    e2 = Entry(master)
    e2.pack()
    e2.focus_set()
    
    def callback():
        writeFile(e.get() + ".txt", e.get() + " " + e2.get())
    
    b2 = Button(master, text="Sign Up", width=20, command=callback)
    b2.pack()
    
    mainloop()

def loginScreenRedrawAll(canvas, data):
    canvas.create_image(0, 100, image=data.gif1, anchor=NW)
    canvas.create_text(data.width/2, 50,
                       text="Market Sentiment Simulation", font="Times 26 bold")
    canvas.create_text(data.width/2, data.height-40,
                       text="Press the Enter key to login", font="Times 20")
    canvas.create_text(data.width/2, data.height-80, text="Press the Space bar to sign up", font="Times 20")
    if data.wrong == True:
        canvas.create_text(data.width/2, data.height-60, text="The username or password you have entered is incorrect.", font="Times 20", fill="red")


####################################
# Stock Preview
####################################

def pairTradingMousePressed(event, data):
    pass

def pairTradingKeyPressed(event, data):
    if event.keysym == "Escape":
        data.mode = "table"
    elif event.keysym == 'h':
        data.mode = "help"
    elif event.keysym == 'Return':
        what(data)

def pairTradingTimerFired(data):
    pass
    
def pairTradingRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/2-40,
                       text="View Stock Chart", font="Arial 26 bold")
    canvas.create_text(data.width/2, data.height/2, text="Press Enter to Continue")
    
# from advanced tkinter widget notes (112 website)
def what(data):
    master = Tk()
    v = StringVar()
    e = Entry(master, textvariable=v)
    e.pack()
    s = v.get()
    e.focus_set()
    
    def callback():
        stockChart(e.get())
        print(e.get())
    
    b = Button(master, text="Display", width=20, command=callback)
    b.pack()
    
    mainloop()

####################################
# Sentiment Analysis
####################################

def sentimentMousePressed(event, data):
    pass

def sentimentKeyPressed(event, data):
    if event.keysym == "Escape":
        data.mode = "table"
    elif event.keysym == 'h':
        data.mode = "help"
    elif event.keysym == 'Return':
        what2(data)

def sentimentTimerFired(data):
    pass
    
def sentimentRedrawAll(canvas, data):
    canvas.create_text(data.width/2, 30,
                       text="Sentiment Analysis", font="Arial 26 bold")
    canvas.create_text(data.width/2, 70, text="Press Enter to Continue")
    if data.ticker != "":
        canvas.create_text(data.width/2, 100, text=str(data.ticker))
        canvas.create_text(data.width/2, 130, text=str(data.ratings))
    try:
        canvas.create_rectangle(0, 145, 600, 175, fill=data.colors[0])
        canvas.create_text(data.width/2, 160, text=data.articles[0])
        canvas.create_rectangle(0, 175, 600, 205, fill=data.colors[1])
        canvas.create_text(data.width/2, 190, text=data.articles[1])
        canvas.create_rectangle(0, 205, 600, 235, fill=data.colors[2])
        canvas.create_text(data.width/2, 220, text=data.articles[2])
        canvas.create_rectangle(0, 235, 600, 265, fill=data.colors[3])
        canvas.create_text(data.width/2, 250, text=data.articles[3])
        canvas.create_rectangle(0, 265, 600, 295, fill=data.colors[4])
        canvas.create_text(data.width/2, 280, text=data.articles[4])
        canvas.create_rectangle(0, 295, 600, 325, fill=data.colors[5])
        canvas.create_text(data.width/2, 310, text=data.articles[5])
        canvas.create_rectangle(0, 325, 600, 355, fill=data.colors[6])
        canvas.create_text(data.width/2, 340, text=data.articles[6])
        canvas.create_rectangle(0, 355, 600, 385, fill=data.colors[7])
        canvas.create_text(data.width/2, 370, text=data.articles[7])
        canvas.create_rectangle(0, 385, 600, 415, fill=data.colors[8])
        canvas.create_text(data.width/2, 400, text=data.articles[8])
        canvas.create_rectangle(0, 415, 600, 445, fill=data.colors[9])
        canvas.create_text(data.width/2, 430, text=data.articles[9])
        canvas.create_rectangle(data.width/2-15, 450, data.width/2+15, 470, fill="black")
        if data.ratio > 1.2:
            canvas.create_text(data.width/2, 460, text = "BUY", fill = "green")
        elif data.ratio < 0.8:
            canvas.create_text(data.width/2, 460, text = "SELL", fill = "red")
        else:
            canvas.create_text(data.width/2, 460, text = "HOLD", fill = "yellow")
    except:
        pass
        
# webscraping module, pretty much my original code though
def scrape(stock):
    url = "https://quotes.wsj.com/%s" % (stock)
    website = requests.get(url)
    source = website.text
    headlines = []
    text = source.split(">")
    for line in text:
        if '<span class="headline"' in line:
            index = text.index(' <span class="headline"')
            result = text[index+2]
            headlines.append(result[:-3])
            text.pop(index)
    return headlines
    
# nltk module modified for article headlines that are based on user input, also pretty much original code
def nltkWork(stock, data):
    text = scrape(stock)
    sid = SentimentIntensityAnalyzer()
    keys = [("neg", 0), ("neu", 0), ("pos", 0), ("compound", 0)]
    ratings = dict(keys)
    for article in text:
        ss = sid.polarity_scores(article)
        data.articles.append(article)
        print(article)
        for k in ss:
            ratings[k] += ss[k]
            if k == "neg":
                neg = ss[k]
            elif k =="pos":
                pos = ss[k]
            print('{0}: {1},'.format(k, ss[k]))
        if (neg + pos) != 0:
            colorNum = round(pos / (neg + pos), 3)
            green = int(colorNum * 255)
            red = int((1-colorNum) * 255)
            fill = '#%02x%02x%02x' % (red, green, 0)
            data.colors.append(fill)
        else:
            fill = '#%02x%02x%02x' % (255, 255, 0)
            data.colors.append(fill)
    for k in ratings:
        ratings[k] = round(ratings[k], 3)
    data.ticker = stock
    try:
        data.ratio = round(ratings["pos"] / ratings["neg"], 3)
    except: pass
    data.ratings = ratings
    
# from advanced tkinter widget notes (112 website)
def what2(data):
    master = Tk()
    v = StringVar()
    e = Entry(master, textvariable=v)
    e.pack()
    s = v.get()
    e.focus_set()
    
    def callback2():
        data.articles = []
        data.colors = []
        nltkWork(e.get(), data)
        print(e.get())
    
    b = Button(master, text="Perform Analysis", width=20, command=callback2)
    b.pack()
    
    mainloop()
                           
####################################
# Edit Portfolio (Trade)
####################################

def tradeMousePressed(event, data):
    pass

def tradeKeyPressed(event, data):
    if event.keysym == "Escape":
        data.mode = "table"
    elif event.keysym == 'h':
        data.mode = "help"
    elif event.keysym == 'Return':
        what3(data)
        
def tradeTimerFired(data):
    pass
    
def tradeRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/2-40,
                       text="Time to execute a trade!", font="Arial 26 bold")
    canvas.create_text(data.width/2, data.height/2, text="Press Enter to Continue")

# referred to advanced tkinter widget notes (112 website); original code

def what3(data):
    master = Tk()
    
    L1 = Label(master, text="Stock Ticker")
    L1.pack(side = TOP)
    
    e1 = Entry(master)
    e1.pack()
    e1.focus_set()
    
    L2 = Label(master, text="Number of Shares")
    L2.pack(side = TOP)
    
    e2 = Entry(master)
    e2.pack()
    e2.focus_set()
    
    def callback1():
        data.ticker = e1.get()
        data.stocks.append(data.ticker)
        appendToFile(data.currUser + ".txt", data.ticker)
        cost = price(data, [data.ticker])
        num = e2.get()
        appendToFile(data.currUser + ".txt", num)
        totalCost = float(cost) * float(num)
        print("cash?", data.totalCash)
        data.totalCash -= totalCost
        print('here', data.totalCash)
        appendToFile(data.currUser + ".txt", str(data.totalCash))
        nextSize = totalCost // 1000
        data.sizes[0] -= nextSize
        data.sizes.append(nextSize)
        print(e1.get(), e2.get())
    
    b1 = Button(master, text="Execute Trade", width=30, command=callback1)
    b1.pack()
    
    mainloop()
    
# from the same API as earlier
def price(data, name):
    for symbol in name:
        dataLOL = { "function": "GLOBAL_QUOTE", 
        "symbol": symbol,
        "interval" : "60min",       
        "datatype": "json", 
        "apikey": "CF43U1Q2LD1PGDKW" } 
        response = requests.get(data.url, dataLOL) 
        dataLOL = response.json()
        a = (dataLOL['Global Quote'])
        keys = (a.keys())
        for key in keys:
            if key == "05. price":
                return a[key]
    
                       
####################################
# Review Portfolio
####################################

def readPortfolio(path, data):
    text = readFile(path)
    lstContent = []
    value = 0
    data.fileStocks = []
    newLabel = []
    for line in text.splitlines():
        lstContent.append(line)
    for line in lstContent:
        if data.currUser not in line:
            if line[0].isalpha():
                data.fileStocks.append(line)
                index = lstContent.index(line)
                cost = round(float(price(data, [line])),2) * int(lstContent[index+1])
                percent = round(cost / 100000, 2)
                newLabel.append(percent)
                value += cost
                data.totalCash = float(lstContent[index+2])
    thing = round(data.totalCash / 100000, 2)
    newLabel.append(thing)
    data.sizes = newLabel
    value += data.totalCash
    data.value = value
    data.growth = round((data.value-100000)/100000, 2)
    data.stocks = data.fileStocks
    data.stocks.append('Cash')                   

def portfolioMousePressed(event, data):
    pass

def portfolioKeyPressed(event, data):
    if event.keysym == "Escape":
        data.mode = "table"
    elif event.keysym == 'h':
        data.mode = "help"
    elif event.keysym == 'Return':
        readPortfolio(data.currUser + ".txt", data)
    elif event.keysym == "p":
        portfolioShow(data)        
        
def portfolioTimerFired(data):
    pass
    
def portfolioRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/2-40,
                       text="Portfolio Review", font="Arial 26 bold")
    canvas.create_text(data.width/2, data.height/2, text="Press Enter to Update")
    canvas.create_text(data.width/2, data.height/2+20, text=data.fileStocks)
    canvas.create_text(data.width/2, data.height/2+40, text="Cash: "+str(data.totalCash))
    canvas.create_text(data.width/2, data.height/2+60, text="Value of Portfolio: "+str(data.value))
    canvas.create_text(data.width/2, data.height/2+80, text="Return: "+str(data.growth)+"%")
    canvas.create_text(data.width/2, data.height-30, text="Press 'P' to View Pie Chart")


####################################
# Table of Contents
####################################

def tableMousePressed(event, data):
    pass

def tableKeyPressed(event, data):
    if event.keysym == "Escape":
        data.mode = "loginScreen"
    elif (event.keysym == '1'):
        data.mode = "pair"
    elif (event.keysym == '2'):
        data.mode = "sentiment"
    elif (event.keysym == '3'):
        data.mode = "trade"
    elif (event.keysym == '4'):
        data.mode = "portfolio"
    elif event.keysym == '5':
        data.mode = "help"
    elif event.keysym == "h":
        data.mode = "help"


def tableTimerFired(data):
    pass
    
def tableRedrawAll(canvas, data):
    margin = 105
    start = 110
    side = 70
    canvas.create_image(50, 0, image=data.gif2, anchor=NW)
    canvas.create_text(data.width//2+side, start, text="Preview Stock Charts", font="Times 20")
    canvas.create_text(data.width//2+side, start+margin, text="Sentiment Analysis", font="Times 20")
    canvas.create_text(data.width//2+side, start+2*margin, text="Edit Portfolio (Trade)", font="Times 20")
    canvas.create_text(data.width//2+side, start+3*margin, text="Portfolio Review", font="Times 20")
    canvas.create_text(data.width//2+side, start+4*margin, text="Help", font="Times 20")
    
####################################
# help mode
####################################

def helpMousePressed(event, data):
    pass

def helpKeyPressed(event, data):
    if event.keysym == "Escape":
        data.mode = "table"
    elif event.keysym == "p":
        data.mode = "portfolio"
    elif event.keysym == "t":
        data.mode = "trade"
    elif event.keysym == "s":
        data.mode = "sentiment"
    elif event.keysym == "c":
        data.mode = "pair"
        
def helpTimerFired(data):
    pass

def helpRedrawAll(canvas, data):
    canvas.create_text(100, data.height/2-40, text="Keyboard Shorcuts", font="Times 26 bold", anchor=W)
    canvas.create_text(100, data.height/2, text="Esc = Table of Contents", font="Times 20", anchor=W)
    canvas.create_text(100, data.height/2+20, text="H = Keyboard Shortcuts (Help)", font="Times 20", anchor=W)
    canvas.create_text(100, data.height/2+40, text="C = Charts", font="Times 20", anchor=W)
    canvas.create_text(100, data.height/2+60, text="S = Sentiment Analysis", font="Times 20", anchor=W)
    canvas.create_text(100, data.height/2+80, text="T = Trade", font="Times 20", anchor=W)
    canvas.create_text(100, data.height/2+100, text="P = Portfolio Review", font="Times 20", anchor=W)

####################################
# use the run function as-is
####################################
# still from class notes
def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600, 600)


