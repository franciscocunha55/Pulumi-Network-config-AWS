# Pulumi-Network-config-AWS

This project contains a minimal network infrastructure (AWS Cloud) based on Pulumi and Python 
<p>
The guideline for elaboration was to create the class for each resource wanted and posteriorly instanciate in the main file with the desired arguments.
<p>

To run this project, assuming the Pulumi CLI and Python is installed:
   ```
  $ pipenv install
  $ pulumi stack init dev
  $ pulumi config set aws:region us-west-2
  $ pipenv run pulumi up
  ```
