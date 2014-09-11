#!/bin/bash
##
# This section should match your Makefile
##
PELICAN=pelican
PELICANOPTS=

BASEDIR=$PWD
INPUTDIR=$BASEDIR/content
OUTPUTDIR=$BASEDIR/output
CONFFILE=$BASEDIR/pelicanconf.py

###
# Don't change stuff below here unless you are sure
###

SRV_PID=$BASEDIR/srv.pid
PELICAN_PID=$BASEDIR/pelican.pid

function usage(){
  echo "usage: $0 (stop) (start) (restart)"
  echo "This starts pelican in debug and reload mode and then launches"
  echo "A SimpleHTTP server to help site development. It doesn't read"
  echo "your pelican options so you edit any paths in your Makefile"
  echo "you will need to edit it as well"
  exit 3
}

function shut_down(){
  if [[ -f $SRV_PID ]]; then
    PID=$(cat $SRV_PID)
    PROCESS=$(ps -p $PID | tail -n 1 | awk '{print $4}')
    if [[ $PROCESS == python ]]; then
      echo "Killing SimpleHTTPServer"
      kill $PID
    else
      echo "Stale PID, deleting"
    fi
    rm $SRV_PID
  else
    echo "SimpleHTTPServer PIDFile not found"
  fi

  if [[ -f $PELICAN_PID ]]; then
    PID=$(cat $PELICAN_PID)
    PROCESS=$(ps -p $PID | tail -n 1 | awk '{print $4}')
    if [[ $PROCESS != "" ]]; then
      echo "Killing Pelican"
      kill $PID
    else
      echo "Stale PID, deleting"
    fi
    rm $PELICAN_PID
  else
    echo "Pelican PIDFile not found"
  fi
}

function start_up(){
  echo "Starting up Pelican and SimpleHTTPServer"
  shift
  $PELICAN --debug --autoreload -r $INPUTDIR -o $OUTPUTDIR -s $CONFFILE $PELICANOPTS &
  echo $! > $PELICAN_PID
  cd $OUTPUTDIR
  python -m SimpleHTTPServer &
  echo $! > $SRV_PID
  cd $BASEDIR
}

###
#  MAIN
###
[[ $# -ne 1 ]] && usage
if [[ $1 == "stop" ]]; then
  shut_down
elif [[ $1 == "restart" ]]; then
  shut_down
  start_up
elif [[ $1 == "start" ]]; then
  start_up
else
  usage
fi
