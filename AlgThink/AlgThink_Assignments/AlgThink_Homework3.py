"""
Coursera / Rice University
Algorithmic Thinking (Part 2)
Module 3 Homework
"""

'''
Background:
Given an array A = [0...n-1], an inversion is a pair of indices
(i,j) such that 0 <= i < j <= n-1 and A[i] > A[j], or the
number of occurrences where an integer in the array is out of
ascending numerical order.
'''

'''
Q1
How many inversions are there in the array A = [5,4,3,6,7]?

ANSWER:
3
See below for a simple inversion counter.
'''
print "Q1 \nCountInversions"

def CountInversions(A):
    """
    Function that takes an array A and returns the num of
    inversions in the array.
    """
    n = len(A)
    i, j = 0, 0
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if A[i] > A[j]:
                count += 1
    return count

A = [5, 4, 3, 6, 7]
print CountInversions(A)

print "\n"

'''
Q2
In an array with n elements, what is the maximum possible 
number of inversions (as an expression in terms of n)?

ANSWER:
(n*(n-1))/2
It has a triangular growth rate; look at it manually from
n=0 to n=6 where each array is completely unordered such that
the elems are in descending numerical order, i.e. there are
maximum inversions in each array. The inversion count is,
respectively, 0, 0, 1, 3, 6, 10, 15. A quick lookup shows
a function of (n*(n-1))/2 driving that result.
'''

print "Q2 \nFinding max inversions \nas f(n)"

arrays = {}
arrays[0] = []
arrays[1] = [0]
arrays[2] = [1, 0]
arrays[3] = [2, 1, 0]
arrays[4] = [3, 2, 1, 0]
arrays[5] = [4, 3, 2, 1, 0]
arrays[6] = [5, 4, 3, 2, 1, 0]
for i in range(7):
    s = "A" + str(i) + ": " + str(arrays[i]) + \
    "\n" + "Inversions: " + str(CountInversions(arrays[i]))
    print s

print "\n"

'''
Q3
What is the best case running time of a brute-force algm that
counts the num of inversions in an array with n elems by
checking every pair of elems in the array? Choose the tightest
big-O bound for this best case time.

ANSWER:
O(nlogn)
One index, let's say i, has to traverse every single elem, 
which takes O(n) time, and index j will traverse increasingly
smaller elems from n-1 to 1 instead of all n-1 elements since
each (i,j) pair is the same as (j,i) and pairs are not 
counted twice. This is for best case, where the array is
already sorted in ascending numerical order.
'''

'''
Q4
Consider the divide and conquer algm for counting the num of
inversions in an array A. Below is the CountInversions algm
that is complete and the Merge algm that is not complete. You
must complete the identified missing components of the Merge
algm. 
Note: These algms will be written in Python by me for testing.

ANSWER:
Line 1: B[i] <= C[j]
Line 2: p - i
See finished algm below.
'''
print "Q4 \nCountInversions / Merge"

def CountInversions(A):
    """
    Input:  Array A[0...n-1]
    Output: The number of inversions in A
    """
    n = len(A)
    if n == 0 or n == 1:
        return 0
    else:
        B = list(A[:(n/2)])
        C = list(A[(n/2):])
        il = CountInversions(B)
        ir = CountInversions(C)
        im = Merge(B, C, A)
        return il + ir + im

def Merge(B, C, A):
    """
    Input:  Two sorted arrays B[0...p-1] and C[0...q-1],
            and an array A[0...p+q-1]
    Output: The num of inversions involving an elem from B
            and an elem from C. Modifies A.
    """
    p = len(B)
    q = len(C)
    count = 0
    i, j, k = 0, 0, 0
    while i < p and j < q:
        if B[i] <= C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
            count += p - i
        k += 1
    if i == p:
        A[k:p+q] = C[j:q]
    else:
        A[k:p+q] = B[i:p]
    return count
        
A = [6, 5, 4, 3, 2, 1, 0]
print "A:", A
print "Inversions:", CountInversions(A)
    
