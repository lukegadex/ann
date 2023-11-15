pipeline {
    agent any

    stages
    {
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/jasminejack12345/ann.git'
                sh 'python3 trial.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m trial'
            }
        }
        stage('Deploy') {
            steps {
                sh 'python3 -m trial'
                echo 'Deploying to test'
            }              
        }    
    }
    post {
        failure {
               mail bcc: '', body: 'Jenkins alert', cc: '', from: '', replyTo: '', subject: 'Pipeline failed', to: 'jasmineejack@gmail.com'           
              }
         }
}
