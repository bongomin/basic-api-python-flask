from flask import Flask,render_template,jsonify


app=Flask(__name__)



@app.route('/')
def hello():
    return jsonify({'about':'hello boss'})




if __name__=="__main__":
    app.run(debug=True)


    