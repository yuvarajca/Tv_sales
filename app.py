from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))




@app.route('/', methods =['GET','POST'])
def input_tweet():
    
    if request.method == 'POST':
        tweet_in= request.form.get("tweet in")
        tweet_list=[]
        tweet_list.append(str(tweet_in))
        result = model.predict(tweet_list)
        return "Prediction: " + str(result)
    
    return render_template('index.html')
if __name__ == '__main__' :
    app.run()