arrays = {}
arrays[0] = []
arrays[1] = [0]
arrays[2] = [1, 0]
arrays[3] = [2, 1, 0]
arrays[4] = [3, 2, 1, 0]
arrays[5] = [4, 3, 2, 1, 0]
arrays[6] = [5, 4, 3, 2, 1, 0]
for i in range(7):
    s = "A" + str(i) + ": " + str(arrays[i]) + \
    "\n" + "Inversions: " + str(CountInversions(arrays[i]))
    print s

print "\n"

'''
Q5
Which of the following gives the recurrence that results
in the tightest running time for the CountInversions algm?

ANSWER:
T(n) = 2T(n/2) + O(n)
I believe the running time to be similar to MergeSort such
that Merge takes O(n) times, judging by every element in the
passed arrays, totaling size n, being iterated through just
once--since even in worst case when you compare a very large
elem in array B to every one in C, after C is expended, you 
simply copy the rest of B to A. Think of it as adding one elem
to A with each comparison, and you can only add n elems to A
in total. The 2T(n/2) I think is similar to splitting the T(n)
running time of CountInversions into two since you split the list
into 2 equal(ish) sized arrays B and C, which take T(n/2) time.
You have 2 of these, so 2T(n/2) + O(n). 
'''

'''
Q6
Which of the following gives the tightest order of growth for the
solution of the following recurrence:
T(n) = 4T(n/2) + n, base: T(1) = 1

ANSWER:
O(n**3)
Look at the Master Theorem. The template is:
T(n) = aT(n/b) + f(n) base T(1) = c, a >= 1, b >= 2, c > 0. Then
f(n) = O(n**d) where d >= 0.
In this case, a = 4, b = 2, c = 1, and d = 1. We compare a to 
b**d to get 4 vs. 2**1 or 4 vs. 2. Since 4 > 2, a > b**d and
the MT says this function has O(n**logb(a)) time, which I looked
up to be equivalent to O(n**3) time.
'''

'''
Q7
Which of the following gives the tightest order of growth for the
solution of the following recurrence:
T(n) = 4T(n/2) + n**3, base: T(1) = 1.

ANSWER:
O(n**3)
Again, we have a = 4, b = 2, c = 1, and d = 3. Comparing a to 
b**d gives 4 vs. 2**3 or 4 vs. 8. Since 4 < 8, a < b**d. The MT
says the function has O(n**d) time, or in this case, O(n**3) 
time. Just like in Q6, but a different way of getting there.
'''

'''
Q8
Consider the mystery algm shown below. What does:
Mystery([-2, 0, 1, 3, 7, 12, 15], 0, 6) compute?

ANSWER:
3
See below for algm and computation. It appears to return an index
of array A where the value of A at that index is equal to the 
index. So A[i] is equal to i if i is returned by the function.
'''

print "Q8 \nMystery Algm"

def Mystery(A, l, r):
    """
    Takes a sorted array A and left and right boundaries l and
    r and returns a mystery output.
    """
    if l > r:
        return -1
    m = (l + r) / 2
    if A[m] == m:
        return m
    else:
        if A[m] < m:
            return Mystery(A, m + 1, r)
        else:
            return Mystery(A, l, m - 1)

A = [-2, 0, 1, 3, 7, 12, 15]
print "A:", A
print "Mystery(A):", Mystery(A, 0, 6)

print "\n"

'''
Q9
What does algm Mystery compute when run on input:
(A[0...n-1], 0, n-1)?

ANSWER:
Returns i if there exists an i such that A[i] = i, otherwise -1.
'''

'''
Q10
What are the best case and worst case running times of Mystery()
as a function of input size n (assume l <= r in the input)?

ANSWER:
Best: O(1)
This is because the algm may get lucky and choose the right index
with the first search (m = (l+r)/2; if A[m] == m, return m). This
midway point may in fact return the desired output.
Worst: O(logn)
This is because I believe the algm acts like a search algm. The
Mystery() function splits the boundaries, checks, and continues
to split the boundaries as it works its way in a single direction
to look for a match, much like BinarySearch. Since the array is
already sorted, it will always run at logn, never touching half
of the array's values.
'''

