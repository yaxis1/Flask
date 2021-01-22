def gv 
pipeline {
    agent any
    stages {
        stage ('Load env script'){
            steps{
                echo "Loading groovy script"
                script{
                    gv = load "script.groovy"
                }
            }
        }
        stage ("Build Stage"){
            steps{
                echo'Building app'
                script{
                    gv.install_requirements()
                }
            }
        }
        stage ("Test Stage"){
            steps{
                echo 'Testing app'
                script{
                    gv.install_requirements()
                }
            }
        }
    }

    post{
        always{
            echo 'End of Pipeline'
        }
    }
}