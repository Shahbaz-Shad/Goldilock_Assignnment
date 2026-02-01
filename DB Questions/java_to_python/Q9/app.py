from flask import Flask, render_template, request

app = Flask(__name__)

# Hardcoded user credentials
USER_CREDENTIALS = {
    "admin": "admin123",
    "user1": "password1"
}

# Route for login page
@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            message = "SUCCESS"
        else:
            message = "FAILURE"

    return render_template("login.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
