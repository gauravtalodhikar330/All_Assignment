from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime


# instantiate flask app
app = Flask(__name__)

# @app.route("/todolist")

#set configs
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#instantiate db object
db = SQLAlchemy(app)

# create marshmallow 
ma=Marshmallow(app)


class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(400),nullable=False)
    completed = db.Column(db.Boolean, nullable = False, default=False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)


def __repr__(self):
    return self.id


# @app.route("/todolist")
# def todo():
#     return jsonify({"Msg" : "Hello World From API"})

# create TodoList Schema
class TodoListSchema(ma.Schema):
    class Meta:
        fields= ('id', 'name', "description", 'completed', 'date_created')

#Create instance of Schemas
todolist_schema = TodoListSchema(many=False)
todolists_schema = TodoListSchema(many=True)


# Create  todos route POST
@app.route("/todolist", methods = ["POST"])
def add_todo():

    try: 
        name = request.json['name']
        description = request.json['description']

        new_todo = TodoList(name = name, description = description)
        db.session.add(new_todo)
        db.session.commit()

        return todolist_schema.jsonify(new_todo)
    
    except Exception as e:
        return jsonify({"Error" : "Invalid request."})

# get todos
@app.route("/todolist", methods=["GET"])
def get_todos():
    todos = TodoList.query.all()
    result_set = todolist_schema.dump(todos)
    return jsonify(result_set)
    
@app.route("/todolist/<int:id>", methods= ["GET"])
def get_todo(id):
    todo = TodoList.query.get_or_404(int(id))
    return todolist_schema.jsonify(todo)

@app.route("/todolist/<int:id>", methods=["PUT"])
def update_todo(id):
    todo = TodoList.query.get_or_404(int(id))

    name = request.json['name']
    description = request.json['description']
    completed = request.json['completed']

    todo.name = name
    todo.description = description
    todo.completed = completed

    db.session.commit()

    return todolist_schema.jsonify(todo)


if __name__ == "__main__":
    app.run(debug=True)
# Delete Todos 


@app.route("/todolist/<int:id>", methods=["DELETE"])
def delete_todo(id):
    todo = TodoList.query.get_or_404(int(id))
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"Sucess" : "Todo deleted."})
    