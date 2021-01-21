pipeline {
    agent any
    stages {
        stage ('Compile Stage'){
            steps{
                bat 'python3 run.py'
            }
        }
        stage ("Test Stage"){
            steps{
                bat 'python3 test.py'
            }
        }
    }
}