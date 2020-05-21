# Puppet script initiallizes a fix to the error in the wp-settings.php file
exec { 'replace wrong syntax':
  command => "sed -i -e 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
  path    => '/bin',
}