'''
Q11
Consider clusterings of points. Let S(n,k) denote the number of
ways that a set of n points can be clustered into k non-empty
clusters. Which of the following is a correct recurrence for
S(n,k) for n >= 1? Assume case cases S(n,n) = S(n,1) = 1.

ANSWER:
S(n,k) = kS(n-1, k) + S(n-1, k-1)
I had to look this up as it was not intuitive to me. I decided to
manually look at n = 0 to n = 6. Before plugging in any numbers,
draw out n numbered dots and start to cluster them into k total
clusters. If k = 2, you can cluster 1 into 0 clusters. For n = 2,
you can get 1 unique permutation of 2 clusters. For n = 3, you 
can make 2 clusters in 3 different ways. For n = 4, 7 perms. For
n = 5, 15 perms. Looking at the components of the equations 
listed as potential answers for this problem showed that the
one above, that I found, is indeed that which returns the correct
number of permutations given n points and k clusters. No clue.

Note: Correct. When deriving the recurrence, consider the case 
where the nth point goes into an existing non-empty cluster or 
when it creates a new cluster.
'''

'''
Q12
Which of the following formulas gives the number of ways of 
clustering a set of n points into 2 non-empty clusters? Look for
a solution to the recurrence from the previous question (k = 2).

ANSWER:
2**(n-1) - 1
I simply crunched the numbers on this one. In fact, I did this 
one prior to Q11 since it helped verify what I found online. Look
at my values for permutations vs. n in Q11 to see how this fits.

Note: Correct. Remember that there are 2**n subs of the n points.
Try to think of one cluster as a sub of the n points and the other
cluster as the complement of that subset. Alternatively, consider
implementing the recurrence in Python, computing the value of the
recurrence for small values of n, and deriving a pattern. (I did)
'''

'''
Q13
Consider the pseudocode for the hierarchical clustering algm:
-----------
HierarchicalClustering
Input: A set P of points whose ith point, p_i, is a pair 
(x_i,y_i); k, the desired number of clusters.
Output: A set C of k clusters that provides a clustering of the
points in P.
-----------
1.  n <- |P|
2.  Initialize n clusters C = {C_1....C_n} where C_i = {p_i}
3.  while |C| > k do
4.      (C_i, C_j) <- argmin_Ci,Cj E C, i!=j d_Ci,Cj
5.      C <- C U {C_i U C_j}
6.      C <- C \ {C_i, C_j}
7.  return C
-----------
Assuming that line 4 takes h(n) time in each iteration, for some
function h, which of the following gives the worst-case running
time of the algm as a function of n when k = 1? Assume that the
union and difference of two sets A and B takes O(|A| + |B|) time.

ANSWER:
O(n**2 + h(n)n)
First take into account that k = 1. Line 2 will create a C with
n clusters, each with exactly one point. Line 3 will cluster as 
long as the length of C is larger than k, which is 1. This means 
that it will loop through until there is only 1 cluster, and all
points in C have been joined together to form one giant cluster
of all n points. What appears to be happening in the while loop
is Line 4, which takes h(n) time, and which looks at two clusters
C_i and C_j, an arbitrary i and j presumably but which are not
equal, and returns some sort of distance measure d_Ci,Cj. Lines 5
and 6 then, respectively, add the cluster {C_i U C_j} and remove
the individual clusters C_i and C_j. 
So to step back, this is taking two points, computing a distance,
and replacing the individual points in C with a cluster that 
contains both points. C lost 2 elems for 1 larger one. I don't
know what O(|A| + |B|) means with regard to the assumption that
the union and difference of two sets A and B take this time to
compute. I'm simply seeing two steps that together, in the worst
case possible, grow a set C by one element. Think if the largest
cluster is always C_i and C_j is always just one point. You are
slowly adding one point to a list, which takes n time. Judging by
that, Lines 4-6 should take h(n) + n time.
Since the while loop runs as long as set C has more than 1 elem,
and we're adding 1 point to the largest cluster at a time, I can
assume that it will run n times. While loop = O(n), which runs
h(n) + n steps each time, so n(h(n) + n) or O(n**2 + h(n)n). This
is how I trudged through this and it may be wrong...we'll see.
'''

