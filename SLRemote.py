from flask import Flask, render_template, request, redirect, url_for
from forms import RemoteForm, TestForm
from utils_light import *

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))




@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def remote():
    form = RemoteForm()
    print('inside quick add routes')
    if form.validate_on_submit(): 
        print('form test msg:')

        print(form.brightness.data)
        change_pattern(form.pattern.data)
        change_brightness(float(form.brightness.data))
        change_color(float(form.color.data))
        change_speed(float(form.speed.data))
        turn_on(form.on_off.data)
     
        if form.clip1.data:
            print('clip1')
            return redirect(url_for('remote'))
        if form.clip2.data:
            print('clip2')
            return redirect(url_for('remote'))
        if form.clip3.data:
            print('clip3')
            return redirect(url_for('remote'))
        if form.submit.data:
            print(('submit'))
            return redirect(url_for('remote'))

    return render_template('remote.html', form=form)

@app.route('/test', methods=['GET', 'POST'])
def test():
    form = TestForm(csrf_enabled=False)
    print(form.age.data)

    if form.validate():
        


        print(request.form["name_of_slider"])
        print('form test msg:')
        print(form.age.data)
        
        #print(request.form["outputtest"])
        return redirect(url_for('main.test'))

    return render_template('test.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
