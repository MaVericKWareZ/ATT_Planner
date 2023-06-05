farmrise-annotationtool-backend
==============================

Backend for annotating images and responding with the annotation response to an annotation tool client

Local Development
-----------------

1. Install PostgreSQL using brew.
2. Start the PostgreSQL service and create a database with the following configuration:

   - Name: annotationtool_local
   - Owner: postgres
3. Create a local settings file:

.. code-block:: sh

   mkdir -p local
   cp att_planner/project/settings/templates/settings.dev.py ./local/settings.dev.py
   cp att_planner/project/settings/templates/settings.unittests.py ./local/settings.unittests.py

4. Run the update command:

.. code-block:: sh

   make update

5. Apply migrations (if any):

.. code-block:: sh

   make migrations
   make migrate

6. Run the server:

.. code-block:: sh

   make run-server


## Signing Key = 9ba0ef42d0bdf1f6bd89c63fe176a944827191d63843bb80e7ce9aa8b79b5c60
## Account Number = 8921459a844db20787198b7cebbca2b08eeb0fab8edce9e7d4b19b224451d16d
## SECRET_KEY = p#2gi=9x9wf4)#m-h52032tssdu#4=)+!gwt$u=3h*bi)%dn6@
