from flask import Flask, request, render_template
from os import listdir

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/AddTime', methods=['GET','POST'])
def Add_time():
    rec_dur = request.form.get('recdur')
    rec_ti = request.form.get('rectime')
    if request.method == 'POST':
        with open("RECTIME.txt", 'a') as Fa: 
            Fa.write(str(rec_ti + " " + rec_dur +"\n"))
    return render_template('AddTime.html')

@app.route('/Remove', methods=['GET','POST'])
def Remove():
    rem_dur = request.form.get('remdur')
    rem_ti = request.form.get('remtime')
    if request.method == 'POST':
        with open('RECTIME.txt', 'r') as file :
            filedata = file.read()
            filedata = filedata.replace(str(rem_ti+" "+rem_dur+"\n"), '')
        with open('RECTIME.txt', 'w') as file:
            file.write(filedata)
    return render_template('Remove.html')

@app.route('/Preview') 
def content(): 
	with open('RECTIME.txt', 'r') as f: 
		return render_template('Preview.html', text=f.read())



if __name__ == '__main__':
    app.debug = True
    app.run()
