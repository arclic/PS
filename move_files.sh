#! /bin/bash

BAEKJOON_DIRECTORIES=$(ls)

for directory in $BAEKJOON_DIRECTORIES
do
    if [ -d $directory ] && [ $directory != 'baekjoon' ] && [ $directory != 'programmers' ]
    then
        mv "./$directory/baekjoon.py" "baekjoon/$directory.py"
        rm -rf $directory
    elif [ $directory == 'programmers' ]
    then
        cd programmers
        PROGRAMMERS_DIRECTORIES=$(ls)
        for dir in $PROGRAMMERS_DIRECTORIES
        do
            mv "./$dir/programmers.py" "$dir.py"
            rm -rf $dir
        done
    fi
done