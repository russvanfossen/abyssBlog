from flask import render_template, request, url_for, redirect, abort, flash
import os
import markdown
from time import ctime

def register_routes(app):

    @app.route('/')
    def index():
        paths = []
        folder_contents = os.listdir(os.path.join(app.root_path, 'md'))
        for num, file in enumerate(folder_contents):
            paths.append([file])
            paths[num].append(ctime(os.path.getctime(os.path.join(app.root_path, 'md', file))))

        return render_template('index.html', folder_contents=paths)

    @app.route("/<fold>")
    def render_routes(fold):
        folder_contents = os.listdir(os.path.join(app.root_path, 'md'))
        if fold not in folder_contents:
            return redirect('/')
        MDContent = []
        with open(os.path.join(app.root_path, 'md', fold)) as mdfile:
            MDContent.append([markdown.markdown(mdfile.read(), extensions=['fenced_code', 'codehilite']), fold,
                              ctime(os.path.getctime(os.path.join(app.root_path, 'md', fold)))])
        return render_template('context_md.html', MDContent=MDContent)
