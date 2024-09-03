from flask import Flask,render_template
from num4 import Num
from data4 import data
app = Flask(__name__)
app.debug = True
@app.route('/')
def home():
  num = Num()
  x = [u[0] for u in data]
  y = [u[1] for u in data]
    #x_mean = num.mean(x)
    #y_mean = num.mean(y)
    #x_std = num.standard_deviation(x)
    #y_std = num.standard_deviation(y)
    #zx = [(u-x_mean)/x_std for u in x]
    #zy = [(u-y_mean)/y_std for u in y]
  zx = num.zscore(x)
  zy = num.zscore(y)
  zx=[f'{u:.3f}' for u in zx]
  zy=[f'{u:.3f}' for u in zy]
  d = list(map(list,zip(x,y,zx,zy)))
  s = sum(float(u[2])*float(u[3]) for u in d)
  n = len(d)
  r = s/(n-1)
  return render_template('index4.html',d=d,r=r)
if __name__ == '__main__':
  app.run(host='localhost', port=8080)