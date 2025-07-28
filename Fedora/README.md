## DeArrow CLI packaging for RPM
This directory contains the specfiles needed to build [dearrow-cli](https://code.mschae23.de/mschae23/dearrow-cli)
and some of its dependencies for Fedora.

If you want to build them yourself and you are not publishing them in your own RPM repository,
make sure you have the following in your `~/.config/mock.cfg`:
```
config_opts['dnf.conf'] += """
[mschae23-fc$releasever]
name=mschae23 for Fedora $releasever
baseurl=https://code.mschae23.de/api/packages/mschae23/rpm/fc$releasever
gpgkey=file:///etc/pki/mock/RPM-GPG-KEY-MSCHAE23
gpgcheck=1
enabled=1
"""
```

As you can see, you'll also need my GPG key at `/etc/pki/mock/RPM-GPG-KEY-MSCHAE23`. You can download it from
https://keys.openpgp.org (`pkg@mschae23.de`). It should have the following fingerprint:
```
60C9 7C71 B476 4DF9 319D  4F02 1315 D06E 9C20 41E8
```
