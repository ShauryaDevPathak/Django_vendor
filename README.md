# Django_vendor
Vendor_management_system_api

# Different API endpoints:
-	**“GET”, “POST” all vendors: <br/>**
Go to http://127.0.0.1:8000/api/vendors

- **“GET”, “PUT”, “DELETE” a specific vendor based on vendor_id:**<br/>
Go to http://127.0.0.1:8000/api/vendors/<vendor_id>

-	**“GET”, performance of a vendor:**<br/>
Go to http://127.0.0.1:8000/api/vendors/<vendor_id>/performance

-	**“GET”, “POST” View all purchase orders:**<br/>
Go to http://127.0.0.1:8000/api/purchase_orders

-	**“GET”, “PUT”, “DELETE” View a specific purchase order based on purchase_id:**<br/>
Go to http://127.0.0.1:8000/api/purchase_orders/<purchase_id>

-	**“POST” Acknowledge api:**<br/>
Go to http://127.0.0.1:8000/api/purchase_orders/<purchase_id>/acknowledge

**Note:** *The vendor_id and purchase_id are the default primary keys assigned by Django. They are always integers.*
