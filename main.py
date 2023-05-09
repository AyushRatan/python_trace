from flask import Flask, request, render_template, redirect
import pandas as pd

df = pd.read_excel("output.xlsx")
print(df)

# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function


@app.route('/', methods = ["GET", "POST"])
def form():
	if request.method == "POST":
		name = request.form["name"]
		age = request.form["age"]
		df.loc[len(df.index)] = [name,age]
		with pd.ExcelWriter("output.xlsx", mode="a", if_sheet_exists="overlay") as writer:
			df.to_excel(writer,index=False)
	return render_template("home.html")


if __name__ == '__main__':
	app.run()
