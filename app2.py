from flask import Flask,jsonify,request


app= Flask(__name__)



@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        some_json = reguest.get_json()
        return jsonify({'you sent':some_json}),201
    else:
        return jsonify({'about':'helo world'})
        

@app.route('/multiply/<int:number>', methods=['GET'])
def multiply(number):
    return jsonify({'result':number*10})

if __name__=='__main__':
    app.run(debug=True)