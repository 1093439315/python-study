# for-in-else + range()

# 判断一个数是不是素数(质数) prime
# 除了 1 和自身以外不能被其它任何数整除

# % mod 取模（取余数）
# n % m == 0 n 可被 m 整除

# 1. 循环遍历出 2 ~ num-1 的数
# 2. 如何判断 num 会被 i 整除
# 3. 如何确认通过所有数字整除的检测
# 4. for-in-else

num = 58653761

#is_prime = True

for i in range(2, num): # 2 <= i < num
    #print(i)
    if num % i == 0:
        #is_prime = False
        print(num, 'not a prime!')
        break
else:
    print(num, 'a prime')

# 报告：num a prime.
#if is_prime:
#    print(num, 'a prime')





