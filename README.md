# Django_vendor
Vendor_management_system_api<br/>
**Note:** *The "Test.pdf" contains the demonstration*

# Starting the project:
- Download and extract the zip file
- Open _mysite_ file and open a terminal
- **Run:** python manage.py runserver
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
- Going to the API endpoints directly will give you error since token-based-authentication is on<br/>
- To test this authentication, do the following steps:<br/>
    -Go to http://127.0.0.1:8000/admin<br/>
    -Go to “Tokens”<br/>
    -Click on add tokens<br/>
    -Select admin (or any other superuser name)<br/>
    -Open a terminal in the project directory and type the following command:<br/>
      curl -X GET http://127.0.0.1:8000/api/vendors -H 'Authorization: Token [your token]'<br/>
**Note:** *insert your token in [your token] part of the command*<br/>
- JSON of the existing vendors should be displayed on the terminal<br/>

# Running the tests for API:
- You must disable the token-authentication to run the following tests.
    - Go to mysite/api/views.py and comment out all the lines containing:
      @authentication_classes([TokenAuthentication])<br/>
      @permission_classes([IsAuthenticated])<br/>
- **For Vendors:**
    - Go to the respective end points and use the get, post, put and delete methods as you please.
    - For post and put methods you must give input as a JSON.
    - Some examples of JSON:
      <br/>
        {
            "name": "Vendor One",
            "contact_details": "2341563748",
            "address": "123 Test Street",
            "vendor_code": "vendor123"
        }
      <br/>
        {
            "name": "Vendor Three",
            "contact_details": "2647893674",
            "address": "789 Elm Street",
            "vendor_code": "vendor456"
        }
      <br/>
    - The vendor_id is derived from “id” column. This column is automatic incrementing integer column.<br/>Therefore, any new POST you make will be assigned a number starting from 1.
    - If a vendor is deleted, the vendor_id which is not empty will not be used by some other vendor

- **For Orders:**
    - Go to the respective end points and use the get, post, put and delete methods as you please.
    - For post and put methods you must give input as a JSON.
    - Some examples of JSON:<br/>
        {
        "po_number": "abc3",
        "vendor": 5,
        "order_date": "2024-05-01T03:24:52Z",
        "expected_delivery_date": "2024-05-03T12:00:00Z",
        "actual_delivery_date": "2024-05-03T12:00:00Z",
        "items": "{\"item1\": \"desc1\"}",
        "quantity": 5,
        "status": "pending",
        "quality_rating": null,
        "issue_date": "2024-05-01T03:30:52Z",
        "acknowledgment_date": "2024-05-01T03:46:46.551265Z"
        }
      <br/>
    - The purchaseorder_id is derived from “id” column. This column is automatic incrementing integer column. Therefore, any new POST you make will be assigned a number starting from 1.
    - If an order is deleted, the purchaseorder_id which is not empty will not be used by some other order
    - **Note:** for updating the metrics the status should be “completed.” Use PUT to update the status and update the metrics

- **For acknowledgement Api:**
    - Go to the api end point and click on POST with no input.
    - The performance metrics are updated automatically
