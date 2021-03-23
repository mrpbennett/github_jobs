from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class JobSearch(FlaskForm):
    search = StringField(
        "search", validators=[DataRequired()], render_kw={"placeholder": "Search"}
    )
    submit = SubmitField("Find jobs")
