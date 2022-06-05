from flask import Flask,  render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    print('GET REQUEST SENT')
    return render_template('index.html')


@app.route('/', methods=['POST'])
def home2():
    dim1 = request.form['first_dim']
    dim2 = request.form['second_dim']
    dim3 = request.form['third_dim']
    volume = float(dim1) * float(dim2) * float(dim3)
    print()
    return render_template('index.html', output=volume)


app.run()
