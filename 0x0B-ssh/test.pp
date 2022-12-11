#edit configuration using puppet
file_line { 'rm password authentication':
  path   => '/home/zemaria/Documents/alx-system_engineering-devops/0x0B-ssh/2_config',
  line   => '123',
  ensure => 'present',
}
