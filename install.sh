#!/bin/bash
echo "This is a simple installer script for pytyphon"

echo "Let's quickly check some dependincies"
sleep 2

echo -n "do you have firefox installed? : "

read que

if [ "$que" = "yes" ]
then
    echo "yup cool kids always use firefox"


elif [ "$que" = "no" ]
then
    echo "oh ok lets install it real quick"
    echo "select your distro"
    echo "1: Debian Based"
    echo "2: Arch Based"
    echo -n "my distro is : "
    read dis
    if [ "$dis" = "1" ]
    then
        echo "yo"
        sudo apt install firefox -y
    elif [ "$dis" = "2" ]
    then
        echo "I also use arch btw"
        sudo pacman -S firefox
    else
        echo "You trippin bro? check your input"
    fi
else
    echo "You trippin bro? check your input"

fi
sleep 1
echo "downloading pip installs"
pip install -r requirements.txt
sleep 1
clear
echo "downloading selenium webdriver"
sleep 3
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
clear
echo "where do you want your driver to be saved?"
echo "1. All users (Recommended)"
echo "2. local user"
echo -n "hmm : "
read $hmm

if [ "$hmm" = "$1" ]
then
    tar -zxvf geckodriver-v0.26.0-linux64.tar.gz
    mv geckodriver -t /usr/bin
    rm -rf geckodriver-v0.26.0-linux64.tar.gz
elif [ "$hmm" = "$2" ]
then
    tar -zxvf geckodriver-v0.26.0-linux64.tar.gz
    mv geckodriver -t /usr/local/bin
    rm -rf geckodriver-v0.26.0-linuz64.tar.gz
else
    echo "error"
fi
clear

echo "All set"
python3 pytyphon.py
