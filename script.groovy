def install_requirements(){
    echo 'Installing requirements for flaskapp'
    sh'sudo apt-get install python3-pip'
    sh'sudo pip install -r requirements.txt'
}
return this