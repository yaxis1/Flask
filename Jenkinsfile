pipeline {
    agent any
    stages {
        stage ('Compile Stage'){
            steps{
                bat 'run.py'
            }
        }
        stage ("Test Stage"){
            steps{
                bat 'python test.py'
            }
        }
    }
}