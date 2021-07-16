from flask import *
import os
app = Flask(__name__)


@app.route('/')
def upload():
    return render_template("try.html")


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save("static/img.jpg")
        command = 'python C:/Users/Rishabh/PycharmProjects/Object_dect/yolov5-develop/detect.py --weights C:/Users/Rishabh/PycharmProjects/Object_dect/yolov5-develop/last1.pt --img 640 --conf 0.7 --source static/img.jpg'

        os.system(command)

        return render_template("try3.html", name=f.filename)


if __name__ == '__main__':
    app.run(debug=True)