pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'apk add --no-cache gcc musl-dev linux-headers'
                sh 'python3 -m pip install -r app_python/requirements.txt'
                sh 'python3 -m pip install flake8'
            }
        }

        stage('Linting') {
            steps{
                sh 'flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics'
                sh 'flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics'
            }
        }

        stage('Testing') {
            steps{
                sh 'cd app_python'
                sh 'python3 -m unittest test_main.py'
            }
        }
    }
}
