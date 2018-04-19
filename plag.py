from flask import Flask ,render_template,request
app = Flask(__name__,template_folder="templates")

file=open("text1.txt","r")
text1=[]
for line in file:
   text1.append(line.strip())

file=open("text2.txt","r")
text2=[]
for line in file:
   text2.append(line.strip())

file=open("text3.txt","r")
text3=[]
for line in file:
   text3.append(line.strip())

@app.route('/')
def hello_world():
    header="<h3>hello,world!</h3><br>Welcome to the plagairism checker"
    linktext="click<a href='/check'>here</a> to use it"
    return header+linktext

@app.route('/check',methods=['GET','POST'])
def check():
    if request.method=="POST":
         response=""
         text=request.form["p_text"]
         lines=text.split('\n')
         textlength=len(lines)
         rendertext=""
         for line in lines:
              rendertext = rendertext+'<br>'+line
         response="given text has"+rendertext

         matches=0
         database=[text1,text2,text3]
         for file in database:
             for line in lines:
                if line.strip() in file:
                     matches+=1

         p_percent=(float(matches)/textlength)*100
         p_output="The given text has <b>"+str(p_percent)+" %</b> plagairised text"
         response= response+p_output
         return response

    else:
        return render_template("plag.html")

if __name__=='__main__':
     app.run(debug=True)
