# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.box_check_update = false

  config.vm.define "bro11", autostart: false do |bro11|
    bro11.vm.network "public_network", ip: "10.0.0.11"
  end
  config.vm.define "bro12", autostart: false do |bro12|
    bro12.vm.network "public_network", ip: "10.0.0.12"
  end
  config.vm.define "bro13", autostart: false do |bro13|
    bro13.vm.network "public_network", ip: "10.0.0.13"
  end
  config.vm.define "bro14", autostart: false do |bro14|
    bro14.vm.network "public_network", ip: "10.0.0.14"
  end

  config.vm.define "bro21", autostart: false do |bro21|
    bro21.vm.network "public_network", ip: "10.0.0.21"
  end
  config.vm.define "bro22", autostart: false do |bro22|
    bro22.vm.network "public_network", ip: "10.0.0.22"
  end
  config.vm.define "bro23", autostart: false do |bro23|
    bro23.vm.network "public_network", ip: "10.0.0.23"
  end
  config.vm.define "bro24", autostart: false do |bro24|
    bro24.vm.network "public_network", ip: "10.0.0.24"
  end

  config.vm.define "bro31", autostart: false do |bro31|
    bro31.vm.network "public_network", ip: "10.0.0.31"
  end
  config.vm.define "bro32", autostart: false do |bro32|
    bro32.vm.network "public_network", ip: "10.0.0.32"
  end
  config.vm.define "bro33", autostart: false do |bro33|
    bro33.vm.network "public_network", ip: "10.0.0.33"
  end
  config.vm.define "bro34", autostart: false do |bro34|
    bro34.vm.network "public_network", ip: "10.0.0.34"
  end

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y apache2 openssh-server vim git curl parallel sysstat
    # Download and install Bro
    [ -d bro-2.4.1/ ] || curl -O https://www.bro.org/downloads/bro-2.4.1.tar.gz
    [ -d bro-2.4.1/ ] || tar -xvzf bro-2.4.1.tar.gz
    cd bro-2.4.1/
    apt-get install -y cmake make gcc g++ flex bison libpcap-dev libssl-dev python-dev swig zlib1g-dev
    ./configure
    make
    make install
    echo "export PATH=\"$PATH:/usr/local/bro/bin\"" >> ~/.bashrc
    # Generate directory for logging
    mkdir -p ~/brolog
    [ -e ~/broeval ] || ln -s /vagrant ~/broeval
    # Generate random files of fixed size
    cd /var/www/html
    base64 /dev/urandom | head -c 10 > 1.txt
    base64 /dev/urandom | head -c 100 > 2.txt
    base64 /dev/urandom | head -c 1000 > 3.txt
    base64 /dev/urandom | head -c 10000 > 4.txt
    base64 /dev/urandom | head -c 100000 > 5.txt
    base64 /dev/urandom | head -c 1000000 > 6.txt
    base64 /dev/urandom | head -c 10000000 > 7.txt
    base64 /dev/urandom | head -c 100000000 > 8.txt
    base64 /dev/urandom | head -c 1000000000 > 9.txt
  SHELL
end