'''
Q14
Consider the pseudocode of the k-means clustering algm:
-----------
KMeansClustering
Input: A set P of points whose ith point p_i is a pair (x_i,y_i);
k, the desired number of clusters; q, a number of iterations.
Output: A set C of k clusters that provides a clustering of 
points in P.
-----------
1.  n <- |P|
2.  Initialize k centers mu_1...mu_k to initial values (each mu
    is a point in the 2D space)
3.  for i <- 1 to q do
4.      Initialize k empty sets C_1 ... C_k
5.      for j = 0 to n-1 do
6.          l <- argmin_1<=f<=k d_pj,muf
7.          C_l <- C_l U {p_j}
8.      for f = 1 to k do
9.          mu_f = center(C_f)
10. return {C_1 ... C_k}
-----------
Which of the following gives the tightest worst-case running time
of the algm as a function of the number of points n and the num
of clusters k and the num of iterations q? Assume that adding
{p_j} to C_l in line 7 takes O(1) time.

ANSWER:
O(q k n)
First let's look at what this does. It creates a variable n which
is the num of points in P. It initializes k presumably random
centers in the 2D space. Then a loop runs from 1 to q, so that 
should theoretically be the first component that affects the
running time significantly. Each loop then initializes k empty
sets and then two more subloops are run. The first runs from n
times, each time computing some kind of distance measure and then
finding the cluster C_l that best fits for point p_j (j = 1 to n)
and adding the point to it. The second runs from f = 1 to k to
update center mu_f to the center of cluster C_f. 
So for each of q loops, first a loop from 1 to n is run, then one
from 2 to k+1 (adjusting for actual 1 to k, 0 to n-1). At first
glance it seems like O(q(n + k)) would fit best, but the options
are 1) O(qkn), 2) O(qkn**2), 3) O(qknlogn), 4) O(kn) and it is
not there. So I need to rethink this.
What is going on then? With each iteration until q, you create k
empty sets, then you run through a loop from 0 to n-1 finding the
center that is closest to each point (I think) and then adding
that point to the cluster C_l that fits best. Then a loop from 1
to k that recenters the mu values. 
So q is absolutely involved in the running time. It's hard not
to think that k is also involved since k centers are retained
throughout the entire process. Line 7 takes O(1) time as per the
question, so Line 6 really determines, upon close inspection, the
running time that's dependent on n. Since it appears to be going
through each point every time (d_pj, muf) then I'd say each point
gets hit with this computation every time. 
A closer inspection of line 6:
l <- argmin_l<=f<=k d_pj,muf
Leads me to suspect that this distance is calculated for every k.
Sooooo, that means that from 1 to q, you run from j = 0 to n-1 a 
calculation that runs from 0 to k-1 on each point p_j. I'm
satisfied with this conclusion.
'''

'''
Q15
Consider a list of n numbers sorted in ascending order. Which of
the following gives the worst-case running time of the most
efficient algm for finding a closest pair of numbers in the list?

ANSWER:
O(n log n)
I looked this up. Divide and conquer in 1D space yields O(nlogn)
running time, presumably in worst case scenario based on the 
material I referenced to find this answer.
'''

'''
Q16
Consider the pseudocode of the brute force algm for closest pair:
-----------
SlowClosestPair
Input: A set P of (>=2) points whose ith point p_i is a pair 
(x_i, y_i).
Output: A tuple (d, i, j) where d is the smallest pairwise dist
of points in P, and i,j are the indices of two points whose
distance is d.
-----------
1.  (d,i,j) <- (INF, -1, -1)
2.  for each p_u E P do
3.      for each p_v E P (u != v) do
4.          (d,i,j) <- min{(d,i,j), (d_pu,pv, u, v)} 
            // min compares 1st elem of each tuple
5.  return (d,i,j)
-----------
Which of the following gives the tightest worst-case running time
of the algm in terms of the number of points n?

ANSWER:
O(n**2)
Let's look at what this is doing. Line 1 initializes d=INF, i,j=
-1,-1. So the variables are given necessary placeholder values.
A loop froms for each point in P, then another loop runs for each
point in P that is not included in the first loop. The question 
is does each p_u,p_v comparison get counted as unique? Line 4
seems to look at distance d of i,j and compare it to the newly
computed distance d_pu,pv and the i,j values with smallest dist
are assigned to i and j before the inner loop runs again. As 
written, it very much appears to have O(n**2) time with no regard
for i and j vs. j and i as the same distance computation. 
'''

