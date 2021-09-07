# Run Ansible using Vagrant

## Run the Python Application

From the `vagrant/python_app_vm` folder run the following command to start the virtual machine

```bash
vagrant up
```

When the vagrant VM was created and the playbook was provisioned, you can connect the VM and check the correctness of app launch

```bash
vagrant ssh
curl -Is http://localhost:5000
```

Enter `logout` or press `CTRL+D` to close the connection

## Run the Docker installation only

From the `vagrant/docker_vm` folder run the following command to start the virtual machine

```bash
vagrant up
```

When the vagrant VM was created and the playbook was provisioned, you can connect the VM and check the correctness of docker installation

```bash
vagrant ssh
docker --version
```

Enter `logout` or press `CTRL+D` to close the connection

## Vagrant Tips

To update the Vagrantfile run:

```bash
vagrant reload
```

To update the playbook run:

```bash
vagrant provision
```
