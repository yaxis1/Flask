pipeline {
    agent any
    stages {
        stage ('Compile Stage'){
            steps{

                sh 'sudo apt-get install python3-pip'
                sh 'sudo pip install --upgrade pip'
                sh 'sudo run.py'
            }
        }
        stage ("Test Stage"){
            steps{
                sh 'sudo python test.py'
            }
        }
    }
}