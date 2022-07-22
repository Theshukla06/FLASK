from flask import Flask
app = Flask(__name__)

@app.route('/')
def Ankit_shukla():
    return 'Ankit Shukla'

if __name__ == "__main__":
    app.run(debug=True)