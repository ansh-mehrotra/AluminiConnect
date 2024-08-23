

from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

def load_data():
    df = pd.read_excel('students.xlsx')
    return df

@app.route('/', methods=['GET', 'POST'])
def index():
    user_details = None
    if request.method == 'POST':
        dob = request.form.get('dob')
        fathers_name = request.form.get('fathers_name')

        df = load_data()
        user_data = df[(df['DOB'] == dob) & (df['Father Name'] == fathers_name)]
        
        if not user_data.empty:
            user_details = user_data.iloc[0].to_dict()
        
    return render_template('index.html', user_details=user_details)

@app.route('/get-details', methods=['GET'])
def get_details():
    email = request.args.get('email')
    df = load_data()
    user_data = df[df['Email'] == email]

    if not user_data.empty:
        user_details = user_data.iloc[0].to_dict()
        return jsonify({'success': True, 'details': user_details})
    else:
        return jsonify({'success': False})

if __name__ == '__main__':
    app.run(debug=True)

