pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/AaliyaShaikh23/student-registrationapp.git'
            }
        }

        stage('Install Requirements') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Verify Flask File') {
            steps {
                bat 'python -c "import app; print(\'Flask app verified successfully\')"'
            }
        }
    }
}




