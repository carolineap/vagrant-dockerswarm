# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

vm = {
  "server" => { :ip => "192.168.33.10", :cpus => 1, :mem => 4096},
  "client" => { :ip => "192.168.33.11", :cpus => 1, :mem => 2048}
}
 
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "ubuntu/bionic64"
  
  vm.each_with_index do |(hostname, info), index|

    config.vm.define hostname do |cfg|
  
      cfg.vm.provider :virtualbox do |vb, override|

        override.vm.network :private_network, ip: "#{info[:ip]}"
        override.vm.hostname = hostname
        vb.name = hostname
        vb.customize ["modifyvm", :id, "--memory", info[:mem], "--cpus", info[:cpus], "--hwvirtex", "on"]
  
      end # end provider
  
    end # end define

  end # end vm

end # end config
