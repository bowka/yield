# yield
what is it, how it works:)

please install IDLE 
sudo apt-get install idle3

create new file yield.py


### yield
[jiːld]

#### verb

  - produce or provide (a natural, agricultural, or industrial product).
   "the land yields grapes and tobacco"
  
  - give way to arguments, demands, or pressure.
   "the Western powers now yielded when they should have resisted"
   synonyms:	surrender, capitulate, submit, relent, admit defeat, accept defeat, concede defeat, back down, climb down, quit,    give in, give up the struggle, lay down one's arms, raise/show the white flag, knuckle under; More 

#### noun

  - an amount produced of an agricultural or industrial product.
   "the milk yield was poor"



TASK 1:
create array of divisors
```sh
def divisor(n):
    ...
def divisorYield(n):
    ...
n = 103045624  
print('my number is : %s' %str(n))    
start1 = time.time()
Array = divisor(n)
time1 = time.time()-start1
print('divisors by array: %s' %str(time1))
print(Array)
print()

start2 = time.time()
Yield = divisorYield(n)
time2 = time.time()-start2
print('divisors by generator: %s' %str(time2))
print(list(Yield))
print(Yield)
```



https://wiki.python.org/moin/Generators
http://struct.input.sk/04.html
