# Puppet command to fix limit

exec { 'limit':
  path    => '/bin',
  command => "sed -i 's/15/1500/g' /etc/default/nginx"
}

exec { 'restart nginx service':
  path    => 'etc/init.d/',
  command => 'nginx restart'