## API example. We need a POST method to save data to DB

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    if(request.method == 'POST'):
        jsonData = request.get_json()
        ### ADD jsonData to DB before return request
        ### Calculate score and send it back on return statement
        return jsonify({'FACT OR FAKE' : jsonData}), 201
    else:
        ##For GET request, send back score for the url
        return jsonify({"about": "get request"})

if __name__ == '__main__':
    app.run(debug=True)