
from flask import Flask, request,redirect,url_for, jsonify, render_template
import pandas as pd

app = Flask(__name__)

def load_data():
    # Load the data from the Excel file
    return pd.read_excel('students.xlsx')

def save_data(df):
    # Save the updated data to the Excel file
    df.to_excel('students.xlsx', index=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_details = None
    if request.method == 'POST':
        dob = request.form.get('dob')
        fathers_name = request.form.get('fathers_name')
        email = request.form.get('email')

        print(f"Received POST request with dob={dob}, fathers_name={fathers_name}, email={email}")

        df = load_data()

        # Check if columns exist in the DataFrame
        if 'Email' not in df.columns or 'DOB' not in df.columns or 'Father Name' not in df.columns:
            print("DataFrame columns:", df.columns)
            return render_template('index.html', user_details=None, error="Required columns are missing in the data file.")

        # Build query conditions
        if email:
            user_data = df[df['Email'] == email]
        elif dob and fathers_name:
            user_data = df[(df['DOB'] == dob) & (df['Father Name'] == fathers_name)]
            print("founddd");
        else:
            user_data = pd.DataFrame()  # Empty DataFrame if no valid search criteria

        if not user_data.empty:
            user_details = user_data.iloc[0].to_dict()
        else:
            user_details = None
        
    return render_template('index.html', user_details=user_details)

@app.route('/get-details', methods=['GET'])
def get_details():
    email = request.args.get('email')
    dob = request.args.get('dob')
    fathers_name = request.args.get('fathers_name')

    print(f"Received GET request with email={email}, dob={dob}, fathers_name={fathers_name}")

    df = load_data()

    # Check if columns exist in the DataFrame
    if 'Email' not in df.columns or 'DOB' not in df.columns or 'Father Name' not in df.columns:
        print("DataFrame columns:", df.columns)
        return jsonify({'success': False, 'message': 'Required columns are missing in the data file'}), 500

    # Filter the dataframe based on the provided parameters
    if email:
        user_data = df[df['Email'] == email]
    elif dob and fathers_name:
        user_data = df[(df['DOB'] == dob) & (df['Father Name'] == fathers_name)]
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
    email = request.form.get('email').strip()
    dob = request.form.get('dob').strip()
    fathers_name = request.form.get('fathers_name').strip()

    new_data = {
        'Name': request.form.get('name'),
        'Batch': request.form.get('batch'),
        'Roll Number': request.form.get('roll_number'),
        'Program Name': request.form.get('program_name'),
        'Branch': request.form.get('branch'),
        'Passout Year': request.form.get('passout_year'),
        'DOB': request.form.get('dob'),
        'Email': request.form.get('email'),
        'Phone Number': request.form.get('phone_number'),
        'WhatsApp Number': request.form.get('whatsapp_number'),
        'Current Designation': request.form.get('current_designation'),
        'Current Company': request.form.get('current_company'),
        'Current City': request.form.get('current_city'),
        'Current Country': request.form.get('current_country'),
        'LinkedIn': request.form.get('linkedin'),
        'Father Name': request.form.get('fathers_name'),
        'Home State': request.form.get('home_state')
    }

    print(f"Updating record for dob={dob}, fathers_name={fathers_name}, email={email} with new_data={new_data}")

    df = load_data()

    df['DOB'] = df['DOB'].astype(str).str.strip()
    df['Father Name'] = df['Father Name'].astype(str).str.strip()

    if email:
        user_data = df[df['Email'].str.strip() == email]
    elif dob and fathers_name:
        user_data = df[(df['DOB'] == dob) & (df['Father Name'] == fathers_name)]
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
