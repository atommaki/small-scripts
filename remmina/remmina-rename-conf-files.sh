#!/bin/bash

# Rename files in the ~/.remmina dir:
#   [0-9]*[0-9].remmina -> ${USERNAME}@${SERVER}.remmina

cd ~/.remmina

for FILE in [0-9]*[0-9].remmina
do
    USERNAME=$(grep ^username= $FILE | cut -d= -f2)
    SERVER=$(grep ^server= $FILE | cut -d= -f2)
    if [ "$USERNAME$SERVER" != "" ]; then
        if [ "$USERNAME" != "" ]
            then NEWFILENAME="${USERNAME}@${SERVER}.remmina"
            else NEWFILENAME="${SERVER}.remmina"
        fi
        N=0
        NEWFILENAME_X=$NEWFILENAME
        while [ -e $NEWFILENAME_X ]; do
            N=$[N+1]
            NEWFILENAME_X=${NEWFILENAME}_$N
        done
        mv -v $FILE $NEWFILENAME_X
    fi
done

