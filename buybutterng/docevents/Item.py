import frappe
import json
import requests
import os
import time
from requests_oauthlib import OAuth1Session

def createWooItems(doc=None, method=None):
	woo_settings = frappe.get_doc("Woo Connect")
	print(woo_settings)
	try:
		if woo_settings:
			_create_woo_item(doc);
	except Exception as e:
		frappe.log_error(e)
		print(e)




def _create_woo_item(doc): 
	if doc.name: # .woocommerce_id
		frappe.flags.wooconnect_data = {
			"description": doc.description,
			# "id": doc.item_code,
			"name": doc.item_name,
			"short_description": doc.description
		}

		woo_settings = frappe.get_doc("Woo Connect")

		if woo_settings.consumer_key and woo_settings.consumer_secret:
			url = "https://buybetter.ng/wp-json/wc/v3/products"

			payload = json.dumps(frappe.flags.wooconnect_data)

			headers = {
			'Content-Type': 'application/json'
			}

			oauthRequest = OAuth1Session(woo_settings.consumer_key,
                    client_secret=woo_settings.consumer_secret)
			response = oauthRequest.request("POST", url, headers=headers, data=payload)
			print(oauthRequest)
			print(frappe.flags.wooconnect_data)
			print(response.text)
			
	# frappe.flags.wooconnect_data = {
	# 	"id": 75,
	# 	"parent_id": 0,
	# 	"number": "74",
	# 	"order_key": "wc_order_5aa1281c2dacb",
	# 	"created_via": "checkout",
	# 	"version": "3.3.3",
	# 	"status": "processing",
	# 	"currency": "INR",
	# 	"date_created": "2018-03-08T12:10:04",
	# 	"date_created_gmt": "2018-03-08T12:10:04",
	# 	"date_modified": "2018-03-08T12:10:04",
	# 	"date_modified_gmt": "2018-03-08T12:10:04",
	# 	"discount_total": "0.00",
	# 	"discount_tax": "0.00",
	# 	"shipping_total": "150.00",
	# 	"shipping_tax": "0.00",
	# 	"cart_tax": "0.00",
	# 	"total": "649.00",
	# 	"total_tax": "0.00",
	# 	"prices_include_tax": False,
	# 	"customer_id": 12,
	# 	"customer_ip_address": "103.54.99.5",
	# 	"customer_user_agent": "mozilla\\/5.0 (x11; linux x86_64) applewebkit\\/537.36 (khtml, like gecko) chrome\\/64.0.3282.186 safari\\/537.36",
	# 	"customer_note": "",
	# 	"billing": {
	# 		"first_name": "Tony",
	# 		"last_name": "Stark",
	# 		"company": "_Test Company",
	# 		"address_1": "Mumbai",
	# 		"address_2": "",
	# 		"city": "Dadar",
	# 		"state": "MH",
	# 		"postcode": "123",
	# 		"country": "IN",
	# 		"email": "tony@gmail.com",
	# 		"phone": "123457890",
	# 	},
	# 	"shipping": {
	# 		"first_name": "Tony",
	# 		"last_name": "Stark",
	# 		"company": "",
	# 		"address_1": "Mumbai",
	# 		"address_2": "",
	# 		"city": "Dadar",
	# 		"state": "MH",
	# 		"postcode": "123",
	# 		"country": "IN",
	# 	},
	# 	"payment_method": "cod",
	# 	"payment_method_title": "Cash on delivery",
	# 	"transaction_id": "",
	# 	"date_paid": "",
	# 	"date_paid_gmt": "",
	# 	"date_completed": "",
	# 	"date_completed_gmt": "",
	# 	"cart_hash": "8e76b020d5790066496f244860c4703f",
	# 	"meta_data": [],
	# 	"line_items": [
	# 		{
	# 			"id": 80,
	# 			"name": "Marvel",
	# 			"product_id": 56,
	# 			"variation_id": 0,
	# 			"quantity": 1,
	# 			"tax_class": "",
	# 			"subtotal": "499.00",
	# 			"subtotal_tax": "0.00",
	# 			"total": "499.00",
	# 			"total_tax": "0.00",
	# 			"taxes": [],
	# 			"meta_data": [],
	# 			"sku": "",
	# 			"price": 499,
	# 		}
	# 	],
	# 	"tax_lines": [],
	# 	"shipping_lines": [
	# 		{
	# 			"id": 81,
	# 			"method_title": "Flat rate",
	# 			"method_id": "flat_rate:1",
	# 			"total": "150.00",
	# 			"total_tax": "0.00",
	# 			"taxes": [],
	# 			"meta_data": [{"id": 623, "key": "Items", "value": "Marvel &times; 1"}],
	# 		}
	# 	],
	# 	"fee_lines": [],
	# 	"coupon_lines": [],
	# 	"refunds": [],
	# }

	# frappe.flags.wooconnect_data = {}


