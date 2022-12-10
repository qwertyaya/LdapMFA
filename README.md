# OpenLDAP Kubernetes Deployment

This repository contains a Kubernetes deployment and service for OpenLDAP. The deployment uses the `bitnami/openldap` Docker image and exposes the OpenLDAP server on port 1389. The admin username and password, as well as the LDAP users and passwords, are stored in Kubernetes secrets.

## Usage

To use the deployment, first create the Kubernetes secrets with the `adminpassword`, `users`, and `passwords` keys. The `adminpassword` key should contain the admin password, the `users` key should contain a comma-separated list of LDAP users, and the `passwords` key should contain a comma-separated list of passwords for the LDAP users (in the same order as the `users` key).

You can create it with the command:

kubectl create secret generic openldap --from-literal=adminpassword=adminpassword --from-literal=users=ilana --from-literal=passwords=password -n yournamespace

Once the secrets are created, you can deploy the OpenLDAP server with the following command:

kubectl apply -f deployment.yaml -n yournamespace

As well as deploying the service with the following command:

kubectl apply -f service.yaml -n yournamespace

This will create a Kubernetes deployment OpenLDAP server. To check if the deployment was successful, you can use the following command to see the status of the deployment:

kubectl get deployments

The LDAP Login Script is a Python script that allows users to log in to an LDAP server using their username and password. It also includes a Telegram bot that sends the user a one-time password (OTP) for additional authentication. 

## Requirements

The LDAP Login Script requires the following libraries:

- `ldap3`
- `rich`
- `telebot`

To install these libraries, run the following command:

pip install ldap3 rich telebot


## Usage

To use the LDAP Login Script, run the `python3 appp.py` command and follow the prompts to enter the Telegram UID, LDAP server URL, your username, and password. The script will then send you an OTP via a Telegram bot, which you need to enter to complete the authentication process.

Once you're logged in, you'll get the user information that is created and stored for you in openldap. 


## Configuration

The LDAP Login Script uses the following environment variables:

- `TG_BOT_TOKEN`: The API token of the Telegram bot that sends the OTP.

## Contributing

If you want to contribute to the LDAP Login Script, please follow these guidelines:

- Fork the repository and create a new branch for your changes.
- Make your changes and add tests to cover them.
- Run the tests to ensure they pass.
- Submit a pull request to the `master` branch of the main repository.

## License

The LDAP Login Script is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
