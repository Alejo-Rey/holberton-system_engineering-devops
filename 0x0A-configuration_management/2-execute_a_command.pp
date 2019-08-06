# Puppet to kill a proccess
exec { 'kill_proccess':
    provider => 'shell',
    path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
    command  => 'pkill killmenow',
}
