def parse_manuals(pk):
    data = """AM-2 Excellent $10.00 AR-3 Good $10.00 B-1 Excellent $ 5.00 CO-1 Excellent $ 5.00 DX-35 Good $20.00 DX-35 Schematic/spec 5.00 DX-60 Excellent $25.00 DX-60 Good $15.00 DX-60B Excellent $25.00 DX-60B Schematic/spec 5.00 GCW-1000-H Exc. $20.00 GH-17A Excellent $ 5.00 GR-54 Very Good $25.00 GR-110 Condnsd. Gd. $15.00 GR-110 Fair $15.00 GR-1131 Excellent $30.00 GR-1132 Very Good $30.00 GW-21 Fair $ 5.00 HA-10 Very Good $20.00 HA-14 Very Good $20.00 HA-20 Excellent $25.00 HA-201 Excellent $ 5.00 HA-201A Excellent $ 5.00 HA-202 Excellent $15.00 HA-202A Excellent $15.00 HD-10 Excellent $15.00 HD-15 $10.00 HD-16 Excellent $ 5.00 HD-1234 Excellent $ 5.00 HD-1250 Excellent $15.00 HD-1274 Excellent $ 5.00 HD-1410 Copy $10.00 HD-1416 Excellent $ 5.00 HD-1416A Excellent $ 5.00 HD-1416H Excellent $ 5.00 HD-1418 Excellent $20.00 HD-1418A Excellent $20.00 HD-1420 Excellent $20.00 HD-1422 Excellent $20.00 HD-1422A Excellent $20.00 HD-1424 Excellent $20.00 HD-1424A Excellent $20.00 HD-1481 Excellent $20.00 HD-1530 Excellent $20.00 HD-1984 Excellent $10.00 HD-1986 Excellent $15.00 HD-3006 Excellent $10.00 HD-3030 Excellent $25.00 HD-3030 Very Good $20.00 HD-4040 (users) Exc. and HD-4040 (assembly) E $40.00 HD-4040 (assembly) E $20.00 HD-4040 shematic $ 5.00 HD-8999 Excellent $25.00 HDA-3030-4 Excellent $10.00 HDA-3030 Illustration booklet $5 HFT-9 Excellent $10.00 HFT-9A Excellent $10.00 HG-10 Excellent $15.00 HG-10B Excellent $15.00 HK-232 (assembly) E and HK-232 (user) E $40.00 HK-232 (assembly) E $25.00 HL-2200 Excellent $25.00 HM-9 Excellent $15.00 HM-10 Excellent $10.00 HM-10A Excellent $10.00 HM-11 Excellent $10.00 HM-15 Very Good $ 8.00 HM-15 Good $ 5.00 HM-102 $10.00 HM-2102 Excellent $10.00 HM-2103 Excellent $15.00 HM-2103 schematic-spec $3.00 HM-2140 Excellent $15.00 HN-31 Excellent $ 5.00 HN-31A Excellent $ 5.00 HO-13 Excellent $25.00 HO-5404 Excellent $25.00 HP-13 Excellent $10.00 HP-13A Excellent $10.00 HP-13B Excellent $10.00 HP-14 Excellent $12.00 HP-23 Excellent $10.00 HP-23B schematic/spec 3.00 HP-24 schematic/spec 3.00 HP-1175 Excellent $15.00 HP-1175 Good $10.00 HR-20 Good $20.00 HR-1680 Excellent $25.00 HR-1680 Schematic $ 15.00 HS-24 Excellent $ 5.00 HW-2-M Bandwidth modific. $5 HW-2-P Bandwidth modific. $5 HW-2-XL Bandwidth modific. $5 HW-7 Excellent $20.00 HW-7 schematic/spec $ 3.00 HW-9 Excellent $25.00 HWA-9 Excellent $10.00 HW-10 Very Good $25.00 HW-12A Excellent $25.00 HW-12A E (condensed) $15.00 HW-16 Excellent $25.00 HW-16 Good $20.00 HW-16 shematic/spec $ 3.00 HW-17A Very Good $25.00 HW-18-1 Good $20.00 HW-18-1 Fair $15.00 HW-18-3 Excellent $25.00 HW-18-3 Good $20.00 HW-19 Excellent $20.00 HW-20 Good $20.00 HW-22 schematic/spec $ 3.00 HW-22A Fair $15.00 HW-22A condensed $15.00 HW-29 Excellent $20.00 HW-29A Excellent $20.00 HW-30 Excellent $20.00 HW-30 Very Good $15.00 HW-32 Fair $15.00 HW-32 condensed $15.00 HW-100 Fair $20.00 HW-101 Fair $20.00 HW-202 Fair $20.00 HW-202 Very Good $25.00 HWA-202-1 Very Good $10.00 HW-2021 Excellent $25.00 HW-2021 Good $10.00 HW-2021 Very Good $20.00 HW-2036 condensed $25.00 HW-2036 copy $25.00 HW-2036 schematic $ 3.00 HW-2036 Modification kit $10.00 HWA-2036-3 Excellent $15.00 HWA-2036-4 Excellent $10.00 HW-5400 (operation) Exc. and (assembly) Excellent $40.00 HW-5400 (operation) Exc. $15.00 HW-5400 (assembly) Exc. $30.00 HW-5400 (assembly) Poor $15.00 HW-5400 update sheet $ 3.00 HX-10 Very Good $30.00 HX-11 Excellent $15.00 HX-20 Very Good $25.00 HX-20 Copy $30.00 HX-20 condensed $25.00 HX-20 (schematic/spec) E $ 5.00 HX-30 Excellent $30.00 HX-30 (schematic/spec) E $ 3.00 HX-1681 Very Good $25.00 HX-1681 Condensed $20.00 KL-1 Excellent $25.00 PS-23 Excellent $15.00 SA-1480 Very Good $15.00 SA-2040 Excellent $20.00 SA-2060A Excellent $25.00 SA-5010 Excellent $20.00 SA-7010 Excellent $10.00 SB-10 Good $15.00 SB-10 copy $10.00 SB-102 schematic only $ 3.00 SB-102 condensed $20.00 SBM-102-1 Modification kit $ 3.00 SB-104A operation $25.00 SBM-104-2 Excellent $15.00 SB-230 condensed $20.00 SB-230 water stained $10.00 SB-230 Excellent $30.00 SBA-300-3 Excellent $10.00 SBA-300-4 Excellent $10.00 SB-301 Condensed $15.00 SB-303 Very Good $30.00 SB-400 Good $25.00 SB-401 Fair $20.00 SB-500 Very Good $30.00 SB-500 Condensed $20.00 SB-600 Excellent $ 5.00 SB-604 Excellent $ 8.00 SB-614 Excellent $30.00 SB-620 Very Good $20.00 SB-634 Good $20.00 SB-634 Excellent $25.00 SB-640 Excellent $15.00 SB-644 Excellent $20.00 SB-650 Excellent $30.00 SB-650 (condensed) $15.00 SB-650 Very Good $25.00 SB-1000 Very Good $25.00 SB-1400 (operation-copy) $10.00 VF-1 Excellent $10.00 VF-1 Fair $ 5.00 VF-2031 Fair $15.00 VF-2031-3 Excellent $ 5.00 VF-2031-6 Excellent $ 5.00 VF-7401 Good $20.00 VF-7401 Very Good $25.00 VFA-7401-1 Excellent $10.00 VL-1180 Excellent $25.00 VL-2280 Excellent $25.00 VP-1-6 Excellent $ 5.00 VP-1-6 schematic/spec $ 3.00 VP-1-12 Excellent $ 5.00"""
    import re
    import datetime
    conditions = ["very good", "good", "excellent", "exc.",
                  "water stained", "fair"]

    matches = re.findall(r'(([\w\-./()]+\s)+)\$\s?(\d+[.]\d\d)', data)
    models = []
    for match in matches:
        name = match[0].strip()
        slug = re.sub('[^\w\-]$', '', name)
        slug = 'manuals-' + re.sub('[^\w\-]', '-', slug).lower()
        slug = slug[:50]

        description = "We carry the " + name + " manual in our collection."
        for condition in conditions:
            pattern = r'\s' + condition
            if re.search(pattern, name, re.I) != None:
                name = re.sub(pattern, '', name, flags=re.I)
                description = re.sub(pattern, '', description, flags=re.I)
                description += " It is in " + condition + " condition."
                break
            
        description += " Please contact us for exact pricing and availability."
        models.append({
                    "pk": pk,
                    "model": "products.product",
                    "fields": {
                        "category": "MANUALS",
                        "title": name,
                        "description": description,
                        "price": match[2],
                        "slug": slug,
                        "created_at": str(datetime.datetime.now()),
                        "modified_at": str(datetime.datetime.now())
                        }
                    })
        pk += 1
    return (models, pk)

