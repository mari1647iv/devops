pipeline {
    agent any

    stages {

        stage('Install dependencies') {
            steps {
                sh 'docker pull python:3.8 '
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
