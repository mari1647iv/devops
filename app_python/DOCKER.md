# Best Practices Used for Docker Containerization

- Create ephemeral containers - container can be stopped and destroyed, then rebuilt and replaced with an absolute minimum set up and configuration.
- Understand build context
- Exclude with `.dockerignore`
- Use multi-stage builds (if it is makes a sense)
- Don’t install unnecessary packages
- Decouple applications (if it is makes a sense)
- Minimize the number of layers
- Sort multi-line arguments alphanumerically
- Leverage build cache
- Use current official images in `FROM` instruction (ex. `alpine`)
- Split long or complex `RUN` statements on multiple lines to improve readability
- Write CMD instruction in the form of `CMD ["executable", "param1", "param2"…]`
- Prefer `COPY` over `ADD`
- COPY files used in different steps individually
- Avoid root user and sudo privileges if it is possible
- Use absolute paths for your `WORKDIR`
- Use linters:
  - for Dockerfile - `hadolint`
- Use security scanners (ex. `Snyk`)

```bash
docker scan app_python
```
