#edit ssh configurations
file_line{ 'Disable password authentication':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no'
}
file_line{ 'add identity':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}
