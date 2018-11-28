from flask import Flask, render_template, request, redirect, url_for
from forms import *
from utils_light import *

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="haldean rules lolol come at me",
    WTF_CSRF_SECRET_KEY="a csrf secret key that also asserts haldean's excellence and handsomeness and other good qualities"
))

@app.route('/', methods=['GET', 'POST'])
def arlo():
    form = ArloForm()
    if form.validate_on_submit(): 
        if form.showSolidColor.data:
            send_osc("/lx/engine/crossfader", 1.0)
        elif form.showLightShow.data:
            send_osc("/lx/engine/crossfader", 0.0)
        elif form.setSpeed.data:
            change_speed(float(form.speed.data))
        elif form.setBrightness.data:
            change_brightness(float(form.brightness.data))
        elif form.setSolidColor.data:
            send_osc("/lx/channel/3/pattern/1/color/hue", float(form.solidColor.data))
        elif form.setTemperature.data:
            send_osc("/lx/master/effect/1/amount", float(form.temperature.data))
        return redirect(url_for('arlo'))
    return render_template('arlo.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
