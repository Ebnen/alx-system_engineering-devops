!#/usr/bin/env bash
# using a puppet to automate file 

file {'/etc/ssh/ssh_config':
  ensure  =>  'present',
}

file_line {'Turn off password auth':
  Path    => '/etc/ssh/ssh_config',
  Line    => 'PasswordAuthentication no',
  Match   => 'PasswordAuthentication yes',
  Replace => 'true',
}

File_line {'Declare Identity File':
  ensure => 'present',
  Path   => '/etc/ssh/ssh_config',
  Line   => 'IdentityFile ~/.ssh/school',
  Match  => '^IdentityFile',
}
