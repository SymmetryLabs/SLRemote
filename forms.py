from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Length
#from flask_babel import _, lazy_gettext as _l
from wtforms.fields.html5 import DecimalRangeField


class RemoteForm(FlaskForm):

    PATTERN_TYPES = [('AskewPlanes', 'AskewPlanes'), ('Balance', 'Balance'), ('Ball', 'Ball') , ('BassPod', 'BassPod'),
    ('Blank', 'Blank'), ('Bubbles' ,'Bubbles') , ('CrossSections','CrossSections'), ('CubeEQ','CubeEQ'), ('CubeFlash','CubeFlash')
    , ('Noise','Noise'), ('Palette','Palette'), ('Pong','Pong')
    , ('Rings','Rings'), ('ShiftingPlane','ShiftingPlane'), ('SoundParticles','SoundParticles')
    , ('SpaceTime','SpaceTime'), ('Spheres','Spheres'), ('StripPlay','StripPlay')
    , ('Swarm','Swarm'), ('Swim','Swim'), ('TelevisionStatic','TelevisionStatic'), ('Traktor','Traktor')
    	, ('ViolinWave','ViolinWave')]

    CLIP_TYPES = [('Clip1', 'Clip1'), ('Clip2', 'Clip2'), ('Clip3', 'Clip3') ] 
    ON_TYPES = [('On', 'On'), ('Off', 'Off')]
    pattern = SelectField(label='Pattern', validators=[DataRequired()], choices=PATTERN_TYPES)#, choices=MEDIA_TYPES)
    brightness = DecimalRangeField(('Brightness'), validators=[DataRequired()])
    color = DecimalRangeField(label=('Color'), validators=[DataRequired()])
    speed = DecimalRangeField(label=('Speed'), validators=[DataRequired()])

    clip = SelectField(label=('Clip'), validators=[DataRequired()], choices=CLIP_TYPES)
    on_off = SelectField(label=('Enabled'), validators=[DataRequired()], choices=ON_TYPES)
    submit = SubmitField('Submit')
    clip1 = SubmitField('Clip 1')
    clip2 = SubmitField('Clip 2')
    clip3 = SubmitField('Clip 3')

class TestForm(FlaskForm):
    
    age = DecimalRangeField('Age', default=0, validators=[DataRequired()])
    submit = SubmitField('Submit')