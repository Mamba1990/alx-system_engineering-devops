#!/usr/bin/pup
# Installing an especific version of flask (2.1.0)
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  Werkzeug >= '2.0'
}
