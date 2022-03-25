All projects require Python 3 to run.
# String and words
Get a count of all words in a text file, or create a copy with a word replaced.
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
Convert a time to another timezone. Optionally, account for user-defined daylight savings start and end times.
## Functionality
### Transform to another timezone.
All dates are in the ISO 8601 format
```
python3 date-time-transformation.py <date and time> <new UTC offset>
```

Example:
```
> python3 date-time-transformation.py 2000-01-01T00:00:00+0000 -6
1999-12-31T18:00:00-0600
```
### Transform to another timezone and set daylight savings time start & end.
```
python3 date-time-transformation.py <date and time> <new UTC offset> <dst start> <dst end>
```

# Big Number Computation
Use Python's built in big integer calculations to perform math on large numbers, including calculations with a decimal place in one number.
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