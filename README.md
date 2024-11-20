## dearrow-cli RPM packaging
This repository contains the specfiles needed to build [dearrow-cli](https://github.com/mschae23/dearrow-cli)
and some of its dependencies for Fedora.

If you want to build them yourself and you are not publishing them in your own RPM repository,
make sure you have the following in your `~/.config/mock.cfg`:
```
config_opts['dnf.conf'] += """
[mschae23-fc41]
name=mschae23 for Fedora 41
baseurl=https://mschae23.de/git/api/packages/mschae23/rpm/fc41
gpgkey=file:///etc/pki/mock/RPM-GPG-KEY-MSCHAE23
gpgcheck=1
enabled=1
"""
```
As you can see, you'll also need my GPG key at `/etc/pki/mock/RPM-GPG-KEY-MSCHAE23`. You can download it from
https://keys.openpgp.org (`contact@mschae23.de`). It should have the following fingerprint:
```
C7EE 4228 9024 78D4 287D  F13B 872D 8A11 8F7B 2F3B
```

