#edit the ulimit for nginx
exec {'update Ulimit default':
  command  => 'sudo sed -i "s/15/4096/g" /etc/defaults/nginx; sudo service nginx restart',
  provider => shell,
}
