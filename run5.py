from flask import Flask,render_templates, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import io
from num5 import Num
from data5 import data
app = Flask(__name__)
app.debug = True
@app.route('/')
def home():
  num = Num()
  x = [i[0] for i in data]
  y = [i[1] for i in data]
  r = num.correlation(x,y)
  a,b = fit_line(x,y)
  return render_template('index5.html',data=data,a=a,b=b,r=r)
@app.route('/plot.png')
def plot_png():
  fig = create_figure(data)
  output = io.BytesIO()
  FigureCanvas(fig).print_png(output)
  return Response(output.getvalue(), mimetype='image/png')
def fit_line(x,y):
  num = Num()
  sum_x = sum(x)
  sum_y = sum(y)
  sum_x2 = sum([i**2 for i in x])
  sum_xy = sum(u*v for u,v in data)
  mean_x = num.mean(x)
  mean_y = num.mean(y)
  n = len(data)
  b1 = sum_xy - (sum_x*sum_y)/n
  b2 = sum_x2 - ((sum_x)**2)/n
  b = b1/b2
  a = mean_y - b*mean_x
  return (a,b)
def create_figure(data):
  x = [i[0] for i in data]
  y = [i[1] for i in data]
  a,b = fit_line(x,y)
  fig = Figure()
  
  axis = fig.add_subplot(1, 1, 1)
  axis.scatter(x,y,c='red',marker='o',alpha=0.7)
  x = np.array([i[0] for i in data])
  axis.plot(x,a+b*x,'-', c='blue')
  axis.set_title("Scatter plot")
  axis.set_xlabel("x")
  axis.set_ylabel("y")
  return fig
if __name__ == '__main__':
  app.run(host='localhost', port=8080)