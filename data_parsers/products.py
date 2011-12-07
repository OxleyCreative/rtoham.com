import json
import parts
import repair_fees
import manuals

repairs = repair_fees.parse_repair_fees()
part_products = parts.parse_parts(repairs[1])
manual_products = manuals.parse_manuals(part_products[1])
products = repairs[0]
products.extend(part_products[0])
products.extend(manual_products[0])
print json.dumps(products)
