#!/usr/bin/python
# vim:fileencoding=utf-8
'''
 idn-lookup.py: IDN (Internationalized Domain Name) lookup support 

 Authors: Zdenek Vasicek (vasicek AT fit.vutbr.cz)
          Marek Vavrusa  (xvavru00 AT stud.fit.vutbr.cz)

 Copyright (c) 2008. All rights reserved.

 This software is open source.
 
 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions
 are met:
 
 Redistributions of source code must retain the above copyright notice,
 this list of conditions and the following disclaimer.
 
 Redistributions in binary form must reproduce the above copyright notice,
 this list of conditions and the following disclaimer in the documentation
 and/or other materials provided with the distribution.
 
 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
 TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE
 LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.
'''
from __future__ import print_function
import unbound
import locale

ctx = unbound.ub_ctx()
ctx.set_option("module-config:","iterator") #We don't need validation
ctx.resolvconf("/etc/resolv.conf")

#The unicode IDN string is automatically converted (if necessary)
status, result = ctx.resolve(u"www.háčkyčárky.cz", unbound.RR_TYPE_A, unbound.RR_CLASS_IN)
if status == 0 and result.havedata:
    print("Result:")
    print("      raw data:", result.data)
    for k in sorted(result.data.address_list):
        print("      address:%s" % k)

status, result = ctx.resolve(u"háčkyčárky.cz", unbound.RR_TYPE_MX, unbound.RR_CLASS_IN)
if status == 0 and result.havedata:
    print("Result:")
    print("      raw data:", result.data)
    for k in sorted(result.data.mx_list_idn):
        print("      priority:%d address:%s" % k)

status, result = ctx.resolve(unbound.reverse('217.31.204.66')+'.in-addr.arpa', unbound.RR_TYPE_PTR, unbound.RR_CLASS_IN)
if status == 0 and result.havedata:
    print("Result.data:", result.data)
    for k in sorted(result.data.domain_list_idn):
        print("      dname:%s" % k)
