pipeline {
    agent any

    stages {
        stage("Build") {
            steps {
                echo "Building the app..."
                python circle.py
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
