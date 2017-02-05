import os
if os.path.exists("data.txt"):
   fh=open("data.txt","r")
   print fh.read()
else:
   print "he"

