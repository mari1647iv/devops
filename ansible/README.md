# Ansible

To run the ansible navigate to the `vagrant` folder and start the Vagrant VM following the instructions.

## Docker role

The Docker role's aim is to install the Docker on Ubuntu machine.

For the implementation the [geerlingguy/ansible-role-docker](https://github.com/geerlingguy/ansible-role-docker) role was used as a template.

## Python application role

The app_python role's aim is to install and launch the Moscow Time web app on a remote machine. It includes the Docker role. The application launches on the port 5000.
