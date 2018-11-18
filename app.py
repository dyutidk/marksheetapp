from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('marksheet.html')

def getPercent(m,t):
    p=int(m)/int(t)*100
    return p

def grade(p):
    
    if(p>95):
        g="S"
    elif(p>90):
        g="A+"
    elif(p>85):
        g="A"
    elif(p>80):
        g="B+"
    elif(p>75):
        g="B"
    elif(p>70):
        g="C+"
    elif(p>65):
        g="C"
    elif(p>60):
        g="D+"
    elif(p>55):
        g="D"
    elif(p<50):
        g="F"
    return g

@app.route('/result',methods=['GET','POST'])
def result():
    if(request.method=='POST'):
        getName=request.form['name']
        getRegNo=request.form['regno']
        getsem=request.form['semester']
        getcol=request.form['college']
        getsname1=request.form['subject1']
        getsmark1=request.form['mark1']
        getstotal1=request.form['t1']
        getsname2=request.form['subject2']
        getsmark2=request.form['mark2']
        getstotal2=request.form['t2']
        getsname3=request.form['subject3']
        getsmark3=request.form['mark3']
        getstotal3=request.form['t3']
        getsname4=request.form['subject4']
        getsmark4=request.form['mark4']
        getstotal4=request.form['t4']
       
        g1=grade(getPercent(getsmark1,getstotal1))
        g2=grade(getPercent(getsmark2,getstotal2))
        g3=grade(getPercent(getsmark3,getstotal3))
        g4=grade(getPercent(getsmark4,getstotal4))
        if(g1=="F" or g2=="F" or g3=="F" or g4=="F"):
            status="Failed"
        else:
            status="Pass"
        return render_template('result.html',n=getName,r=getRegNo,s=getsem,c=getcol,s1=getsname1,s1m=getsmark1,s1t=getstotal1,s2=getsname2,s2m=getsmark2,s2t=getstotal2,s3=getsname3,s3m=getsmark3,s3t=getstotal3,s4=getsname4,s4m=getsmark4,s4t=getstotal4,g1=g1,g2=g2,g3=g3,g4=g4,status=status)

if(__name__=='__main__'):
    app.run(debug=True)