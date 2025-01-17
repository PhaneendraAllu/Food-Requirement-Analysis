from flask import Flask,render_template,request

import pickle
import numpy as np

model=pickle.load(open('num_orders.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    base_price=request.form['base_price']
    Dishes=request.form['Dishes']
    if(Dishes=="Beverages"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=1,0,0,0,0,0,0,0,0,0,0,0,0,0
    if(Dishes=="Extras"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,0,1,0,0,0,0,0,0,0,0,0,0
    if(Dishes=="Soup"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,0,0,0,0,0,0,0,0,0,0,1,0
    if(Dishes=="Other Snacks"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,0,0,0,1,0,0,0,0,0,0,0,0
    if(Dishes=="Salad"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,0,0,0,0,0,0,0,1,0,0,0,0
    if(Dishes=="Rice Bowl"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,0,0,0,0,0,0,1,0,0,0,0,0
    if(Dishes=="Starters"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,0,0,0,0,0,0,0,0,0,0,0,1
    if(Dishes=="Sandwich"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,0,0,0,0,0,0,0,0,1,0,0,0
    if(Dishes=="Pasta"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,0,0,0,0,1,0,0,0,0,0,0,0
    if(Dishes=="Desert"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,1,0,0,0,0,0,0,0,0,0,0,0
    if(Dishes=="Biryani"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,1,0,0,0,0,0,0,0,0,0,0,0,0
    if(Dishes=="Pizza"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,0,0,0,0,0,1,0,0,0,0,0,0
    if(Dishes=="Fish"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,0,0,1,0,0,0,0,0,0,0,0,0
    if(Dishes=="Sea Food"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14=0,0,0,0,0,0,0,0,0,0,0,1,0,0
        
    center_id=request.form['center_id']
        
    center_type=request.form['center_type']
    if(center_type=="TYPE_A"):
        a1,a2,a3=1,0,0
    if(center_type=="TYPE_B"):
        a1,a2,a3=0,1,0
    if(center_type=="TYPE_C"):
        a1,a2,a3=0,0,1
        
    checkout_price=request.form['checkout_price']
    
    city_code=request.form['city_code']
    
    cuisine=request.form['cuisine']
    if(cuisine=="continental"):
        b1,b2,b3,b4=1,0,0,0
    if(cuisine=="Indian"):
        b1,b2,b3,b4=0,1,0,0
    if(cuisine=="Italian"):
        b1,b2,b3,b4=0,0,1,0
    if(cuisine=="thai"):
        b1,b2,b3,b4=0,0,0,1
        
    emailer=request.form['emailer']
        
    homepage=request.form['homepage']
        
    id=request.form['id']    
    meal_id=request.form['meal_id']
    op_area=request.form['op_area']
    region_code=request.form['region_code']
    week=request.form['week']
    
    total=[[float(base_price),s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,int(center_id),a1,a2,a3,float(checkout_price),int(city_code),b1,b2,b3,b4,int(emailer),int(homepage),int(id),int(meal_id),float(op_area),int(region_code),int(week)]]
    y_pred=model.predict(np.array(total))
    
    
    print(y_pred)
    
    return render_template("index.html",showcase="num of orders per week:"+str(y_pred[0]))


if __name__=='__main__':
    app.run(debug=True)
    
        
    
    
