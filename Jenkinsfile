pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/AaliyaShaikh23/student-registrationapp.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Verify App File') {
            steps {
                bat 'python -c "import app; print(\'Flask app verified successfully\')"'
            }
        }
    }
}
