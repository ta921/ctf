from pwn import *
from Crypto.Util.number import long_to_bytes
from Crypto.Util.number import isPrime
import math

c1 = 0x6295ebaa36e672c1049f96b46d8bf275992e5ad44312edada0339049819d617013b4bb0500ed9b1a286a6032e5fb67396114ca8a107827bd71557c63d5b11a2c0a90def603c3095d3514ea467e9a73b66ee8d80925a8c46ff57dc243cbe99986b83d2e28d1d0669bbe638af98a95710f3b663a82bf1370914327290e853b6f94dc4b522f03707d7870e8c6978dfd3a9520fcf62eb9eece248136e7ad18d98674c7bb95cb91671acdc27fe49a28093f56309bc8e3cbfffb5951aaf0032e8839d3b1552223e511dfe2244b5a070f8d31d7a02ac3a294134c4733af154a3c667262ae9e2fa38d3dc3d36c06bb936565474bcc161e84b32fb1c674fc4f7c524ec276
c2 = 0x65c579821feeec1166098897a31737b897dd8c40dfdb557c029a85ceb60ddc9e3096661581e8886dfe80bf17bc39835381681af0b67961e81433a9a7ab835c5a366dd8f2f1eca5505857225c5e172f4f7ee153ee97f01ff4bf6bdbdbbabaf766b5a0351a6f83f1e98b4ce2b2821c702eeb4af3c20d182b4a71faa01e2aea25e133fae457a4cbca7c938f2ef90b53f99871cdabf2ecb31e76f05058f16d812a27b5e5e41790198f9abc162f4623b962c0d8c95b043038b4dd781ddcd90e34c55cdf1e8e1c4871094bad5182dd2fc84dc3c9e65919aced1b288215bc8db01bc663facfe8ec6c4648664b3ea9e862452043c4a75beeaa50592df9db320c45be8a4d

c = c1 * c2
print(hex(c))
print(format(c, 'x'))

#FLAG is katagaitai-CTF{y0u_4r3_4_RSA_3ncryp710n_m4st3r}