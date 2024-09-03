class Num:
  def __init__(self,ls=None):
    self.ls=ls
 
  def mean(self, data = None):
    lst=data if data else self.ls
    n = len(lst)
    s = sum(lst)
    return s/n if n>0 else float('nan')
 
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