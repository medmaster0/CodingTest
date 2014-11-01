from flask import Flask
app = Flask(__name__)

@app.route('/prob1')
def prob1():
    return ("Answer to Problem 1: \n \
    SELECT Car.id\n \
    FROM Car\n \
    INNER JOIN Owner\n \
    ON Car.owner_id=Owner.id \n \
    WHERE Owner.gender=0 \n \
    AND Owner.age>21; ")

@app.route('/prob2')
def prob2():
    return ("Program for Problem 2: \n \
    # Program to compute primes \n \
    # \n \
    # usage: \n \
    # python primes.py <N> \n \
    # \n \
    # input: \n \
    # N: compute all primes up to N \n \
    # \n \
    # output: \n \
    # list containing all primes up to N \n \
    # \n \
    # By Anthony Baca \n \
 \n \
    import sys \n \
 \n \
    N = int(sys.argv[1]) \n \
 \n \
    nums = range(2,N) #numbers we're going to test \n \
    for i in range(2,N): \n \
        nums = filter(lambda x: x==i or x % i, nums) #filter out those that are divisible \n \
\n \
    print nums")

if __name__ == '__main__':
    app.run()
