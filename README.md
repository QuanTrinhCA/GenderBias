# [Problem 1: Gender bias](https://www.unb.ca/saintjohn/sase/_assets/documents/problems2019.pdf)

With the new advances in artificial intelligence, there are now some software can that help 
with the pre-selection of candidates for jobs or positions (i.e., identify the most promising 
candidates). These typically check the applications received and identify the ones that are 
closer to the ones from people hired in the past. The danger here is that if the past selection 
process was biased (against a particular gender), then the new system would probably continue 
having such bias. It is thus important to test that the automatic selection is not biased. 

For this problem, you should write a program that will perform such test. We will assume here 
that an unbiased selection process is defined as one where every candidate has an equal 
chance of being selected. This would mean that if 40% of the candidates are women, then we 
would want to have about 40% of the selected candidates to be women as well (more or less). 

Your program should test 5 selection cases. For each case, there are 2 lines of input (for a total 
of 10 lines – see the example input below). The first line of the 2 contains 2 positive integers: 
the number of applications from male candidates and from female candidates respectively (in 
this order). The second line (of the 2) also has 2 numbers (zero or positive integer): the number 
of selected candidates from each gender (male and then female). What you have to do with 
these numbers is to first calculate what should have been the number of female candidates 
selected if the process was perfectly bias free. For example, in the first case below, this number 
should have been 7 (as 20 x 21 / 60). Note: this expected number will always be an integer. 
Then you should compare it with the actual number of female candidates selected. If the 
difference is 2 or less, then print “no bias”. If the difference is 5 or less (but larger than 2), print 
“some bias”. If the difference is higher than 5, print “heavily biased”. Also indicate the gender 
that is negatively affected.

For the example input below, here are the calculations:
Case 1 (lines 1 & 2): expected=7, actual= 8 -> no bias
Case 2 (lines 3 & 4): expected=10, actual=13 -> some bias against men
Case 3 (lines 5 & 6): expected=10, actual=10 -> no bias
Case 4 (lines 7 & 8): expected=15, actual=5 -> heavily biased against women
Case 5 (lines 9 & 10): expected=4, actual=10 -> heavily biased against men

## Sample Input 1
```
60 21
20 8
45 45
10 13
10 20
5 10
30 45
10 5
30 40
3 10
```

## Sample Output 1
```
no bias
some bias against men
no bias
heavily biased against women
heavily biased against men
```
