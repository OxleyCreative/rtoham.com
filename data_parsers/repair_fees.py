def parse_repair_fees():
 import re
 import json
 import datetime

 data = """<P><FONT SIZE="-1">DX-40.................$75.00</FONT></P>
         <P><FONT SIZE="-1">DX-60.................$75.00</FONT></P><P><FONT SIZE="-1">HA-201...............$49.00</FONT></P>
         <P><FONT SIZE="-1">HA-202...............$79.00</FONT></P>
         <P><FONT SIZE="-1">HD-10.................$79.00</FONT></P>
         <P><FONT SIZE="-1">HD-15.................$39.00</FONT></P>
         <P><FONT SIZE="-1">HD-16.................$35.00</FONT></P>
         <P><FONT SIZE="-1">HD-1250.............$75.00</FONT></P>
         <P><FONT SIZE="-1">HD-1410.............$68.00</FONT></P>
         <P><FONT SIZE="-1">HD-1418.............$97.00</FONT></P>
         <P><FONT SIZE="-1">HD-1481.............$70.00</FONT></P>
         <P><FONT SIZE="-1">HD-1515.............$55.00</FONT></P>
         <P><FONT SIZE="-1">HD-8999.............$97.00</FONT></P>
         <P><FONT SIZE="-1">HG-10.................$58.00</FONT></P>
         <P><FONT SIZE="-1">HL-2200............$140.00</FONT></P>
         <P><FONT SIZE="-1">HM-102..............$39.00</FONT></P>
         <P><FONT SIZE="-1">HM-2102............$39.00</FONT></P>
         <P><FONT SIZE="-1">HM-2140............$58.00</FONT></P>
         <P><FONT SIZE="-1">HM-2141............$58.00</FONT></P>
         <P><FONT SIZE="-1">HO-10.................$88.00</FONT></P>
         <P><FONT SIZE="-1">HO-13.................$98.00</FONT></P>
         <P><FONT SIZE="-1">HO-5404............$105.00</FONT></P>
         <P><FONT SIZE="-1">HO-5404-1.........$75.00</FONT></P>
         <P><FONT SIZE="-1">HP-13(A,B)........$75.00</FONT></P>
         <P><FONT SIZE="-1">HP-23(A,B,C)....$75.00</FONT></P>
         <P><FONT SIZE="-1">HP-1144.............$88.00</FONT></P>
         <P><FONT SIZE="-1">HP-1144A..........$88.00</FONT></P>
 <P><FONT SIZE="-1">HP-1175..............$75.00</FONT></P><P><FONT SIZE="-1">HR-10..................$88.00</FONT></P><P><FONT SIZE="-1">HR-1680..............$88.00</FONT></P><P><FONT SIZE="-1">HW-7..................$75.00</FONT></P><P><FONT SIZE="-1">HW-8..................$75.00</FONT></P><P><FONT SIZE="-1">HW-9..................$98.00</FONT></P><P><FONT SIZE="-1">HW-12,22,32......$93.00</FONT></P><P><FONT SIZE="-1">HW-16................$93.00</FONT></P><P><FONT SIZE="-1">HW-99..............$108.00</FONT></P><P><FONT SIZE="-1">HW-100,101.....$115.00</FONT></P><P><FONT SIZE="-1">HW-104............$135.00</FONT></P><P><FONT SIZE="-1">HW-104A........$125.00</FONT></P><P><FONT SIZE="-1">HW-202.............$88.00</FONT></P><P><FONT SIZE="-1">HW-2021....no service</FONT></P><P><FONT SIZE="-1">HW-2036(A)....$110.00</FONT></P><P><FONT SIZE="-1">HW-5400..........$145.00</FONT></P><P><FONT SIZE="-1">HWA-5400-1.....$98.00</FONT></P><P><FONT SIZE="-1">HX-10...............$145.00</FONT></P><P><FONT SIZE="-1">HX-1681.............$98.00</FONT></P><P><FONT SIZE="-1">PS-9000..............$98.00</FONT></P><P><FONT SIZE="-1">RX-1..................$145.00</FONT></P><P><FONT SIZE="-1">SA-2040..............$88.00</FONT></P><P><FONT SIZE="-1">SA-2060(A)........$98.00</FONT></P><P><FONT SIZE="-1">SA-2500............$158.00</FONT></P><P><FONT SIZE="-1">SA-2550..............$63.00</FONT></P><P><FONT SIZE="-1">SA-5010(A)........$88.00</FONT></P><P><FONT SIZE="-1">SB-10...................$88.00 </FONT></P>"""

 matches = re.findall(r'>([\w\-(,)]+)[.]+\$(\d+[.]\d{2})\s?<', data)
 models = []
 pk = 1
 for match in matches:
     slug = re.sub('[^\w\-]$', '', match[0])
     slug = 'repairs-' + re.sub('[^\w\-]', '-', slug).lower()
     models.append({
             "pk": pk,
             "model": "products.product",
             "fields": {
                 "category": "REPAIRS",
                 "title": match[0],
                 "description": "Send your " + match[0] + " to us for repair.",
                 "price": float(match[1]),
                 "slug": slug,
                 "created_at": str(datetime.datetime.now()),
                 "modified_at": str(datetime.datetime.now())
                 }
             })
     pk += 1
 return (models, pk)
