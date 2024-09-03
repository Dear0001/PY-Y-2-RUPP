from flask import Flask,render_template, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
import io
app = Flask(__name__)
app.debug = True
data = pd.read_csv('data7.csv',sep=',',usecols=['x','y'])
x = data['x'].tolist()
y = data['y'].tolist()
r = np.corrcoef(x,y)[0,1]
n = len(data)
#calculate least-square line
a,b = np.polynomial.polynomial.polyfit(x,y,deg=1)
@app.route('/')
def home():
  fit = f'y\u0302 = {a:.2f} + {b:.2f}x' if b>=0 else f'y\u0302 = {a:.2f}{b:.2f}x'
  predicted_y_hat = [round((a+(b*i)),4) for i in x]
  #Residual
  residual = [round((y[i]-predicted_y_hat[i]),4) for i in range(n)]
  #SSResid sum((y-y_hat)^2)
  SSResid = sum([u**2 for u in residual ])
  #SSTo sum((y-y_mean)^2)
  y_mean = np.mean(y)
  SSTo = sum((u - y_mean)**2 for u in y)
  r_square = round((1-(SSResid/SSTo)),2)
  se = round((SSResid/(n-2))**0.5,4)
  data_new = list(map(list,zip(x,y,predicted_y_hat,residual)))
  #print(f'a={a}, b={b}, {fit}')
  return render_template('index7.html',data=data_new,fit=fit,r=r,se=se,r_square=r_square,SSResid=SSResid,SSTo=SSTo)
@app.route('/plot.png')
def plot_png():
  fig = create_figure()
  output = io.BytesIO()
  FigureCanvas(fig).print_png(output)
  return Response(output.getvalue(), mimetype='image/png')
def create_figure():
  fig = Figure(figsize=(16,6))
  ax1 = fig.add_subplot(1, 2, 1)
  ax1.scatter(x,y,c='r',marker='o',alpha=1,label = r'$x,y$')
  ax1.legend()

  x_arr = np.array(x)
  ax1.plot(x,a+b*x_arr,'-', c='blue')
  ax1.set_xlabel("x")
  ax1.set_ylabel("y")
  ax1.set_title("Scatter plot")
  predicted_y_hat = [round((a+(b*i)),4) for i in x]
  #Residual
  residual = [round((y[i]-predicted_y_hat[i]),4) for i in range(n)]

  ax2 = fig.add_subplot(1, 2, 2)
  ax2.scatter(x,residual,c='b',marker='x',alpha=1,label =
  r'$x,residual$')
  ax2.legend()
  ax2.set_xlabel('x')
  ax2.set_ylabel('residual')
  ax2.set_title("Residual plot")
  return fig
if __name__ == '__main__':
 app.run(host='localhost', port=8080)