'''
Q17
Consider pseudocode for divide and conquer algm for solving the
closest pair problem:
-----------
FastClosestPair
Input: A set P of (>=2) points whose ith point p_i is a pair
(x_i,y_i) SORTED in nondecreasing order of their horizontal (x) 
coordinates.
Output: A tuple (d,i,j) where d is the smallest pairwise dist
of the points in P, and i,j are indices of two points whose
distance is d.
-----------
1.  n <- |P|
2.  if n <= 3 then
3.      (d,i,j) <- SlowClosestPair(P)
4.  else
5.      m <- (n/2)
6.      P_l <- {p_i: 0<=i<=m-1}; P_r <- {p_i: m<=i<=n-1}
        // P_l and P_r are also sorted
7.      (d_l,i_l,j_l) <- FastClosestPair(P_l)
8.      (d_r,i_r,j_r) <- FastClosestPair(P_r)
9.      (d,i,j) <- min{(d_l,i_l,j_l), (d_r,i_r+m,j_r+m)}
10.     mid <- 1/2(x_m-1 + x_m)
11.     (d,i,j) <- min{(d,i,j), ClosestPairStrip(P,mid,d)}
12. return (d,i,j)
-----------
If the helper function ClosestPairStrip used in line 11 has a
worst case running time of O(f(n)), which of the recurrences
models the running time of FastClosestPair? You may assume that
ClosestPairStrip examines all of its input and, therefore, f(n)
grows at least as fast as n. Here, d is a constant.

ANSWER:
T(n) = 2T(n/2) + n
T(2) = d
Considering that this is divided into 2 halves, and while f(n)
grows AT LEAST as fast as n, it could grow faster than n, so
I get what I got. We'll see if it's right.
'''

'''
Q18
Consider pseudocode for ClosestPairStrip:
-----------
ClosestPairStrip
Input: A set P of points whose ith point p_i is (x_i,y_i);
mid and w both of which are real numbers.
Output: A tuple (d,i,j) where d is the smallest pairwise dist
of points in P whose horizontal (x) coords are within w from mid.
-----------
1.  Let S be a list of the set {i: |x_i - mid| < w}
2.  Sort the indices in S in nondecreasing order of the vertical
    (y) coords of their associated points
3.  k <- |S|
4.  (d,i,j) <- (INF, -1, -1)
5.  for u <- 0 to k-2 do
6.      for v <- u+1 to min{u+3, k-1} do
7.          (d,i,j) <- min{(d,i,j), (d_PS[u],PS[v], S[u], S[v])}
8.  return (d,i,j)
-----------
If n is the size of the input P, what is the worst case running
time of ClosestPairStrip?

ANSWER:
O(nlogn)
I'm kind of stumped. The algm seems to do the following: (1) Let
S be a list of indices where the distance of x_index to mid is
less than w; (2) Sort the indices in S in ascending order of  y
coords; (3) initialize k to num of elems in S; (4) initialize
(d,i,j) to placeholders; (5) loop through u=0 to k-2; (6) loop
through v=u+1 to min(u+3, k-1); (7) Calculate a distance between
some two points and assign min value to (d,i,j); (8) return
(d,i,j).
First, I think the sorting probably affects the runtime, being
O(nlogn) time at its fastest. The outer loop runs from 0 to k-2
and the inner from 1 to min(3,k-1). Because these distance
calculations are left up in the air, it's hard to say what 
exactly is going on and how long it's taking to compute during
these steps. The answer options are (1) O(nlogn), (2) O(n), 
(3) O(n**2), and (4) O(n**2 logn). 
It appears that the sort is O(nlogn) and you add the time it 
takes to run the nested loop k-2 times. The size of k is 
dependent on the number of indices in S. It seems, in line 1,
that worst case is mid = 0 and w = maximum value of x in the
set, where you look at x_i minus zero, or x_i, being less than
the max value of x_i you can get or some number larger than the
max value. So length of S would be n if every index of every 
point is in it. So the outer loop runs 0 to n-2, the inner from
1 to either 3 or n-1. Since min 3 is small, let's say that's
constant kind of, and you run O(nlogn) + O(n) which is really
just O(nlogn).

Note: Correct. S may include all of the points in P so the sort in
line 2 costs O(nlogn) time in worst cases. Note that lines 5-7
require only O(n) time.
'''

