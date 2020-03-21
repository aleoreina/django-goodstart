#!/bin/bash
# github: projectsh-django
# autor: Angel Reina (@aleoreina) - Venezuela

function template_header {  
clear	
echo -e "--------------------------------------------------------"
echo -e "#  project.sh  for Django Project \e[5m        Easy for you! \e[25m"
echo -e "--------------------------------------------------------"
echo -e "######### \e[1m  Ver 1.0 Github: @projectsh-django \e[25m #########"
echo -e "      "
}

function template_main_menu {
 
    template_header
    echo -e "--------------------------------------------------------"
	echo -e " \e[101m Manage.py functions \e[49m "
    echo -e "--------------------------------------------------------"
    echo "1) Run Server :: 127.0.0.1:8080"
    echo "2) Run Server :: 0.0.0.0:8080"
    echo "3) Run Shell for project"
    echo "4) Create SuperAdmin User"
    echo "5) Do make migrations (structure) for all models.py to Database "
    echo "6) Do migrations for all models.py to Database "
    echo -e "--------------------------------------------------------"


    echo -e "--------------------------------------------------------"
	echo -e " \e[44m Requirements functions \e[49m "
    echo -e "--------------------------------------------------------"
    echo "R1) Install / Update Packages :: requirements.txt"
    echo "R2) Install / Update Packages :: packages.json (via yarn)"
    echo -e "--------------------------------------------------------"




    echo "X) Exit"
}
function msg_backing_to_main_menu {
    echo "Redirecting to main menu in 2 seconds..."
}
function install_requirements_txt {
    template_header
    echo "Installing req.txt"
    pip install -r requirements.txt
    sleep 2
}
function install_packages_json_via_yarn {
    template_header
    echo "Installing package.json"
    yarn
    sleep 2
}
function run_shell {
    template_header
    echo "Running shell for Project "
    python ./manage.py shell
    msg_backing_to_main_menu
    sleep 2
}
function run_server_for_127_0_0_1_port_8080 {
    template_header
    echo "Running Server for 127.0.0.1:8080 for Django.. "
    python ./manage.py runserver 127.0.0.1:8080
    msg_backing_to_main_menu

    sleep 2
}
function run_server_for_all_ips_port_8080 {
    template_header
    echo "Running Server for 0.0.0.0:8080 for Django.. "
    python ./manage.py runserver 0.0.0.0:8080
    msg_backing_to_main_menu

    sleep 2
}
function run_make_migrations {
    template_header
    echo "Creating structured migrations  "
    python ./manage.py makemigrations
    msg_backing_to_main_menu
    sleep 2
}
function run_migrate {
    template_header
    echo "Doing migrations to DB "
    python ./manage.py migrate
    msg_backing_to_main_menu
    sleep 2
}
function create_superadmin {
    template_header
    echo "Create a superadmin user "
    python ./manage.py createsuperuser
    msg_backing_to_main_menu
    sleep 2
}
# Purpose - Get input via the keyboard and make a decision using case..esac 
function main_menu(){
    template_main_menu
	local c
	read -p "Enter the code > " c
	case $c in
        1)  run_server_for_127_0_0_1_port_8080 ;; 
    	2)	run_server_for_all_ips_port_8080 ;;
        3)  run_shell ;;
        4)  create_superadmin ;;
        5)	run_make_migrations ;;
        6)  run_migrate ;;
		R1)	install_requirements_txt ;;
        R2)	install_packages_json_via_yarn ;;
		X)	echo "Bye!"; exit 0 ;;
		*)	
			echo "Please select between 1 to 2 choice only."
			pause
	esac
}

# ignore CTRL+C, CTRL+Z 
#trap '' SIGINT SIGQUIT SIGTSTP

while true
do
	clear
 	main_menu
done