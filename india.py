import os
if os.path.exists("plugins/hhehe/data.txt"):
   fh=open("plugins/hhehe/data.txt","r")
   print fh.read()
else:
   print "he"

