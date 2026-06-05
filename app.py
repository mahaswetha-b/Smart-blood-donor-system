from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

FILE = "donors.csv"

# create csv if not exists
if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "BloodGroup", "Phone", "City"])


# HOME (SHOW ALL DONORS)
@app.route("/")
def home():
    donors = []
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader, None)
        donors = list(reader)

    return render_template("index.html", donors=donors)


# ADD DONOR
@app.route("/add", methods=["POST"])
def add_donor():
    name = request.form["name"]
    blood = request.form["blood"]
    phone = request.form["phone"]
    city = request.form["city"]

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, blood, phone, city])

    return redirect("/")


# DELETE DONOR
@app.route("/delete/<int:index>")
def delete_donor(index):
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        donors = list(reader)

    if 0 <= index < len(donors):
        donors.pop(index)

    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(donors)

    return redirect("/")


# SEARCH DONOR
@app.route("/search", methods=["POST"])
def search():
    blood = request.form["blood"].upper().strip()
    results = []

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader, None)

        for row in reader:
            if row and row[1].upper().strip() == blood:
                results.append(row)

    return render_template("index.html", donors=results)


if __name__ == "__main__":
    app.run(debug=True)