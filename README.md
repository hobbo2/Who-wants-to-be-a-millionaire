### Video Demo:  https://www.youtube.com/watch?v=tT9st8okARY&ab_channel=AndrewHobson
#### Idea:
I got my idea for this small program after reading 'How to make your first million' by Graham Ingram.
In this book he outlines the time frame it will take to make your first million by investing in a stock index which tracks the global stock movements. I chose the S&p500 as it has a long history which means that the average year returns are more accurate.

#### Numbers and maths
According to my calculations and yahoo finance, the average annual return on the S&P500 is 11.88%. I took this rate and calculated the effective monthly rate at which it would be compounded.

Formula used: s = p - p (1 + i)**n     /      1 - (1 + i)

WHERE:
s = final amount ie 1 000 000
p = monthly installments
i = effective interest rate 11.88 / 12
n = periods ie 12 months x years

to calculate periods I used logarithms:
Denominator: 1 - (s * (1 - (1 + i)) / p)
numberator: 1 + i
periods = log(denominator) / log( 1 + i)

periods were then converted to years and months.

To calculate mothly installmants I went back to highschool maths using equations and arrived at the formula of:
p = s - s * (1 + i)   /     1 - (1 + i ) ** periods


#### How it works:
the program will prompt the user whether they want:
 A) to calculate the how long it will take to make 1 million given a set monthly investment. This approach assumes the user knows how much they can afford to invest each month.

 B) to calculate what amount the user should invest monthly given a set time period. This approach assumes the user knpws the time period which they want to reach 1 million.

 ### Result:
 The program will then output the amount invested and the years and months it will take to reach their goal


 ### Goal reached?
 Yes, I would confirm that I did what I wanted to achieve from this project. With more knowledge I would like to integrate API's so that a user could select a stock or etf and then be given 
 the result of how long itwould take for them to be a millionaire given mothly investment and the average return of a stock. This will highlight the effects of compounding interest. 
