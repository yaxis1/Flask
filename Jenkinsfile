pipeline {
    agent any
    stages {
        stage ('Compile Stage'){
            steps{
                
                sh 'apt-get install python3-pip'
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