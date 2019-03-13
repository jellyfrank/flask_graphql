
from flask_graphql import GraphQLView
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/graph"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


db = SQLAlchemy(app)

from graph import schema

app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

