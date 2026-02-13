# Z následujících si vyber kód a sestav funkční flask aplikaci (není třeba použít vše, vyber si pouze ty části kódu, které potřebuješ)
# Kód je funkční, pouze místo dotazníků je potřeba doplnit podle potřeby
from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

#with open("data/recenze.json", "r", encoding="utf-8") as file:
#    message = json.load(file)

@app.route("/")
def home():
    return render_template("vitej.html")

@app.route("/form")
def form():
    login = request.args.get("login")
    recenze = request.args.get("recenze")
    print(login, recenze)

    data = {
        "login": login,
        "recenze": recenze
    }
    #message.append(data)

    #with open("data/recenze.json", "w", encoding="utf-8") as file:
    #    json.dump(message, file, indent=4)

    if login and recenze:
        return render_template("form.html", login=login, recenze=recenze)

    if login == "nic" or recenze == "nic":
       return render_template("form.html", login="", recenze="uživatel byl příliš líný na napsání recenze")

    return render_template("form.html")
# request.form.get("???")
# print("???")
# cursor.execute("???")
# if request.method == "POST"
# render_template("???", ???, ???)


#vypisuje nam do konzole bugy
if __name__ == "__main__":
    app.run(debug=True)
