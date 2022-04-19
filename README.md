<<<<<<< HEAD

<h3>This project contains a minimal network infrastructure (AWS Cloud) based on Pulumi and Python <h3>
=======
# Pulumi-Network-config-AWS

This project contains a minimal network infrastructure (AWS Cloud) based on Pulumi and Python 
>>>>>>> 49f530ddf57bfcd0dac71f980683ed838970ce19
<p>
The guideline for elaboration was to create the class for each resource wanted and posteriorly instanciate in the main file with the desired arguments.
<p>

To run this project:
   
   ### Prerequisites 
      
     
   1. [Install Pulumi](https://www.pulumi.com/docs/get-started/install/)
   2. [Configure Pulumi for AWS](https://www.pulumi.com/registry/packages/aws/installation-configuration/)
   3. [Configure Pulumi for Python](https://www.pulumi.com/docs/intro/languages/python/)
      
 
 ### Run in cmd
 
   ```
  $ pulumi stack init dev
  $ pulumi config set aws:region AWS_REGION
  $ pulumi up
  ```
