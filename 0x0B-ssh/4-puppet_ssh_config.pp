# Puppet to create a file and give permition
exec { 'add_lines':
  command  => '/bin/echo -e "    PasswordAuthentication No\n    IdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config',
  path => '/etc/bin'
}
