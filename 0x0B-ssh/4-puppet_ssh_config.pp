# Puppet to create a file and give permition
exec { 'add_lines':
  command  => '/bin/echo -e "    PasswordAuthentication no\n    IdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config',
  path     => '/usr/bin'
}
