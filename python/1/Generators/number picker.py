def pickNumbers(vals):
  with open(vals) as r:
    tiedosto = r.read().replace('\n'," ").split(' ')
  for x in tiedosto:
    try:
      yield float(x)
    except:
      pass