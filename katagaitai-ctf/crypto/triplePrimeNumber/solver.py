from Crypto.Util.number import long_to_bytes
from Crypto.Util.number import isPrime
import math

N = 67065672690003311763317709419239610557390343983642475637401743672576109945257067184833335724739055507713911257315218712587814893083624350883742409846705280437477167123258389279794173962158743669272579645355673342245762921030115425496807817179463838289989203454462239442929037937280576079274015891379372111920942638362069541216440451571876835309164009534472257137288932986602402701138615446175231785642792848820669091022296147160056161442272348780482860974581364602714484270631008573473898498428385421074872452077465881960139871928561910298478867269284810190424497649782935570132183725497729691409916508813245062130717
e = 65537
c = 48141562923871083014787967622878906989794337644154518693891607304653086195283748066464626227387560498174312882600915530896311873451719919881013485188886552136171663560506892992061365053564941028961783007281608994591890724343626429488198602396064077068317352966231341078531074244714250131439327527702967234197174610978175451434403144143929967942519339212638940715118885947858572492615370041199900154549327069364947064186401270502244647235839653174778612836848667894682929935646780724078041869331796039547774517905373955566804586398816127667745198939820021666387133349877782922343576819256878925770428220409970820294598

def next_prime(n):
    while True:
        n -= 1
        if isPrime(n):
            print(n)
            if (N % n == 0):
                return n
        
def checkTruePrime(q):
    while(True):
        if (N % q != 0):
            q = next_prime(q)

q = next_prime(int(math.isqrt(N//3)))

p=N//q
phi=(p-1)*(q-1)
d=pow(e,-1,phi)
m=pow(c,d,N)
print(p*q)
print(long_to_bytes(int(m)))