# String and words
## Functionality
### Get word count of text file.
```
python3 string-and-words.py -c <text file>
``` 
### Replace words and save as a new text file.
```
python3 string-and-words.py -r <text file> <new text file> <old word> <new word>
```

# Date & Time Transformation
## Functionality
### Transform to another timezone.
All dates are in the ISO 8601 format
```
python3 date-time-transformation.py -c <date and time> <offset>
```

Example:
```
> python3 date-time-transformation.py 2000-01-01T00:00:00+0000 -6
1999-12-31T18:00:00-0600
```
### Transform to another timezone and set daylight savings time start & end.
```
python3 date-time-transformation.py -c <date and time> <offset> <dst start> <dst end>
```

# Big Number Computation
## Functionality
### Add or subtract two numbers
```
python3 big-number-computation.py <number 1> <operator> <number 2>
```
Example
```
> python3 big-number-computation.py 100000000000000000000000000000 - 200000000000000000000000000000.1
-99999999999999999999999999999.9
```