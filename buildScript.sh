#!/bin/bash
echo "Welcome to the Build demo!"

firstline=$(head -n 1 source/changelog.md)
read -a splitfirstline <<< $firstline
version=${splitfirstline[1]}
echo "You are building version" $version

echo "Enter 1 to continue and 0 to exit"
read versioncontinue
if [ $versioncontinue -eq 1 ]
then
  echo "Oke"
  for filename in source/*
  do
    if [ $filename == "source/secretinfo.md" ]
    then
      echo $filename "was not copied because it is a secret"
    else
      echo $filename "was copied"
      cp $filename build/.
    fi
  done
  cd build/
  echo "Build version $version contains:"
  ls
  cd ..
else
  echo "Please return when you are ready to build!"
fi