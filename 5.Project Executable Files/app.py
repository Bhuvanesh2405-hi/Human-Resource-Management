import pickle
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/predict')
def predict():
    return render_template("predict.html")

@app.route('/predict', methods=['POST'])
def pred():
    try:
        d = request.form['department']
        if d == "Sales & Marketing":
            d = 7
        elif d == "Operations":
            d = 4
        elif d == "Technology":
            d = 8
        elif d == "Analytics":
            d = 0
        elif d == "R&D":
            d = 6
        elif d == "Procurement":
            d = 5
        elif d == "Finance":
            d = 1
        elif d == "HR":
            d = 2
        elif d == "Legal":
            d = 3
        else:
            raise ValueError("Invalid department value")

        education = request.form['education']
        if education == '1':
            education = 1
        elif education == '2':
            education = 2
        else:
            education = 3

        no_of_trainings = int(request.form['no_of_trainings'])
        age = int(request.form['age'])
        previous_year_rating = float(request.form['previous_year_rating'])
        length_of_service = int(request.form['length_of_service'])

        KPIs = request.form['KPIs']
        if KPIs == '0':
            KPIs = 0
        else:
            KPIs = 1

        awards_won = request.form['awards_won']
        if awards_won == '0':
            awards_won = 0
        else:
            awards_won = 1

        avg_training_score = float(request.form['avg_training_score'])

        total = [[float(d), float(education), float(no_of_trainings), float(age), float(previous_year_rating), float(length_of_service), KPIs, awards_won, avg_training_score]]
        model = pickle.load(open("promotion_model.pkl", "rb"))

        prediction = model.predict(total)

        

        if prediction[0] == 0:
            text = 'Sorry, you are not eligible for promotion'
        else:
            text = 'Great, you are eligible for promotion'
        return render_template("submit.html", data=text)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"

        
        
if __name__ == '__main__':
    app.run(debug=True)