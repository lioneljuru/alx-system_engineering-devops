# A ptppet script to fix a server request fail when fail when loaded with a high number
# of requests

exec {'write':
  provider => shell,
  command  => 'sudo sed -i "s/15/4096/g" /etc/default/nginx'
}

exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart'
}
