from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/userstatic')
# def user():
#     return {
#         "name":"teguh",
#         "age":25,
#         "hobbies":["eat","sleep","learning"]
#     }

    

if __name__ == '__main__':
    app.run(debug=True)