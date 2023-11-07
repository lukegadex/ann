pipeline {
    agent any

    stages {
        stage("Build") {
            steps {
                sh "python.py"
                echo "Building the app..."
               
            }
        }
        stage("Test") {
            steps {
                echo "Testing the app..."
            }
        }
        stage("Deploy") {
            steps {
                echo "Deploying the app..."
            }
        }
    }
}
