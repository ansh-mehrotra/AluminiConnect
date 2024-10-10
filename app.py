
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
import pandas as pd

app = Flask(__name__)

def load_data():
    # Load the data from the Excel file
    return pd.read_excel('students.xlsx')

def save_data(df):
    # Save the updated data to the Excel file
    df.to_excel('students.xlsx', index=False)


#Added login route here in the main code
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        dob = request.form.get('dob')
        father_name = request.form.get('father_name')

        df = load_data()
        print(dob,father_name)
        # Check if the necessary columns exist in the DataFrame
        if 'EMAIL ID1' not in df.columns or 'BIRTH DATE' not in df.columns or 'FATHERNAME' not in df.columns:
            print("DataFrame columns:", df.columns)
            return render_template('login.html', error="Required columns are missing in the data file.")

        # First check if the email is correctly identified
        if email:
            user_data = df[df['EMAIL ID1'] == email]
            if not user_data.empty:
                return render_template('index.html', user_details=user_data.iloc[0].to_dict())  # Redirect to index.html after successful login

        # If email is not provided or doesn't match, check if both dob and father's name are correct
        if dob and father_name:
            user_data = df[(df['BIRTH DATE'] == dob.strip()) & (df['FATHERNAME'] == father_name.strip())]
            if not user_data.empty:
                return render_template('index.html',user_details=user_data.iloc[0].to_dict())
            else:
                print("no user details")
                return  # Redirect to index.html after successful login

        print("Reached here");
        # If neither email nor dob + father's name match
        flash('Invalid login credentials. Please try again.')
        return render_template('login.html', email=email, dob=dob, father_name=father_name)

    # For GET requests, just show the login page
    return render_template('login.html')




@app.route('/get-details', methods=['GET'])
def get_details():
    email = request.args.get('email')
    dob = request.args.get('dob')
    fathers_name = request.args.get('fathers_name')

    print(f"Received GET request with email={email}, dob={dob}, fathers_name={fathers_name}")

    df = load_data()

    # Check if columns exist in the DataFrame
    if 'EMAIL ID1' not in df.columns or 'BIRTH DATE' not in df.columns or 'FATHERNAME' not in df.columns:
        print("DataFrame columns:", df.columns)
        return jsonify({'success': False, 'message': 'Required columns are missing in the data file'}), 500

    # Filter the dataframe based on the provided parameters
    if email:
        user_data = df[df['EMAIL ID1'] == email]
    elif dob and fathers_name:
        user_data = df[(df['BIRTH DATE'] == dob) & (df['FATHERNAME'] == fathers_name)]
    else:
        return jsonify({'success': False, 'message': 'No valid search criteria provided'}), 400

    if not user_data.empty:
        user_details = user_data.iloc[0].to_dict()

        # Replace NaN values with None
        user_details = {k: (None if pd.isna(v) else v) for k, v in user_details.items()}

        return jsonify({'success': True, 'details': user_details})
    else:
        return jsonify({'success': False, 'message': 'No matching records found'}), 404

@app.route('/update-details', methods=['POST'])
def update_details():
    # Access form data
    email = request.form.get('EMAIL ID1')
    dob = request.form.get('BIRTH DATE')
    fathers_name = request.form.get('FATHERNAME')

    new_data = {
        'ENROLLMENTNO': request.form.get('ENROLLMENTNO'),
        'STUDENTNAME': request.form.get('STUDENTNAME'),
        'FATHERNAME': request.form.get('FATHERNAME'),
        'PROGRAM': request.form.get('PROGRAM'),
        'BRANCH': request.form.get('BRANCH'),
        'PASSOUT YEAR': request.form.get('PASSOUT YEAR'),
        'BIRTH DATE': request.form.get('BIRTH DATE'),
        'EMAIL ID1': request.form.get('EMAIL ID1'),
        'EMAIL ID2': request.form.get('EMAIL ID2'),
        'CONTACT NO.': request.form.get('CONTACT NO.'),
        'WHATSAPP NO.': request.form.get('WHATSAPP NO.'),
        'HOME STATE': request.form.get('HOME STATE'),
        'LINKEDIN PAGE': request.form.get('LINKEDIN PAGE'),
        'LAST UPDATE DATE': request.form.get('LAST UPDATE DATE'),
        'CURRENT DESIGNATION': request.form.get('CURRENT DESIGNATION'),
        'COMPANY': request.form.get('COMPANY'),
        'CITY': request.form.get('CITY'),
        'COUNTRY': request.form.get('COUNTRY'),
        'DEGREE NAME': request.form.get('DEGREE NAME'),
        'BRANCH/SPECIALIZATION': request.form.get('BRANCH/SPECIALIZATION'),
        'INSTITUTE NAME': request.form.get('INSTITUTE NAME'),
        'INSTITUTE CITY': request.form.get('INSTITUTE CITY'),
        'INSTITUTE COUNTRY': request.form.get('INSTITUTE COUNTRY'),
        'JOINING YEAR': request.form.get('JOINING YEAR'),
        'COMPLETION YEAR': request.form.get('COMPLETION YEAR'),
        'HIGHEST DEGREE NAME': request.form.get('HIGHEST DEGREE NAME'),
        'HD BRANCH/SPECIALIZATION': request.form.get('HD BRANCH/SPECIALIZATION'),
        'HD INSTITUTE NAME': request.form.get('HD INSTITUTE NAME'),
        'HD CITY': request.form.get('HD CITY'),
        'HD COUNTRY': request.form.get('HD COUNTRY'),
        'HD JOINING YEAR': request.form.get('HD JOINING YEAR'),
        'HD COMPLETION YEAR': request.form.get('HD COMPLETION YEAR')
    }

    print(f"Updating record for dob={dob}, fathers_name={fathers_name}, email={email} with new_data={new_data}")

    df = load_data()

    # Strip whitespace
    df['BIRTH DATE'] = df['BIRTH DATE'].astype(str).str.strip()
    df['FATHERNAME'] = df['FATHERNAME'].astype(str).str.strip()

    if email:
        user_data = df[df['EMAIL ID1'].str.strip() == email]
    elif dob and fathers_name:
        user_data = df[(df['BIRTH DATE'] == dob) & (df['FATHERNAME'] == fathers_name)]
    else:
        return jsonify({'success': False, 'message': 'No valid search criteria provided'}), 400

    if not user_data.empty:
        index = user_data.index[0]
        df.loc[index, new_data.keys()] = pd.Series(new_data)

        save_data(df)

        return jsonify({'success': True, 'message': 'Record updated successfully'})
    else:
        return jsonify({'success': False, 'message': 'No matching records found'}), 404

if __name__ == '__main__':
    app.run(debug=True)









