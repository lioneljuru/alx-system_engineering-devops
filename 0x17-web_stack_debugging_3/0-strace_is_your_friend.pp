# atomated puppet fix (to find out why Apache is returning a 500 error)

excec { 'Fix wordpress site':
	command => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
	provider => shell,
}
