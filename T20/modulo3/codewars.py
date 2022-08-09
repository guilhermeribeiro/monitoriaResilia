def ips_between(start, end):
    ip_ini = start.split('.')
    ip_ini = [int(x) for x in ip_ini]
    ip_fim = end.split('.')
    ip_fim = [int(x) for x in ip_fim]

    a = (ip_fim[0] - ip_ini[0])
    b = (ip_fim[1] - ip_ini[1])
    c = (ip_fim[2] - ip_ini[2])
    d = (ip_fim[3] - ip_ini[3])
    
    if a == 0 and b == 0 and c == 0:
        return d
    elif a == 0 and b == 0:
        return d + (c*256)
    elif a == 0:
        return d + (b*256) + (c*256)

    return d + (b*256) + (c*256) + (a*256)

 #53.155.94.168 and 255.255.255.255
 #118615 should equal 3395592535

# test.assert_equals(ips_between("10.0.0.0", "10.0.0.50"), 50)
# test.assert_equals(ips_between("20.0.0.10", "20.0.1.0"), 246)
# * With input "10.0.0.0", "10.0.0.50"  => return   50 
# * With input "10.0.0.0", "10.0.1.0"   => return  256 
# * With input "20.0.0.10", "20.0.1.0"  => return  246
print(ips_between("53.155.94.168", "255.255.255.255"))
