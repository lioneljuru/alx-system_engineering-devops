# Configure nginx using puppet

package { 'nginx':
  ensure => present,
}

service { 'nginx':
  ensure => running,
  enable => true,
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  mode    => '0644',
  content => 'Hello World',
}

exec { 'ngix_configure_redirect':
  command     => '/bin/sed -i "/server_name _;/a\\\n\\tlocation /redirect_me {\n\t\treturn 301 https://www.instagram.com/john.sky05;\n\t}" /etc/nginx/sites-available/default',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
}

exec { 'nginx_configure_custom_404':
  command     => '/bin/sed -i "/server_name _;/a\\\n\\terror_page 404 /custom_404.html;\n\tlocation /custom_404.html {\n\t\troot /var/www/error;\n\t\tinternal;\n\t}" /etc/nginx/sites-available/default',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
}

exec { 'nginx_restart':
  command     => '/usr/sbin/service nginx restart',
  path        => ['/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  refreshonly => true,
}