'''
Q19
Based on your answers to Q17 and Q18, what is the worst case
running time of FastClosestPair? Review the MT.

ANSWER:
O(nlogn)
From Q17, I got T(n)= 2T(n/2) + f(n), base: T(2) = d. From Q18 I
got f(n) = O(nlogn). So T(n) = 2T(n/2) + nlogn. a = 2, b = 2,
c = d (dist), and d = 1, I think. 2 = 2**1, so according to the
MT, T(n) = O(n**d logn) or O(nlogn).
'''

'''
Q20
If the algm for ClosestPairStrip could be modified such that its
running time f(n) is O(n), what would be the worst case running
time of FastClosestPair? Again, use your answer from Q17 and
consult the MT.

ANSWER:
O(nlogn)
If f(n) = n, then d still equals 1, and nothing changes.
'''

print "INCORRECT ANSWERS, FIRST ATTEMPT"
print "Q3: Incorrect. As described, the brute force algm \
examines all pairs of elements and, thus, can't be O(nlogn)"
print "Q6: Incorrect. Review the MT."
print "Q15: Incorrect. A faster method is possible."
print "Q19: Incorrect. The worst case running time is slightly \
slower"
print "REVISITED EACH IN NOTES"
print "\n"

'''
Q3
What is the best case running time of a brute-force algm that
counts the num of inversions in an array with n elems by
checking every pair of elems in the array? Choose the tightest
big-O bound for this best case time.
OPTIONS: (1) O(n**2), (2) O(1), (3) O(n**3), (4) O(n), 
(5) O(nlogn)

ANSWER:
O(nlogn) - INCORRECT
Note: Incorrect. As described, the brute force algm examines all
pairs of elems and thus can't be O(nlogn).

NEW ANSWER:
O(n**2)
Rationalized due to the note that every pair is examined. I assume
that means that i and j are two indices traversing the array each
n times, a total of n**2 times. 
'''

'''
Q6
Which of the following gives the tightest order of growth for the
solution of the following recurrence:
T(n) = 4T(n/2) + n, base: T(1) = 1
OPTIONS: (1) O(n**2), (2) O(n), (3) O(nlogn), (4) O(logn),
(5) O(n**3)

ANSWER:
O(n**3) - INCORRECT
Note: Review the MT.

NEW ANSWER:
O(n**2)
Let's look again at this recurrence. a = 4, b = 2, c = 1, d = 1.
This seems to be pretty obvious. Compare a to b**d again,
we get 4 vs. 2**1 or 4 vs. 2. a > b**d, so the MT says that this
has O(n**log_b(a)) running time. This, however, is not one of 
the options listed above. My previous source for converting this
to n**3 must have been mistaken. Unless I did crunch the numbers.
Let's look at logb(a). That's log2(4) or 2. I could've looked at that
incorrectly as log_b**a instead of log_b(a). So if that equals 2, the
MT says O(n**2) is the answer.
'''

