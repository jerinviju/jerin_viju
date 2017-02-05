import sys
from Class import node 
from reportlab.pdfgen import canvas
import os
import json
from importlib import import_module

movie=""
duration=""
stars=""
num=""
cont=""
simplelist=[]
i=1
j=1
objforpass=node("","","","")
c=canvas.Canvas("output/data.pdf")



def getdata():
	movie = raw_input("Please enter the name of the film: ")
	
	duration = raw_input("Please enter the duration of the film: ")
	
	stars = raw_input("Please enter the name of the actors with , seperation: ")
	
	num = raw_input("Please enter the format of the file to be saved(1-plaintext,2-pdf,3-plugins): ")
        
        cont = raw_input("Do you want to continue(y|n): ")
        newnode=node(movie,duration,stars,num)
        simplelist.append(newnode)
        print "\n\n"
        if cont=="y":
             
             getdata()
        else:
             filetype()
       
def filetype():
        global simplelist
        global c
        for ele in simplelist:
             
            
             if ele.num=="1":
                 plaintxt(ele)
             elif ele.num=="2":
                 pdf(ele)
             else:
                 reflection(ele)
        c.save()

def plaintxt(data):
        global i
      
        f=open("output/data.txt","a+")  
        f.write("Movie %d\r\n"%i)
        i=i+1
        f.write("Name of the movie: %s\n" %data.movie)
        f.write("duration of the movie: %s\n"%data.duration)
        f.write("actors of the movie: %s\n"%data.stars)
        f.write("\n")
        f.close
        print "check the output folder for plaintext"
             


def pdf(data):
        global j
        global c
        c.drawString(3,800-((j-1)*50),"Movie %d"%j)
        c.drawString(3,800-(((j-1)*50)+10),"Name of the Movie: %s"%data.movie)
        c.drawString(3,800-(((j-1)*50)+20),"Duration of the Movie: %s"%data.duration)       
        c.drawString(3,800-(((j-1)*50)+30),"Stars of the Movie: %s"%data.stars)
        j=j+1
        print "check the output folder for pdf"
     

def reflection(data):
        flag=0
        
        num=1
        for f in os.listdir("plugins/"):
             child=os.path.join("plugins/",f)     
            
             if os.path.exists(child+"/manifest.json"):
                 
                 flag=1
                 Json=json.loads(open(child+"/manifest.json").read())
                 
                 
                 try:
                            
                     print Json["name"]+"-%d"%num
                     num=num+1
                 except Exception:

                     print "please check your manifest"
              
                       
            
        if flag==0:
             print "srry there is no plugins available now\n"
             nums = raw_input("please choose plaintext|pdf (1|2): ")
             if nums=="1":
                  plaintxt(data)
             elif nums=="2":
                  pdf(data)
        else:
             z=1
             option= input("Choose your plugin: ")
             for f in os.listdir("plugins/"):
                  
                  if option==z:
                      
                      plugin=os.path.join("plugins/",f) 
                      Json=json.loads(open(plugin+"/manifest.json").read())
                      f=open(plugin+"/data.txt","a+")  
                           
        
                      f.write("Name of the movie: %s\n" %data.movie)
                      f.write("duration of the movie: %s\n"%data.duration)
                      f.write("actors of the movie: %s\n"%data.stars)
         
                      f.close
                      try:
                           
                          x=Json["classname"]
                          
                          import_module(x) 
                         
                      except Exception:

                          print "please check your manifest"
                      break
                  else:
                      z=z+1
              
  
getdata()
