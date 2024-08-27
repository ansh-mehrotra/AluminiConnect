
from flask import Flask, request, jsonify, render_template
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

if __name__ == '__main__':
    app.run(debug=True)
