from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL

class URLForm(FlaskForm):
    url = StringField('Enter URL', validators=[DataRequired(), URL()])
    platform = SelectField('Social Media Platform', 
                        choices=[
                            ('general', 'General'),
                            ('twitter', 'Twitter/X'),
                            ('linkedin', 'LinkedIn'),
                            ('facebook', 'Facebook'),
                            ('instagram', 'Instagram')
                        ])
    submit = SubmitField('Generate Content')