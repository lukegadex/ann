
   pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/jasminejack12345/ann.git']])
            }
        }
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
                echo 'Deploy code'
            }
        }
    }
    post {
        success {
               mail bcc: '', body: '''Build has been successful. Refer to the link for an insight 
                    https://github.com/jasminejack12345/ann.git''', cc: '', from: '', replyTo: '', subject: 'CI/CD Pipeline', to: 'jasmineejack@gmail.com, jahno743@gmail.com, blaisekilang4@gmail.com, lukegadebo@gmail.com'          
        }
        failure {
            mail bcc: '', body: 'For more infor on the pipeline failure, checkout the console output at {env.BUILD_URL}', cc: '', from: '', replyTo: '', subject: '${env.JOB_NAME} - Build # ${env.BUILD_NUMBER} has failed,', to: 'anneludemejay@gmail.com, jahno743@gmail.com, blaisekilang4@gmail.com, lukegadebo@gmail.com'
           }
       }
}         
