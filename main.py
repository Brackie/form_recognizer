import json


json_format = [
	{
		"receipt_type": "Itemized",
		"merchant": "Contoso",
		"address": "123 Main Street Redmond, WA 98052",
		"telephone": "+19876543210",
		"Date": "2019-06-10",
		"Time": "13:59:00",
		"Subtotal": "1098.99",
		"Tax": "104.4",
		"Total": "1203.39",
		"items": [
			{
				"Item Quantity": 1,
				"Item Name": "Surface Pro 6",
				"Total Price": 999.00,
			},
			{
				"Item Quantity": 1,
				"Item Name": "Surface Pen",
				"Total Price": 99.00,
			}
		]
	}
]

# the json file where the output must be stored 
out_file = open("receipts.json", "w")
json.dump(json_format, out_file, indent = 4) 
out_file.close()