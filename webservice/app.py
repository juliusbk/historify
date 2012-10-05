from flask import Flask, render_template, request
import urllib, uuid, os
import make_image
import PIL
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit/")
def loader():
    url = request.args.get("url", "")
    return render_template('submit.html',url=url)

@app.route("/process/")
def process():
    url = request.args.get("url", "")

    PIL_image = make_image.make_image(url, resize=True, size=15000)
    fid = str(uuid.uuid1())
    path = 'static/dzi_converter/files/'+fid
    PIL_image.save(path+'.jpg')
    os.system("python static/dzi_converter/seadragon.py "+path+'.jpg')

    path = "/"+path+".dzi"
    return render_template("image.html", path=path)

if __name__=="__main__":
    app.run(debug=True)
