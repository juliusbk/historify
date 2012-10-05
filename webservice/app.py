from flask import Flask, render_template, request
import urllib, uuid, os
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
    #process(tag)
    f = urllib.urlopen(url)
    fid = str(uuid.uuid1())
    path = 'static/dzi_converter/files/'+fid
    f_local = open(path+'.jpg','w')
    f_local.write( f.read() )
    f_local.close()

    os.system("python static/dzi_converter/seadragon.py "+path+'.jpg')

    path = "/"+path+".dzi"
    return render_template("image.html", path=path)

if __name__=="__main__":
    app.run(debug=True)
