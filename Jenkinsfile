pipeline {
    agent any
    stages {
        stage ('Compile Stage'){
            steps{
                echo'Compiling app'


            }
        }
        stage ("Test Stage"){
            steps{
                echo'Testing app'

            }
        }
    }
    post{
        always{
            echo 'End of Pipeline'
        }
    }
}