#kill process
exec {'killme':
  command => '/usr/bin/pkill killmenow',
}
