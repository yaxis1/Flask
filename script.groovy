def install_requirements(){
    echo 'Installing requirements for flaskapp'
    sh'sudo su'
    sh'apt-get install python3-pip'
    sh'pip install -r requirements.txt'
}
return this