from flask import Flask, render_template, request, redirect
from scrapper import get_jobs
app = Flask("SuperScrapper")


@app.route("/")
def home():
    return render_template("po.html")


@app.route("/report")  # 밑에 함수만 봄
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        jobs = get_jobs(word)
        print(jobs)
    else:
        return redirect("/")

    return render_template("report.html", searchingBy=word)

app.run(host="0.0.0.0")
