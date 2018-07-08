Understanding Docker Commands

## in a sequence
1. FROM
2. COPY
3. EXPOSE

### FROM - because there are preset environments to start your stuff from
- specifies the base image that the container will be using, which is the operating system (ubuntu/linux/whatever) with the required stuff installed already (python libraries like scikit-learn, tf and stuff)

### COPY - because those environments have their own group file system
- specifies which folder to copy into the docker environment from the host environment (which is either your laptop or some cloud console)
- needs to specify the PATH in which the folder will be in the DOCKER environment, so that if can find its own files

### EXPOSE - because those environments have their own networking stack (ports)
- specifies which port to expose (e.g. :5000)
- expose whitelisted ports (doesn't expose every single thing within the container)

### WORKDIR
- specifies the working directory of the folder when the container starts
- equivalent to `right click + open terminal at folder`

### RUN
- runs commands, like `python app.py` or `node app.js` or `npm start`
- e.g. `RUN pip install`

### CMD
- functions similar to the RUN command. it is the final RUN command you run, and basically you want to make sure that they don't ever terminate (otherwise the container stops serving stuff)
- something like `port.listen()` is javascript and `app.run()` in python's flask.
- e.g. run the flask app (as the final command in the string of commands)

## docker CLI commands
`docker build -t my-container-name .`  # builds the blueprint (doesn't run it yet)
`docker ps`  # list files
`docker images`  # see your built images
`docker run -p 5000:5000 my-container-name`  # runs + tells it to bind my port `5000:...` to the docker container's port `...:5000`. [ref](https://docs.docker.com/v1.7/reference/run/#expose-incoming-ports)