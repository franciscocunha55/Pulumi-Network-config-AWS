# Pulumi-Network-config-AWS

This project contains a minimal network infrastructure (AWS Cloud) based on Pulumi and Python 
<p>
The guideline for elaboration was to create the class for each resource wanted and posteriorly instanciate in the main file with the desired arguments.
<p>

To run this project:
   
   # Prerequisites 
      
      1. [Install Pulumi](https://www.pulumi.com/docs/get-started/install/)
      2. [Configure Pulumi for AWS](Configure Pulumi for AWS)
      3. [Configure Pulumi for Python](https://www.pulumi.com/docs/intro/languages/python/)
      
 </br>
 
 # Run in cmd
 
   ```
  $ pulumi stack init dev
  $ pulumi config set aws:region AWS_REGION
  $ pulumi up
  ```
