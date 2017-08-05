from pyzillow.pyzillow import ZillowWrapper, GetUpdatedPropertyDetails, GetDeepSearchResults
import requests

zillow_key = "X1-ZWz1fwbv0vp1xn_34dhf"
myaddress = '7007 N Stratton ct Peoria IL'
zipcode = '61615'

def getLastSoldDate(address):
    zillow_data = ZillowWrapper(zillow_key)
    deep_search_response = zillow_data.get_deep_search_results(address, zipcode)
    result = GetDeepSearchResults(deep_search_response)
    return result.last_sold_date



