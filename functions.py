def klarge(k,lisip):
  lis=list(set(lisip))
  lis.sort(reverse=True)
  return lis[k-1]