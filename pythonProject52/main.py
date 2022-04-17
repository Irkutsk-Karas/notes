from flask import Flask, render_template
# from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_restful import reqparse, abort, Api, Resource

from data import db_session
from data.notes import Note
from resources import user_res, note_res

app = Flask(__name__)
api = Api(app)

# login_manager = LoginManager()
# login_manager.init_app(app)

# для одного объекта
api.add_resource(note_res.NoteResource, '/api/notes/<int:note_id>')

# для списка объектов
api.add_resource(note_res.NoteListResource, '/api/notes')

# для одного объекта
api.add_resource(user_res.UserResource, '/api/users/<int:user_id>')

# для списка объектов
api.add_resource(user_res.UserListResource, '/api/users')


@app.route("/")
def index():
    db_sess = db_session.create_session()
    # if current_user.is_authenticated:
    #     notes = db_sess.query(Note).filter(
    #         (Note.user == current_user) | (Note.is_private != True))
    # else:
    #     notes = db_sess.query(Note).filter(Note.is_private != True)
    notes = db_sess.query(Note).filter(Note.is_private != True)
    return render_template("index.html", notes=notes)


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    db_sess.commit()
    app.run()


if __name__ == '__main__':
    main()

