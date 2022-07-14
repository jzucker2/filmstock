# Docker

Found this for keeping docker images up to date!

https://github.com/containrrr/watchtower

```
docker build -t filmstock:latest .
docker run -dp 5000:5000 filmstock
docker container ls
# container ID from above used below
docker exec -it f7ecbbadc663 /bin/sh
```

Docker compose

```
# don't always need --build
docker-compose up -d --build
docker-compose ps
docker-compose logs filmstock
docker-compose exec -it filmstock /bin/sh
docker-compose stop
```

## Dockerfile

The [reference page for Dockerfile is here](https://docs.docker.com/engine/reference/builder/)

I also should probably take advantage of `ONBUILD` [here](https://docs.docker.com/engine/reference/builder/#onbuild)

## Docker Raspberry Pi Set Up

From [here](https://dev.to/elalemanyo/how-to-install-docker-and-docker-compose-on-raspberry-pi-1mo)

Or actually [here](https://pumpingco.de/blog/setup-your-raspberry-pi-for-docker-and-docker-compose/)

```
ssh pi@10.0.1.144
```

In order to fix the newer images for the pi, I needed to fix a few things:

Issue:

* https://github.com/docker-library/python/issues/674

Fix:

* https://blog.samcater.com/fix-workaround-rpi4-docker-libseccomp2-docker-20/

```
# Get signing keys to verify the new packages, otherwise they will not install
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 04EE7237B7D453EC 648ACFD622F3D138

# Add the Buster backport repository to apt sources.list
echo 'deb http://httpredir.debian.org/debian buster-backports main contrib non-free' | sudo tee -a /etc/apt/sources.list.d/debian-backports.list

sudo apt update
sudo apt install libseccomp2 -t buster-backports
```

### Raspberry Pi Cryptography

This is a huge mess

Details about the `cryptography` dependency on rust is here: https://cryptography.io/en/latest/installation/#rust

I had a ton of links to help:

* https://github.com/rust-lang/cargo/issues/8719
* https://github.com/WeblateOrg/docker/pull/1427/files
* https://github.com/rust-lang/cargo/issues/7451
* https://github.com/docker/buildx/issues/395
* https://github.com/pyca/cryptography/issues/6829
* https://github.com/matrix-org/synapse/issues/9403
* https://github.com/pyca/cryptography/issues/6286
* https://github.com/rust-lang/cargo/issues/9335
* https://github.com/rust-lang/cargo/issues/10230#issuecomment-1001349815
* https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=998232
* https://github.com/pyca/cryptography/issues/6485

#### Rust

Installing rust has instructions:

* https://rust-lang.github.io/rustup/installation/other.html
* https://static.rust-lang.org/rustup/rustup-init.sh
* https://forge.rust-lang.org/infra/other-installation-methods.html#which
