#!/bin/bash
cd /home/repl

# Run the config scripts
for file in /home/repl/config/*.sh; do bash "$file"; done

# Back to repl directory after running config scripts
cd /home/repl

# Run nginx
service nginx start

# Run IDE in background
/usr/bin/supervisord

# Wait for nginx to be up and running
until nc -vz localhost 3000; do
    echo "no connection"
    sleep 0.1
done

# Wait for Theia IDE to be up and running
until nc -vz localhost 3001; do
    echo "no connection"
    sleep 0.1
done

for file in /home/repl/startup/*.sh; do bash "$file"; done

# Set bash prompt: repl:~/path$
echo 'PS1="\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u:\[\033[01;34m\]\w\[\033[00m\]\$ "' > .bashrc

# Make sure to save every command in the history
echo "shopt -s histappend" >> .bashrc
echo "export PROMPT_COMMAND=\"history -a; history -c; history -r; $PROMPT_COMMAND\"" >> .bashrc
touch .bash_history

python3 -i
