# pupper to change the line file
exec { '/var/www/html/wp-settings.php':
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  provider => 'shell'
}