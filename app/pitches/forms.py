from wtforms import StringField, TextAreaField, SelectField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    category = SelectField(u'Category', choices=[('tc', 'Tech'), ('biz', 'Business'), ('bd', 'Big Data'), ('rb', 'Robotics')]
                           , validators=[DataRequired()])
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    description = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
