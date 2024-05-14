from flask import render_template, redirect
import os
import markdown
from time import ctime
from pymdownx import emoji

extensions = [
    'pymdownx.magiclink',
    'pymdownx.betterem',
    'pymdownx.tilde',
    'pymdownx.emoji',
    'pymdownx.tasklist',
    'pymdownx.superfences',
    'pymdownx.saneheaders',
    'pymdownx.tasklist',
    'pymdownx.mark',
    'pymdownx.smartsymbols',
    'pymdownx.caret',
    'pymdownx.extra',
    'sane_lists',
    'nl2br',

]

extension_configs = {
    'pymdownx.extra':{
        'markdown.extensions.tables':{
            'use_align_attribute': True
        }
    },
    "pymdownx.magiclink": {
        "repo_url_shortener": True,
        "repo_url_shorthand": True,
        "provider": "github",
        "user": "facelessuser",
        "repo": "pymdown-extensions"
    },
    "pymdownx.tilde": {
        "subscript": True
    },
    "pymdownx.emoji": {
        "emoji_index": emoji.gemoji,
        "emoji_generator": emoji.to_png,
        "alt": "short",
        "options": {
            "attributes": {
                "align": "absmiddle",
                "height": "20px",
                "width": "20px"
            },
            "image_path": "https://github.githubassets.com/images/icons/emoji/unicode/",
            "non_standard_image_path": "https://github.githubassets.com/images/icons/emoji/"
        }
    }
}




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
            MDContent.append([markdown.markdown(mdfile.read(), extensions=extensions, extension_configs=extension_configs), fold,
                              ctime(os.path.getctime(os.path.join(app.root_path, 'md', fold)))])
        return render_template('context_md.html', MDContent=MDContent)
