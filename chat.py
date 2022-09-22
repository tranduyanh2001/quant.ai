import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from gtts import gTTS
import os
import yfinance as yf

language = 'en'
with open('intents.json', 'r') as f:
    intents = json.load(f)

FILE = "stock_data.pth"

data = torch.load(FILE)

input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']

model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()

#asking user what stock they want to know about
bot_name = "quant.AI"
print("Let's chat! Type 'quit' to exit.")
user_stock = input("What stock ticker do you want to know about? Only type the ticker letters:  ")
ticker = yf.Ticker(user_stock)
stock_data = {
    'industry' : ticker.info['industry'],
    'sector': ticker.info['sector'],
    'profitMargins' : ticker.info['profitMargins'],
    'recommendation' : ticker.info['recommendationKey'],
    'currentPrice' : ticker.info['currentPrice'],
    'returnOnEquity' : ticker.info['returnOnEquity'],
    'full_name' : ticker.info['longName'],
    'opening_price' : ticker.info['open'],
    'averageVolume' : ticker.info['averageVolume'],
    'dayLow' : ticker.info['dayLow']
}

#start of NLP task
while True:
    sentence = input('You: ')
    if sentence =='quit':
        break
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0]) #1 row since 1 saMPLE
    #convert to torch tensor
    X = torch.from_numpy(X)

    output = model(X) #gives us prediction
    #outputs the index of the max value and the max value itself
    _, predicted = torch.max(output, dim=1)
    #tag as the key of the maximum value
    tag = tags[predicted.item()] 

    #check if probabgility for tag is high enough
    probs = torch.softmax(output, dim=1)
    #actual prob for this predictedf tag
    prob = probs[0][predicted.item()]

    if prob.item()> 0.55:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                if tag == "current price":
                    mytext = random.choice(intent['responses']) + str(stock_data.get('currentPrice'))
                    #print(f"{bot_name}: {random.choice(intent['responses'])}")
                    myobj = gTTS(text=mytext, lang=language, slow=False)
                    myobj.save("welcome.mp3")
                    # Playing the converted file
                    os.system("welcome.mp3")
                    print(f"{bot_name}: {mytext}")
                elif tag == "sector":
                    mytext = random.choice(intent['responses']) + str(stock_data.get('sector'))
                    #print(f"{bot_name}: {random.choice(intent['responses'])}")
                    myobj = gTTS(text=mytext, lang=language, slow=False)
                    myobj.save("welcome.mp3")
                    # Playing the converted file
                    os.system("welcome.mp3")
                    print(f"{bot_name}: {mytext}")
                elif tag == "recommendation":
                    mytext = random.choice(intent['responses']) + str(stock_data.get('recommendation'))
                    #print(f"{bot_name}: {random.choice(intent['responses'])}")
                    myobj = gTTS(text=mytext, lang=language, slow=False)
                    myobj.save("welcome.mp3")
                    # Playing the converted file
                    os.system("welcome.mp3")
                    print(f"{bot_name}: {mytext}")
                elif tag == "full_name":
                    mytext = random.choice(intent['responses']) + str(stock_data.get('full_name'))
                    #print(f"{bot_name}: {random.choice(intent['responses'])}")
                    myobj = gTTS(text=mytext, lang=language, slow=False)
                    myobj.save("welcome.mp3")
                    # Playing the converted file
                    os.system("welcome.mp3")
                    print(f"{bot_name}: {mytext}")
                elif tag == "returnOnEquity":
                    mytext = random.choice(intent['responses']) + str(stock_data.get('returnOnEquity'))
                    #print(f"{bot_name}: {random.choice(intent['responses'])}")
                    myobj = gTTS(text=mytext, lang=language, slow=False)
                    myobj.save("welcome.mp3")
                    # Playing the converted file
                    os.system("welcome.mp3")
                    print(f"{bot_name}: {mytext}")
                elif tag == "industry":
                    mytext = random.choice(intent['responses']) + str(stock_data.get('industry'))
                    #print(f"{bot_name}: {random.choice(intent['responses'])}")
                    myobj = gTTS(text=mytext, lang=language, slow=False)
                    myobj.save("welcome.mp3")
                    # Playing the converted file
                    os.system("welcome.mp3")
                    print(f"{bot_name}: {mytext}")                                                             
                elif tag == "profitMargins":
                    mytext = random.choice(intent['responses']) + str(stock_data.get('profitMargins'))
                    #print(f"{bot_name}: {random.choice(intent['responses'])}")
                    myobj = gTTS(text=mytext, lang=language, slow=False)
                    myobj.save("welcome.mp3")
                    # Playing the converted file
                    os.system("welcome.mp3")
                    print(f"{bot_name}: {mytext}")                                                             
                elif tag == "opening_price":
                    mytext = random.choice(intent['responses']) + str(stock_data.get('opening_price'))
                    #print(f"{bot_name}: {random.choice(intent['responses'])}")
                    myobj = gTTS(text=mytext, lang=language, slow=False)
                    myobj.save("welcome.mp3")
                    # Playing the converted file
                    os.system("welcome.mp3")
                    print(f"{bot_name}: {mytext}")                                                             
                elif tag == "averageVolume":
                    mytext = random.choice(intent['responses']) + str(stock_data.get('averageVolume'))
                    #print(f"{bot_name}: {random.choice(intent['responses'])}")
                    myobj = gTTS(text=mytext, lang=language, slow=False)
                    myobj.save("welcome.mp3")
                    # Playing the converted file
                    os.system("welcome.mp3")
                    print(f"{bot_name}: {mytext}")
                elif tag == "dayLow":
                    mytext = random.choice(intent['responses']) + str(stock_data.get('dayLow'))
                    #print(f"{bot_name}: {random.choice(intent['responses'])}")
                    myobj = gTTS(text=mytext, lang=language, slow=False)
                    myobj.save("welcome.mp3")
                    # Playing the converted file
                    os.system("welcome.mp3")
                    print(f"{bot_name}: {mytext}")  
                else:
                    mytext = random.choice(intent['responses'])
                    #print(f"{bot_name}: {random.choice(intent['responses'])}")
                    myobj = gTTS(text=mytext, lang=language, slow=False)
                    myobj.save("welcome.mp3")
                    # Playing the converted file
                    os.system("welcome.mp3")
                    print(f"{bot_name}: {mytext}")                                                      
    else:
        mytext = "I do not understand"
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("welcome.mp3")

        # Playing the converted file
        os.system("welcome.mp3")
        print(f"{bot_name}: {mytext}")
        #print(f"{bot_name}: I do not understand...")