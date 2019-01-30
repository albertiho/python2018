import sys
import string

fileIn, fileOut = sys.argv[1], sys.argv[2]
enc = "utf-8"
with open(fileIn, encoding =enc) as i:
  tiedosto = i.read()
  i.close()

outp, check = "", []
for x in tiedosto:
  if x not in string.whitespace and x not in check:
      outp = outp + x + " "
      check.append(x)
    
with open(fileOut, mode='w', encoding=enc) as o:
  o.write(outp[:len(outp)-1] + '\n')