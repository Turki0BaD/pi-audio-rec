from flask import Flask, request, render_template

# Starting the web page
app = Flask(__name__)


# The main page
@app.route('/')
def my_form():
    return render_template('index.html')


# The add a new recording time and duration
# As well as the code to open and modify the .txt file
@app.route('/AddTime', methods=['GET', 'POST'])
def Add_time():
    # rec_dur and rec_ti is getting data from the HTML Page
    rec_dur = request.form.get('recdur')
    rec_ti = request.form.get('rectime')
    if request.method == 'POST':
        with open("RECTIME.txt", 'a') as Fa:
            Fa.write(str("\n" + rec_ti + " " + rec_dur))
    return render_template('AddTime.html')


# The remove page and the code to read ,confirm
# and the remove the time and duration
@app.route('/Remove', methods=['GET', 'POST'])
def Remove():
    # rem_dur and rem_ti is getting data from the HTML Page
    rem_dur = request.form.get('remdur')
    rem_ti = request.form.get('remtime')
    if request.method == 'POST':
        with open('RECTIME.txt', 'r') as file:
            filedata = file.read()
            filedata = filedata.replace(str(rem_ti + " " + rem_dur), '')
        with open('RECTIME.txt', 'w') as file:
            file.write(filedata)
    return render_template('Remove.html')


# getting data from the .txt file and display it
@app.route('/Preview')
def content():
    with open('RECTIME.txt', 'r') as f:
        return render_template('Preview.html', text=f.read())


# Uploading the web page for use
if __name__ == '__main__':
    # The given IP allows us to upload the page over the network
    app.run(debug=True, host='0.0.0.0')
