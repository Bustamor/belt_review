from flask import Flask, render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "asdlfjdsafjepowjfodf54wjfoeqwjfewqofjeqwlkfjas;odfjd;osfjew;ofjewqofjeqwofjewq;"

