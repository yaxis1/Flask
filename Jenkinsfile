pipeline {
    agent any
    stages {
        stage ('Compile Stage'){
            steps{

                sudo pip install --upgrade pip
                run.py
            }
        }
        stage ("Test Stage"){
            steps{
                python test.py
            }
        }
    }
}