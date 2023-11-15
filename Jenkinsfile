pipeline {
    agent any

    stages {
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
                echo 'Deploying the code'
            }
        }  
    }
    post {
        success {
            mail bcc: '', body: 'Build success.', cc: '', from: 'admin@jenkins', replyTo: 'jasmineejack@gmail.com', subject: 'Jenkins Pipeline', to: 'anneludemejay@gmail.com,lukegadebo,jahno743@gmail.com,blaisekilang@gmail.com'
          }
        failure {
               mail bcc: '', body: 'The pipeline failed.', cc: '', from: '', replyTo: '', subject: 'Jenkins pipeline error', to: 'jasmineejack@gmail.com,lukegadebo@gmail.com,blaisekilang4@gmail.com,jahno743@gmail.com'
            }
    } 
}
