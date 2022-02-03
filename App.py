from flask import Flask , jsonify , request
from Data import final_dict
app = Flask(__name__)
@app.route("/")
def index():
    return jsonify({"data":final_dict,"message":"success"}),200
@app.route("/star")
def star():
    name= request.args.get("name")
    star_data = next(final_dict[item] for item in final_dict if item == name)
    print(star_data)
    return jsonify({"data":star_data,"message":"success"}),200
if __name__ == "__main__":
    app.run()