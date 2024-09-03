from flask import Flask,render_template
from num2 import Num
app = Flask(__name__)
@app.route('/')
def home():
  nm = Num()
  data = [1200,1300,2300,3200,3300,3800,4000,4100,4300,4800,5500,5700,5700,5800,6000,6300,6800,6800,6900,7700]
  mean=nm.mean(data)
  median=nm.median(data)
  return render_template('index2.html',data=data,mean=mean,median=median)
if __name__ == '__main__':
  app.run(host='localhost', port=8080)
