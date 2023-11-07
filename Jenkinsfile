pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh ' python3 python.py'
                echo 'Building the app...'
               
            }
        }
        stage('Test') {
            steps {
                echo 'Testing the app...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the app...'
            }
        }
    }
}
