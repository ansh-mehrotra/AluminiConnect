from flask import Flask, request, redirect, url_for, render_template
import pandas as pd

app = Flask(__name__)


def load_data():
    # Specify the engine explicitly
    df = pd.read_excel('students.xlsx')

    print(df.columns)
    return df


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        
        # Load the data
        df = load_data()
        print
        # Assuming the email column exists, filter the data
        user_data = df[df['Email'] == email]
        
        if not user_data.empty:
            # Convert user data to dictionary to pass to the template
            user_details = user_data.iloc[0].to_dict()
        else:
            user_details = None
        
        return render_template('index.html', user_details=user_details, email=email)
    
    return render_template('index.html', user_details=None)

@app.route('/update', methods=['POST'])
def update():
    student_id = request.form.get('student_id')
    new_name = request.form.get('name')
    new_email = request.form.get('email')

    if not student_id:
        # Handle the case where student_id is not provided
        return "Student ID is required", 400

    # Proceed with the update if all required fields are present
    df = pd.read_excel('students.xlsx', engine='openpyxl')
    
    # Check if student_id exists
    if int(student_id) in df['Roll Number'].values:
        df.loc[df['Roll Number'] == int(student_id), 'Name'] = new_name
        df.loc[df['Roll Number'] == int(student_id), 'Email'] = new_email
        df.to_excel('students.xlsx', index=False)
        return redirect(url_for('index'))
    else:
        return f"Student ID {student_id} not found", 404


if __name__ == '__main__':
    app.run(debug=True)
    