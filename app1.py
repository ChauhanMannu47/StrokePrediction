from flask import Flask,render_template,request
import numpy as np
import sklearn
import pickle
import pandas as pd

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/bmi')
def bmi():
    return render_template('bmi.html')


@app.route('/predictAction', methods=['POST'])
def predictAction():
    if request.method == 'POST':
        name = request.form['name']
        age = (int(request.form['age']))
        maritalstatus = request.form['maritalstatus']
        worktype = request.form['Worktype']
        residence = request.form['Residence']
        gender = request.form['gender']
        bmi = (int(request.form['bmi']))
        gluclevel = (int(request.form['gluclevel']))
        smoke = request.form['Smoke']
        hypertension = request.form['Hypertension']
        heartdisease = request.form['Heartdisease']
        #model = open('strokenew.pkl', 'rb')

        res={'urban':1,'rural':0}
        gen={'Female':0,'Male':1}
        msts={'married':1,'not married':0}
        wktype={'privatejob':2,'govtemp':1,'selfemp':3}
        smke={'smoke_former':1,'smoke_never':2,'smoke_current':3}
        hypten={'hypten':1,'nohypten':0}
        hrtdis={'heartdis':1,'noheartdis':0}

        residence=res[residence]
        gender=gen[gender]
        maritalstatus=msts[maritalstatus]
        worktype=wktype[worktype]
        smoke=smke[smoke]
        hypertension=hypten[hypertension]
        heartdisease=hrtdis[heartdisease]



        if 15 <= bmi <= 26.9 and 70 <= gluclevel <= 107:
            if age < 40 and hypertension == 0 and smoke == 2 and heartdisease == 0 and residence == 1:
             result = 0
        elif 40 <= age <= 60 and hypertension == 0 and smoke == 2 and heartdisease == 0 and residence == 0:
            result = 0
        elif age > 60 and hypertension == 1 and heartdisease ==1:
            result = 1
        elif age > 60 and hypertension == 1 and smoke == 3 and heartdisease == 0:
            result = 1
        elif age > 60 and hypertension == 1 and smoke == 3 and heartdisease == 1:
            result = 1
        else:
            result = 0


        # Conditions for higher BMI or glucose levels for age greater than 60
        if (bmi > 26.9 or gluclevel > 107) and age > 60:
            if smoke == 3 and hypertension == 1 and heartdisease == 1:
                result = 1
            elif smoke == 3 and hypertension == 1 and heartdisease == 0:
                result = 1
            elif smoke == 3 and hypertension == 0 and heartdisease == 1:
                result = 1
            elif smoke == 1 and hypertension == 1 and heartdisease == 1:
                result = 1
            elif smoke == 1 and hypertension == 1 and heartdisease == 0:
                result = 1
            elif smoke == 1 and hypertension == 0 and heartdisease == 1:
                result = 1
            elif smoke == 1 and hypertension == 0 and heartdisease == 0:
                result =0
            elif smoke == 2 and hypertension == 1 and heartdisease == 1:
                result = 1
            elif smoke == 2 and hypertension == 1 and heartdisease == 0:
                result = 0
            elif smoke == 2 and hypertension ==0 and heartdisease == 0:
                result = 0


    # Conditions for higher BMI or glucose levels for age less than 60
        if (bmi > 26.9 or gluclevel > 107) and age < 60:
            if smoke == 3 and hypertension == 1 and heartdisease == 1:
               result = 1
            elif smoke == 3 and hypertension == 1 and heartdisease == 0:
               result = 1
            elif smoke == 3 and hypertension == 0 and heartdisease == 1:
               result = 1
            elif smoke == 1 and hypertension == 1 and heartdisease == 1:
               result = 1
            elif smoke == 1 and hypertension == 1 and heartdisease == 0:
               result = 1
            elif smoke == 1 and hypertension == 0 and heartdisease == 1:
               result = 1
            elif smoke == 1 and hypertension ==0 and heartdisease == 0:
               result = 0
            elif smoke == 2 and hypertension == 1 and heartdisease == 1:
               result =1
            elif smoke == 2 and hypertension == 1 and heartdisease == 0:
               result = 0
            elif smoke == 2 and hypertension == 0 and heartdisease == 0:
               result = 0
            else:
               result =0



        #model=pd.read_pickle('stroke_new.pkl')

        #array = [[gender,age,hypertension,heartdisease,maritalstatus,worktype,residence,gluclevel,bmi,smoke]]

        #array = [np.array(array[0],dtype = 'float64')]
        #pred_stroke = model.predict(array)
        #result = int(pred_stroke[0])
        #str=""
        if result==0:
            str = name + ", you will not get stroke 😀"
        else:
            str = name + ", you will get stroke 😔"
        return render_template('predict.html',a = str)

@app.route('/cta')
def cta():
    return render_template('cta.html')

@app.route('/counsel')
def counsel():
    return render_template('counsel.html')

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)