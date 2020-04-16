import hubspot
HUBSPOT_API_KEY="YOUR API KEY"
print ("Creating client")
hubspot_client = hubspot.Client.create(HUBSPOT_API_KEY)
print ("Getting contacts SimplePublicObjectInput")
from hubspot.crm.contacts import SimplePublicObjectInput
print ("Making contacts client and calling create")
cc_cl  = hubspot_client.crm.contacts()
contact_input = SimplePublicObjectInput({"email":"some_name@some_email2.com"})
contacts_api = hubspot_client.crm.contacts().basic_api()
print(contacts_api.create(simple_public_object_input=contact_input))

print ("getting deals SimplePublicObjectInput")
from hubspot.crm.deals import SimplePublicObjectInput
deals_input = SimplePublicObjectInput({"dealname":"test_api_deal"})
print("can't make deal until associations are fixed")
#hubspot_client.crm.deals.basic_api.create(simple_public_object_input=deals_input)
print ("getting pipelines")
pipelines = hubspot_client.crm
pipelines = pipelines.pipelines
pipelines = pipelines.pipelines_api
from hubspot.crm.pipelines import PipelineInput
print ("getting all pipelines for deals")
print(pipelines.get_all("deals"))
print ("checkin auth can be constructed")
ss = hubspot_client.auth
ss = ss.oauth
print("owner api")
own_api = hubspot_client.crm.owners
from hubspot.crm.owners import PublicOwner
print(own_api.default_api.get_page())

