from flask import Flask, jsonify, request
import sys

app = Flask(__name__)

#This is in the main app, normaly. I removed the whole datastruct.

running_port = sys.argv[1] if len(sys.argv) > 1 else 5000
output_file = sys.argv[2] if len(sys.argv) > 2 else "log.txt"
output_target = "log_files/" + output_file

@app.route('/', methods=['POST'])
def racine_post():
    # with open(output_target, "a", encoding="utf-8") as out_file:
    with open(output_target, "a", encoding="utf-8") as out_file:
            out_file.write(str(request.form) + "\n")
    return "Information logged"


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port=running_port)
