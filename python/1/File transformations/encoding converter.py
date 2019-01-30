import sys

encInp, encOut, filename = sys.argv[1], sys.argv[2], sys.argv[3]
try:
  with open(filename, encoding=encInp) as r:
    tiedosto = r.read()
    r.close()
    
  with open(filename, mode='w', encoding=encOut) as w:
    w.write(tiedosto)
    
except OSError:
  print("Error opening {}".format(filename))
except UnicodeDecodeError:
  print("Error reading {} with {}".format(filename, encInp))
except UnicodeEncodeError:
  print("Error writing {} with {}".format(filename, encOut))