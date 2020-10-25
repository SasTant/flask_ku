from flask import Flask, redirect, url_for, render_template

apl = Flask(__name__)

@apl.route("/")
def rumah():
    return render_template('index.html')

@apl.route("/<jeneng>")
def guna(jeneng):
    return f"hello {jeneng}!"

@apl.route("/admin")
def admin():
    return redirect(url_for("rumah"))

if __name__ == "__main__":
    apl.run()
