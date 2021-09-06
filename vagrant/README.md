# Run Ansible using Vagrant

From the `vagrant` folder run the following command to start the virtual machine

```bash
vagrant up
```

When the vagrant VM was created and the playbook was provisioned, you can connect the VM

```bash
vagrant ssh
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
