import os

from flask import Flask, render_template, request, jsonify

from superhelp import conf
from superhelp.helper import OutputSettings, get_formatted_help_dets

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

## The bit we get using AJAX
@app.route('/get_help', methods=['POST'])
def get_help() -> str:
    code = request.get_json()
    output_settings = OutputSettings(
        format_name=conf.Format.HTML,
        theme_name=None, detail_level=conf.Level.EXTRA,
        warnings_only=False, execute_code=False)
    formatted_help_dets = get_formatted_help_dets(code=code,
        file_path=None, project_path=None, exclude_folders=None,
        output_settings=output_settings, in_notebook=False)
    help_strs = [help_str for help_str, _file_path in formatted_help_dets]
    help_str = '\n\n'.join(help_strs)
    return jsonify(help_str)

if __name__ == '__main__':
    app.run(debug=True)
    
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 33507))
    app.run(host='0.0.0.0', port=port)

