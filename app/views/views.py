from flask import Flask, render_template, redirect, url_for, request, abort
from app.controllers.session_interface import MySessionInterface
from app.controllers import UserLogin, UserLogout, GetCurrentUsername, GetContactList, SaveContactRequest

app = Flask(__name__, template_folder="../templates", static_folder="../static")

app.secret_key = b"A231XEA12312301230#$1DW120X23"
app.session_interface = MySessionInterface()


@app.route("/")
def Index():
    username, login_auth = GetCurrentUsername()
    return render_template("index.html", username=username, login_auth=login_auth)


@app.route("/contact", methods=["GET", "POST"])
def Contact():
    if request.method == "POST":
        if request.form:
            name = request.form.get("name")
            email = request.form.get("email")
            category = request.form.get("category")
            priority = request.form.get("priority")
            message = request.form.get("message")

            SaveContactRequest(name, email, category, priority, message)
            return redirect(url_for("Contact"))

    username, login_auth = GetCurrentUsername()
    return render_template("contact.html", username=username, login_auth=login_auth)


@app.route("/contact-list")
def ContactList():
    username, login_auth = GetCurrentUsername()
    contact_list = GetContactList()
    return render_template("contact_list.html", username=username, login_auth=login_auth, contact_list=contact_list)


@app.route("/login", methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        if request.form:
            if "username" in request.form and "password" in request.form:
                username = request.form.get("username")
                password = request.form.get("password")
                if UserLogin(username, password):
                    return redirect(url_for("Index"))
                else:
                    return redirect(url_for("Login"))
        abort(400)
    username, login_auth = GetCurrentUsername()
    return render_template("login.html", username=username, login_auth=login_auth)


@app.route("/logout")
def Logout():
    if UserLogout():
        return redirect(url_for("Index"))


if __name__ == "__main__":
    app.run(debug=True)
