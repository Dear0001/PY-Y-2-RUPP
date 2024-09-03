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