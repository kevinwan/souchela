#!/bin/sh

echo Number of lines of Python code:
find souche -name "*.py" -print | grep -v "migrations" | xargs cat | \
    grep -v -e "[[:space:]]*#" -e "^[[:space:]]$" | wc -l

echo Number of lines of Javascript code:
find souche/static/js -name "*.js" -print | xargs cat | \
    grep -v -e "^[[:space:]]*$" -e "^[[:space:]]*//" -e "^[[:space:]]*/\*" \
    -e "^[[:space:]].*\*/" | wc -l

echo Number of lines of HTML code:
find souche -name "*.html" -print | xargs cat | wc -l

echo Number of lines of CSS code:
find souche -name "*.css" -print | xargs cat | wc -l
