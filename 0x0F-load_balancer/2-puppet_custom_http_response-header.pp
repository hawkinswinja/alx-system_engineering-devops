# Installs a Nginx server with custome HTTP header

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header'],
}

exec { 'add_header':
  provider => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/server_name _;/add_header X-Served-By \'$HOST\';\\nserver_name _;/g" /etc/nginx/sites-available/default',
  before      => Exec['restart Nginx'],
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
