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


# Filling the database:
You can fill the database from the admin page. Go to http://127.0.0.1:8000/admin and login with an admin/superuser account.

# Test for Token-based-authentication:
- Going to the API endpoints directly will give you error since token-based-authentication is on
- To test this authentication, do the following steps:
    +Go to http://127.0.0.1:8000/admin
    +Go to “Tokens”
    +Click on add tokens
    +Select admin (or any other superuser name)
    +Open a terminal in the project directory and type the following command:
      curl -X GET http://127.0.0.1:8000/api/vendors -H 'Authorization: Token [your token]'
**Note:** *insert your token in [your token] part of the command*
  - JSON of the existing vendors should be displayed on the terminal
