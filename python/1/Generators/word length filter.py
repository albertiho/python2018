def wordLenFilter(vals, l):
  with open(vals) as r:
    tiedosto = r.read().replace("\n"," ").split(" ")
  for x in tiedosto:
    if len(x) == l:
      yield x