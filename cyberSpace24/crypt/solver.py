def is_prime(n):
    """nが素数かどうかを判定する関数"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(start, end):
    """指定した範囲内の素数を生成する関数"""
    primes = []
    for num in range(end, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def generate_prime(len):
    """指定した範囲内の素数を生成する関数"""
    primes = []
    i = 0
    while(i):
        if is_prime(num):
            primes.append(num)
    return primes

# 例: 100までの素数を生成
limit = 100
primes = generate_primes(limit)
print(primes)