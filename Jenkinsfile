pipeline {
    agent any
    stages {
        stage ('Compile Stage'){
            steps{
                sh 'python run.py'
            }
        }
        stage ("Test Stage"){
            steps{
                sh 'python test.py'
            }
        }
    }
}