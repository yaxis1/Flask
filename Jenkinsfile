pipeline {
    agent any
    stages {
        stage ('Compile Stage'){
            steps{

                sh 'pip install --upgrade pip'
                sh 'run.py'
            }
        }
        stage ("Test Stage"){
            steps{
                sh 'python test.py'
            }
        }
    }
}