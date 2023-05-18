from flask import Flask, jsonify, request
app = Flask(__name__)

List = [
    {
        'id' : 1,
        'name' : u'Jeff',
        'Contact' : u'981363748',
        'done' : False
    },
       {
        'id' : 2,
        'name' : u'Maria',
        'Contact' : u'3785873467',
        'done' : False
    }
]
@app.route("/add-data", methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message" : "Please provide the data!"
        }, 400)


    contact = {
        'id' : task [-1] ['id'] + 1,
        'name' :request.json['Name'],
        'Contact' : request.json.get('Contact', "")
        'done' : False
    }
    List.append(Contact)
    return jsonify({
       "status": "succese",
      "message": "contact added succesfuly"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : List
    })

if (__name__ == "__main__"):
    app.run(debug = True)