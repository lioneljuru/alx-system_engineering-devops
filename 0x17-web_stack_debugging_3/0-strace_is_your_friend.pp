# atomated puppet fix (Correct internal server error)

excec { 'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
