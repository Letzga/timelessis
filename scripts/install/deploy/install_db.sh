#!/bin/sh

# @todo #248:30min Implement a service for Postgres. Postgres should be up and running
#  after host restart. Lets create and install a service for Postgres and make sure it is
#  started and running.
# Script for Postgres availability check, installation, launch
which psql
if [ "$?" -gt "0" ]; then
  echo "Postgres Not installed, installing"
  sudo apt-get -y install wget ca-certificates
  wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
  sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
  sudo apt-get update
  sudo apt-get -y install postgresql postgresql-contrib
  echo "Done installing Postgres"
else
  echo "Postgres already installed"
fi

 service postgresql status
 if [ "$?" -gt "0" ]; then
   echo "Postgres is Not running, launching".
   service postgresql start
   echo "Postgres launched"
 else
   echo "Postgres already running"
 fi