# def post_request():
# 	# Emulate Woocommerce Request
# 	headers = {
# 		"X-Wc-Webhook-Event": "created",
# 		"X-Wc-Webhook-Signature": "h1SjzQMPwd68MF5bficeFq20/RkQeRLsb9AVCUz/rLs=",
# 	}
# 	# Emulate Request Data
# 	data = """{"id":74,"parent_id":0,"number":"74","order_key":"wc_order_5aa1281c2dacb","created_via":"checkout","version":"3.3.3","status":"processing","currency":"INR","date_created":"2018-03-08T12:10:04","date_created_gmt":"2018-03-08T12:10:04","date_modified":"2018-03-08T12:10:04","date_modified_gmt":"2018-03-08T12:10:04","discount_total":"0.00","discount_tax":"0.00","shipping_total":"150.00","shipping_tax":"0.00","cart_tax":"0.00","total":"649.00","total_tax":"0.00","prices_include_tax":false,"customer_id":12,"customer_ip_address":"103.54.99.5","customer_user_agent":"mozilla\\/5.0 (x11; linux x86_64) applewebkit\\/537.36 (khtml, like gecko) chrome\\/64.0.3282.186 safari\\/537.36","customer_note":"","billing":{"first_name":"Tony","last_name":"Stark","company":"Woocommerce","address_1":"Mumbai","address_2":"","city":"Dadar","state":"MH","postcode":"123","country":"IN","email":"tony@gmail.com","phone":"123457890"},"shipping":{"first_name":"Tony","last_name":"Stark","company":"","address_1":"Mumbai","address_2":"","city":"Dadar","state":"MH","postcode":"123","country":"IN"},"payment_method":"cod","payment_method_title":"Cash on delivery","transaction_id":"","date_paid":null,"date_paid_gmt":null,"date_completed":null,"date_completed_gmt":null,"cart_hash":"8e76b020d5790066496f244860c4703f","meta_data":[],"line_items":[{"id":80,"name":"Marvel","product_id":56,"variation_id":0,"quantity":1,"tax_class":"","subtotal":"499.00","subtotal_tax":"0.00","total":"499.00","total_tax":"0.00","taxes":[],"meta_data":[],"sku":"","price":499}],"tax_lines":[],"shipping_lines":[{"id":81,"method_title":"Flat rate","method_id":"flat_rate:1","total":"150.00","total_tax":"0.00","taxes":[],"meta_data":[{"id":623,"key":"Items","value":"Marvel &times; 1"}]}],"fee_lines":[],"coupon_lines":[],"refunds":[]}"""

# 	# Build URL
# 	port = frappe.get_site_config().webserver_port or "8000"

# 	if os.environ.get("CI"):
# 		host = "localhost"
# 	else:
# 		host = frappe.local.site

# 	url = "http://{site}:{port}/api/method/erpnext.erpnext_integrations.connectors.woocommerce_connection.order".format(
# 		site=host, port=port
# 	)

# 	r = requests.post(url=url, headers=headers, data=data)

# 	time.sleep(5)
# 	return r