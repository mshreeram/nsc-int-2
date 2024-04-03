def sha1(message):
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0
    bytes = ""
    for i in message:
        bytes += '{0:08b}'.format(ord(i))
    bits = bytes + "1"
    pbits = bits
    while len(pbits) % 512 != 448:
        pbits += '0'
    pbits += '{0:064b}'.format(len(bits) - 1)

    def chunks(arr, n):
        return [arr[i: i + n] for i in range(0, len(arr), n)]
    
    def rol(num, p):
        return ((num << p) | (num >> (32 - p))) & 0xffffffff
    
    a = h0
    b = h1
    c = h2
    d = h3
    e = h4

    for chunk in chunks(pbits, 512):
        words = chunks(chunk, 32)
        w = [0] * 80
        for i in range(16):
            w[i] = int(words[i], 2)
        for i in range(16, 80):
            w[i] = rol((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1)
        
        for i in range(80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k =  0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6
            
            temp = rol(a, 5) + f + e + k + w[i] & 0xffffffff
            e = d
            d = c
            c = rol(b, 30)
            b = a
            a = temp
        
        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff
    
    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

print(sha1("my name is shreeram"))