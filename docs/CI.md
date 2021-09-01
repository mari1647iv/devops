# Continuous Integration of Python Web Application

## Continuous Integration Best Practices

- Maintain a code repository
- Automate the build and deployment
- Keep your Actions minimal
- Don’t install dependencies unnecessarily
- Make the build self-testing
- Set GitHub secrets
- Limit environment variables to the narrowest possible scope
- Store authors in Action metadata to promote code ownership
- Leverage GitHub Actions Marketplace
- Don’t use self-hosted runners in a public repository
- Fast builds with most recent changes
- Test in a Clone of the Production Environment
- Make it easy to get the latest deliverables
- Everyone can see the results of the latest build
- Ensure every repository contains a CI/CD workflow

## Jenkins Best Practices

- Keep Jenkins secure at all times
  - set access control
  - enable Cross Site Request Forgery (CSRF) Protection
  - use Jobs Restrictions Plugin to filter jobs that can be run on the master node
- Always backup The “JENKINS_HOME” directory
- Setup different job/project for each maintenance or development branch created
- Reduce repetition of similar Pipeline steps
- Avoid calls to Jenkins.getInstance
- Do not override built-in Pipeline steps
- Avoid large global variable declaration files
- Avoid very large shared libraries
- Avoid NotSerializableException
- Ensure Persisted Variables Are Serializable
- Do not assign non-serializable objects to variables
- Prevent resource collisions in jobs that are running in parallel
- Use “File Fingerprinting” to manage dependencies
- Making sure to use Groovy code in Pipelines as glue
- Avoid complex Groovy code in Pipelines
- Build scalable Jenkins Pipeline
- Manage declarative syntax/declarative Pipelines
- Maintain higher test code coverage and run unit tests as part of your Pipeline
- Monitor your CI/CD Pipeline
