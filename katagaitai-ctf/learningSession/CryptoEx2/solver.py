from Crypto.Util.number import long_to_bytes
from Crypto.Util.number import isPrime
import math

N = 14224882908410368764360484874067250400388978460672556891255759017098175256313350112865947942620259550657641892863278357156596163845551071024540508278775724866155378903436287808439690717384226344284098082766014654398833495788216422818786345558009286002776427768249668676948519395474270058331321470694849401101416099242223530653466558703573162382338400582086994992158271180818641679743996809111304540219769071624446246094219874558606679794376050922309695324744971897096923230695728118458370284781138238227312950245661877888897940668689991033328554791631373339072762955787982254713729601813249127066079370331369801505059
e = 65537
c = 14126261345724116189935573765798571201123559396873115386362384916908590205638517186580205445537352471744577267715036213801589914087499465098288392002498627799757398581743975061886396726421376479674451732390972030316611556814920979392928082900749901212629723043432030954781767875829697827744754995253138660953893115046782175857291607288653399091519253705753378669648782331584763778947071794867565964552305882316504605664521710416648017473785556498354177011417859388974666044281992633079667023529901396060617558180817442448043482988748016820412056041051959860175160057152196771273477931436777599522852656969096815641849

def next_prime(n):
    while True:
        n += 1
        if isPrime(n):
            return n

q = next_prime(int(math.isqrt(N)))
p=N//q
phi=(p-1)*(q-1)
d=pow(e,-1,phi)
m=pow(c,d,N)
print(long_to_bytes(int(m)))
