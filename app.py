from flask import Flask, request,render_template
from pymongo import MongoClient
app=Flask("myiiec")
@app.route('/form')
def myform():
    return render_template("basic.html")
    


@app.route('/data',methods=['POST'])
def mydata():
    if request.method=='POST':
       global data1
       data1=request.form.get('x')
       
       db=[
         {
        "name": data1
          }
            ]
       client= MongoClient("mongodb://127.0.0.1:27017")
       client['lw']['agg_alternative_1'].insert(db)

    return data1




app.run(port=1234,debug=True)
