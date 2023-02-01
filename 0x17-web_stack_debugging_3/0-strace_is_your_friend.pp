#fix typo in wordpress settings file
exec { 'Replace typo error':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
