import math

p = 17909846913545745386493125908911854263612607106728915603127212965314247637657396372818592280407128818660705831885720947282813640280389079563410780620656876283468254976455745562098067562146959
g = 2
h = 17413104517515011241192863348863107702560336383889971529984431408575370876996707903625705222778267725132532332524986272558385317746947010007867166622016461148283342557497614544448296154406991

# Baby-step Giant-step法
def babystep_giantstep(g, y, p, q=None):
    if q is None:
        q = p - 1
    m = int(q**0.5 + 0.5)
    # Baby step
    table = {}
    gr = 1  # g^r
    for r in range(m):
        table[gr] = r
        gr = (gr * g) % p
        print (q, r, m)
    # Giant step
    try:
        gm = pow(g, -m, p)  # gm = g^{-m}
    except:
        return None
    ygqm = y                # ygqm = y * g^{-qm}
    for q in range(m):
        print (q, q, m)
        if ygqm in table:   # 左辺と右辺が一致するとき
            return q * m + table[ygqm]
        ygqm = (ygqm * gm) % p
    return None

# Pohlig–Hellman法
def pohlig_hellman_DLP(g, h, p):
    crt_moduli = []
    crt_remain = []
    for q, _ in factor(p-1):
        x = babystep_giantstep(pow(g,(p-1)//q,p), pow(h,(p-1)//q,p), p, q)
        if (x is None) or (x <= 1):
            continue
        crt_moduli.append(q)
        crt_remain.append(x)
    x = crt(crt_remain, crt_moduli)
    return x

x = pohlig_hellman_DLP(g, h, p)
print(x)
print(pow(g, x, p) == h)