'''
Q15
Consider a list of n numbers sorted in ascending order. Which of
the following gives the worst-case running time of the most
efficient algm for finding a closest pair of numbers in the list?
OPTIONS: (1) O(n), (2) O(nlog**2(n)), (3) O(logn), 
(4) O(nlogn), (5) O(log**2(n))

ANSWER:
O(n log n) - INCORRECT
Note: A faster method is possible.

NEW ANSWER:
O(log**2(n))
By process of elimination, O(nlog**2(n)) is off the table because
it is slower. The other 3 are options: O(n), O(log**2(n)), and
O(logn). This doesn't seem to be linear because increasing n
will increase the pairs that need to be compared, so I'm taking
O(n) off the table. I could rationalize that a 1D list of n numbers
can have indices i and j traverse the list, and since it is described
as "the most efficient algm" for finding a closest pair, the i,j pairs
will be considered the same as j,i pairs, so those are eliminated.
So you have n**2 but n is diminishing at logn rate for both i and
j. I would have to say that worst case, O(log**2(n)) makes the
most sense, since nlogn initially made sense, but since that n
component would also diminish in size, logn would be fitting. I
don't think it is in total O(logn) because you are always comparing
2 indices across the entire list. O(logn) makes sense if you are 
disregarding half of that list at a time. 
'''

'''
Q19
Based on your answers to Q17 and Q18, what is the worst case
running time of FastClosestPair? Review the MT.
OPTIONS: (1) O(nlog**2(n)), (2) O(nlogn), (3) O(n**2 logn),
(4) O(n**2 log**2(n))

ANSWER:
O(nlogn) - INCORRECT
Note: The worst case running time is slightly slower. Consider
the part of the MT where f(n) = Th(n**c log**k(n)) where 
c = log_b(a) (or in the notes where a = b**d). 

NEW ANSWER:
O(nlog**2(n))
From Q17, T(n) = 2T(n/2) + f(n), base T(2) = d. This is correct. 
From Q18, f(n) = O(nlogn). This is also correct. So from these, I
get a = 2, b = 2, and d = 1? According to Wiki, linked in the note, 
f(n) = Th(n**c log**k(n)) where c = log_b(a) and then
T(n) = Th(n**c log**k+1(n)). In the example given on wiki:
T(n) = 2T(n/2) + 10n. a = 2, b = 2, c = 1, f(n) = 10n. 
f(n) = Th(n**c log**k(n)) where c = 1, k = 0.
Next we see if we satisfy the case 2 condition:
log_b(a) = log_2(2) = 1, therefore yes c = log_b(a).
So it follows from the second case of the MT:
T(n) = Th(n**log_b(a) log**k+1(n)) = Th(n**1 log**1(n)) = Th(nlogn).
Thus the given recurrence relation T(n) was in Th(nlogn).
This is confirmed by the exact solution of the recurrence relation, 
T(n) = n + 10nlog_2(n), assuming T(1) = 1.
So what does that mean for me here? 
f(n) = nlogn, c = 1, k = 1.
See if we can satisfy the case 2 condition:
log_b(a) = log_2(2) = 1, and therefore c (1 in this case) = log_b(a).
So it follows from the second case of the MT that:
T(n) = Th(n**log_b(a) log**k+1(n)) = Th(n**1 log**2(n)) = O(nlog**2(n)).
This is "slightly slower", as per the note, than nlogn. The other two options
multiply this by either another n (much slower) or another n AND logn
(even slower).
'''

print "INCORRECT ANSWERS, FIRST ATTEMPT"
print "Q15: Incorrect. The method must examine all of the n points"
print "Final thoughts on remaining incorrect answers below"

'''
Q15
Consider a list of n numbers sorted in ascending order. Which of
the following gives the worst-case running time of the most
efficient algm for finding a closest pair of numbers in the list?
OPTIONS: (1) O(n), (2) O(nlog**2(n)), (3) O(logn), 
(4) O(nlogn), (5) O(log**2(n))

ANSWER:
O(n log n) - INCORRECT
Note: A faster method is possible.

NEW ANSWER:
O(log**2(n)) - INCORRECT
Note: The method must examine all of the n points.

REMAINING OPTIONS:
O(n)
O(nlog**2(n))
O(n**2)

THOUGHTS:
I'm not sure. If O(nlogn) wasn't fast enough, and O(log**2(n))
did not examine all n points, what's left? O(n**2) and O(nlog**2(n))
are both slower than O(nlogn), so O(n) is the only one left. I assume
the most efficient algm is some kind of divide and conquer. The MT
would have a form T(n) = 2T(n/2) + n I think, where O(n) time is
the result of the analysis. I'm really not sure!!!!!!!!!!!!!!!!!!!!
'''