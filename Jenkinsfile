pipeline {
    agent any
    stages {
        stage ('Compile Stage'){
            steps{
                cmd 'python run.py'
            }
        }
        stage ("Test Stage"){
            steps{
                cmd 'python test.py'
            }
        }
    }
}