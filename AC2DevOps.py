import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')


def ehprimo(primo):
    for i in range(2, primo+1):
        if i != primo:
            i = primo % i
            if i == 0:
                return False
                break
        else:
            return True
            break
cont = 0
num = 2
while cont <= 100:
    if ehprimo(num) == True:
        print(num)
        cont += 1
    num = num + 1
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

