# djtbot

### Basic Usage
10
1. First run `make build` inside root directory.
11
2. Then run `make up` to start up the project for first time.
12
​
13
Checkout the [commands](#commands) section for more usage.


### Commands
25
To use this project, run this commands:
26
​
27
1. `make up` to build the project and starting containers.
28
2. `make build` to build the project.
29
3. `make start` to start containers if project has been up already.
30
4. `make stop` to stop containers.
31
5. `make shell-web` to shell access web container.
32
6. `make shell-db` to shell access db container.
33
7. `make shell-nginx` to shell access nginx container.
34
8. `make logs-web` to log access web container.
35
9. `make logs-db` to log access db container.
36
10. `make logs-nginx` to log access nginx container.
37
11. `make collectstatic` to put static files in static directory.
38
12. `make log-web` to log access web container.
39
13. `make log-db` to log access db container.
40
14. `make log-nginx` to log access nginx container.
41
14. `make restart` to restart containers.
