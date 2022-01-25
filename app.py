from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))




@app.route('/', methods =['GET','POST'])
def input_tv():
    
    if request.method == 'POST':
        tv_sales= request.form.get("tv sales")
        tv_list=[[]]
        tv_list[0].append(float(tv_sales))
        result = model.predict(tv_list)
        return "Prediction: " + str(result) 
    return render_template('index.html')

if __name__ == '__main__' :
    app.run()