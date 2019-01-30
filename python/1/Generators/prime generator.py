def primes(amt, lb=2):
  d, q = {}, 2
  
  while(amt > 0):
    if q not in d:
      if q >= lb:
        yield q
        amt -= 1
      d[q * q] = [q]
    else:
      for p in d[q]:
        d.setdefault(p + q, []).append(p)
      del d[q]
    q += 1