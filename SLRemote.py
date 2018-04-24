from flask import Flask, render_template, request, redirect, url_for
from forms import RemoteForm, TestForm
from utils_light import *

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))


output_on_osc_route = '/lx/output/enabled'
channel_1_pattern_osc_route = '/lx/channel/1/activePattern'
color_osc_route = '/lx/palette/color/hue'
speed_osc_route = '/lx/engine/speed'
blur_osc_route = '/lx/channel/1/effect/1/amount/'
bright_osc_route = '/lx/output/brightness'

patterns_full = ['AskewPlanes', 'Balance', 'Ball', 'BassPod', 'Blank', 'Bubbles', 'CrossSections', 'CubeEQ', 
                 'CubeFlash', 'Noise', 'Palette', 'Pong', 'Rings', 'ShiftingPlane', 'SoundParticles', 'SpaceTime',
                'Spheres', 'StripPlay', 'Swarm', 'Swim', 'TelevisionStatic', 'Traktor', 'ViolinWave']

patterns_lower = [x.lower() for x in patterns_full]
color_labels_encoding = ['red', 'orange', 'yellow', 'green', 'teal', 'blue', 'purple', 'magenta']
speed_labels = ['slow', 'medium', 'fast']
effect_labels = ['low', 'medium', 'high']
brightness_labels = ['off', 'dim', 'down', 'half', 'up', 'full', 'bright']

bright_unencode = [0.0, 0.3, 0.3, 0.5, 0.7, 1.0, 1.0]
speed_unencode = [0.2, 0.5, 0.8]
color_unencode = [0.0, 0.08, 0.15, 0.35, 0.48, 0.67, 0.76, 0.84]
effect_unencode = [0.0, 0.3, 0.6, 0.9]


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
