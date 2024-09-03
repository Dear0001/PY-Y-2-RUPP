from flask import Flask,render_template, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import io
from num6 import Num
from data6 import data1
app = Flask(__name__)
app.debug = True
@app.route('/')
def home():
  num6 = Num()
  data6 = data1
  x = [i[0] for i in data1]
  y = [i[1] for i in data1]
  n = len(data1)
  a,b,fit = num6.least_square_line(x,y)
  predicted_y_hat = [round((a+(b*i)),4) for i in x]
  #Residual
  residual = [round((y[i]-predicted_y_hat[i]),4) for i in range(n)]
  #SSResid sum((y-y_hat)^2)
  SSResid = sum([u**2 for u in residual ])
  #SSTo sum((y-y_mean)^2)
  y_mean = num6.mean(y)
  SSTo = sum((u - y_mean)**2 for u in y)
  r_square = round((1-(SSResid/SSTo)),2)
  se = round((SSResid/(n-2))**0.5,4)
  data = list(map(list,zip(x,y,predicted_y_hat,residual)))
  #print(f'a={a}, b={b}, {fit}')
  return render_template('index6.html',data=data,fit=fit,se=se,r_square=r_square,SSResid=SSResid,SSTo=SSTo)
@app.route('/plot.png')
def plot_png():
  data=data1
  fig = create_figure(data1)
  output = io.BytesIO()
  FigureCanvas(fig).print_png(output)
  return Response(output.getvalue(), mimetype='image/png')
def create_figure(data1):
  num6=Num()
  x = [i[0] for i in data1]
  y = [i[1] for i in data1]
  a,b,fit = num6.least_square_line(x,y)

  fig = Figure(figsize=(16,6))
  ax1 = fig.add_subplot(1, 2, 1)
  ax1.scatter(x,y,c='r',marker='o',alpha=1,label = r'$x,y$')
  ax1.legend()

  x = np.array([i[0] for i in data1])
  ax1.plot(x,a+b*x,'-', c='blue')
  ax1.set_xlabel("x")
  ax1.set_ylabel("y")
  ax1.set_title("Scatter plot")

  n=len(x)
  predicted_y_hat = [round((a+(b*i)),4) for i in x]
  #Residual
  residual = [round((y[i]-predicted_y_hat[i]),4) for i in range(n)]

  ax2 = fig.add_subplot(1, 2, 2)
  ax2.scatter(x,residual,c='b',marker='x',alpha=1,label = r'$x,residual$')
  ax2.legend()
  ax2.set_xlabel('x')
  ax2.set_ylabel('residual')
  ax2.set_title("Residual plot")
  return fig
if __name__ == '__main__':
  app.run(host='localhost', port=8080)