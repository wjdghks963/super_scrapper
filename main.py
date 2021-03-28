from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

app = Flask("SuperScrapper")

db = {}


@app.route("/")
def home():
    return render_template("po.html")


@app.route("/report")  # 밑에 함수만 봄
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()     # word를 소문자로
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")

    return render_template("report.html",
                           searchingBy=word,
                           resultsNumber=len(jobs),
                           jobs=jobs
                           )

@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()       # error 생성
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")

app.run(host="0.0.0.0")
