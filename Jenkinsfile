pipeline {
    agent any
    stages {
        stage ('Compile Stage'){
            steps{

                bat 'sudo pip install --upgrade pip'
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