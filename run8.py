from flask import Flask,render_template, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
import io
app = Flask(__name__)
app.debug = True
data = pd.read_csv('data8.csv',sep=',',usecols=['x','y'])
x = data['x'].tolist()
y = data['y'].tolist()
r = np.corrcoef(x,y)[0,1]
n = len(data)
#calculate regression line
a,b1,b2 = np.polynomial.polynomial.polyfit(x,y,deg=2)
@app.route('/')
def home():
  fit = f"y\u0302 = {a:.3f}{'+' if b1>=0 else ''}{b1:.3f}x{'+' if b2>=0 else ''}{b2:.3f}x\u00b2"
  predicted_y_hat = [round((a+(b1*i)+(b2*i**2)),4) for i in x]
  
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
  return render_template('index8.html',data=data_new,fit=fit,r=r,se=se,r_square=r_square,SSResid=SSResid,SSTo=SSTo)
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
  ax1.plot(x,a+b1*x_arr+b2*(x_arr**2),'-', c='blue',label= f"y\u0302 ={a:.3f}{'+' if b1>=0 else ''}{b1:3f}x{'+' if b2>=0 else ''}{b2:.3f}x\u00b2")
  ax1.set_xlabel("x")
  ax1.set_ylabel("y")
  ax1.set_title("Scatter plot")
  ax1.legend()
 
  predicted_y_hat = [round((a+(b1*i)+(b2*i**2)),4) for i in x]
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