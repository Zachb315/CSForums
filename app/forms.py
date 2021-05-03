from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextField, PasswordField

from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginUser(FlaskForm):
    email = StringField('Email:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Login')


class CreateUser(FlaskForm):
    username = StringField('Username:', validators=[DataRequired(message='Username is required')])
    firstname = StringField('First Name:', validators=[DataRequired(message='First name is required')])
    lastname = StringField('Last Name:', validators=[DataRequired(message='Last name is required')])
    email = StringField('Email:', validators=[DataRequired(), Email(message='A Valid email is required')])
    password = PasswordField('Password:', validators=[DataRequired(message='Password is required')])
    submit = SubmitField('Login')

class createTopic(FlaskForm):
    title = StringField('Title:', validators=[DataRequired(message='Title is required')])
    description = StringField('Description:', validators=[DataRequired(message='Description is required')])
    submit = SubmitField('Create Topic')


class createEvent(FlaskForm):
    event_name = StringField('Event Name:', validators=[DataRequired(message='Event name is required')])
    description = StringField('Description:', validators=[DataRequired(message='Description is required')])
    event_date = StringField('Event Date:', validators=[DataRequired(message='Event date is required')])
    submit = SubmitField('Create Event')


class createPost(FlaskForm):
    content = StringField('Content:', validators=[DataRequired(message='Content is required')])
    submit = SubmitField('Post')

class createCareer(FlaskForm):
    job_name = StringField('Job Name:', validators=[DataRequired(message='Job name is required')])
    applyBy_date = DateTimeLocalField('Apply By:', format='%Y-%m-%dT%H:%M', validators=[DataRequired(message='Apply by is required')])
    description = StringField('Description:', validators=[DataRequired(message='Description is required')])
    submit = SubmitField('Create Career')

class memberRequest(FlaskForm):
    email = StringField('Email:', validators=[DataRequired()])
    submit = SubmitField('Submit')


class forgotPassword(FlaskForm):
    email = StringField('Email:', validators=[DataRequired()])
    submit = SubmitField('Request Password Reset')

class resetPassword(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPw = PasswordField('Re-enter password', validators=[DataRequired()])
    submit = SubmitField('Reset Password')

class changeEmail(FlaskForm):
    email = StringField('New Email:', validators=[DataRequired()])
    confirmEm = StringField('Re-enter Email:', validators=[DataRequired()])
    submit = SubmitField('Change Email')

class changePassword(FlaskForm):
    previousPW = PasswordField('Enter in Old Password:', validators=[DataRequired()])
    newPW = PasswordField('Enter in New Password:', validators=[DataRequired()])
    confirmPW = PasswordField('Re-enter New Password:', validators=[DataRequired()])
    submit = SubmitField('Change Password')

class emailAnnouncement(FlaskForm):
    topic = StringField('Email Topic:', validators=[DataRequired(message='Topic is required')])
    message = StringField('Message:', validators=[DataRequired(message='Message is required')])
    submit = SubmitField('Send Emails')

