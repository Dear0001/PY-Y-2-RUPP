class Num:
  def __init__(self,ls=None):
    self.ls=ls
  def mean(self, data = None):
    lst=data if data else self.ls
    n = len(lst)
    s = sum(lst)
    return s/n if n>0 else float('Nan')

  def median(self, data = None):
    lst = sorted(data) if data else sorted(self.ls)
    n = len(lst)
    mid = (n)//2
    return lst[mid] if n%2 else (lst[mid-1] + lst[mid])/2

  def deviation_from_mean(self, data = None):
    lst = sorted(data) if data else sorted(self.ls)
    m = self.mean(lst)
    return [x-m for x in lst]
  def sample_variant(self, data = None):
    lst = data if data else self.ls
    m = self.mean(lst)
    return sum([(x-m)**2 for x in lst])/(len(lst) -1)

  def standard_deviation(self, data = None):
    lst = data if data else self.ls
    m = self.mean(lst)
    return (sum([(x-m)**2 for x in lst])/(len(lst) -1)) ** (0.5)

  def iqr(self, data = None):
    lst = sorted(data) if data else sorted(self.ls)
    n = len(lst)
    lower,upper = (lst[0:n//2],lst[n//2+1:]) if n%2 else (lst[0:n//2],lst[n//2:])
    q1 = self.median(lower)
    q3 = self.median(upper)
    return q3 - q1

  def zscore(self, data = None):
    lst = data if data else self.ls
    m = self.mean(lst)
    s = self.standard_deviation(lst)
    return [((u - m)/s) for u in lst]

  def correlation(self,x=None,y=None):
    zx = self.zscore(x)
    zy = self.zscore(y)
    zxzy = [x*y for x,y in zip(zx,zy)]
    d = list(map(list,zip(x,y,zx,zy,zxzy)))
    s = sum(float(u[2])*float(u[3]) for u in d)
    n = len(d)
    r = s/(n-1)
    return r
  def least_square_line(self,x,y):
    data = list(map(list,zip(x,y)))
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum([i**2 for i in x])
    sum_xy = sum( i*j for i,j in data)
    mean_x = self.mean(x)
    mean_y = self.mean(y)
    n = len(data)
    b1 = sum_xy - (sum_x*sum_y)/n
    b2 = sum_x2 - ((sum_x)**2)/n

    b = round(b1/b2,4)
    a = round(mean_y - b*mean_x,4)
    st = f'{a}+{b}x' if b>=0 else f'{a}{b}x'
    return [a,b,f'y\u0302 = {st}']