from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_babel import _, lazy_gettext as _l
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


class UndercardForm(FlaskForm):
    EVENT_TYPES = [('lightning in a bottle', 'lightning in a bottle'), ('bottlerock', 'bottlerock'), ('local sf shows', 'local sf shows')]

    # full_name = StringField(_l('name', validators=[DataRequired()]))
    phone_number = StringField(_l('phone or email'), validators=[DataRequired()])
    # email = StringField(_l('email'), validators=[DataRequired(), Email()])
    event = SelectField(label=('event'), validators=[DataRequired()], choices=EVENT_TYPES)

    # spotify_username = StringField('spotify username', validators=[DataRequired()])
    submit = SubmitField('send')

class RegistrationForm(FlaskForm):
    full_name = StringField(_l('Full Name', validators=[DataRequired()]))
    username = StringField(_l('Username'), validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    curr_city = StringField(_l('City'))
    password = PasswordField(_l('Password - use a simple password like your middle name during the beta'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(),
                                           EqualTo('password')])
    referral = StringField(_l('Referred By'))
    submit = SubmitField(_l('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different username.'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different email address.'))
