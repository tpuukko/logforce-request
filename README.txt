Help on module logforce_request:

NAME
    logforce_request

FILE
    /home/teemuki/Ohjelmointi/Logforce/logforce-xml/json/logforce-requests/logforce_request.py

DESCRIPTION
    Module gives ability to send HTTP-request to the Logforce server. Module contains two classes IntegrationRequest and 
    LogforceRequest. The IntegrationRequest is used to send a integration side request, as the LogforceRequest class
    is used to send a service side request. The integration side messages are for messages coming from Metsäjärjestelmäs,
    and the service side is for all Logforce clients as Lastaussovellus, Suunnittelusovellus and Ajoneuvosovellus.

CLASSES
    IntegrationRequest
    LogforceRequest
    
    class IntegrationRequest
     |  Class contains methods to make a integration side requests to Logforce Server
     |  
     |  Methods defined here:
     |  
     |  __init__(self, base_url)
     |      @Constructor
     |      @param {string} base_url requests base url, use some url from URLS dictionary
     |      @return {IntegrationRequest}
     |  
     |  post(self, service_url, data)
    
    class LogforceRequest
     |  Class contains methods to make a service side reqeust to Logforce server.
     |  @variable {request.Response} self.response contains last response object
     |  @variable {request.Response} self.authentication_response contains authentication request
     |  
     |  Methods defined here:
     |  
     |  __init__(self, base_url, client_version)
     |      @Constructor
     |      @param {string} base_url requests base url, use some url from URLS dictionary
     |      @param {string} client_version LF-Client-Version   
     |      @return {None}
     |  
     |  authenticate(self, username, password)
     |      Authenticate user to logforce server
     |      @param {string} username
     |      @param {string} password
     |      @return {LogforceRequest}
     |      @raise ConnectionError if connection fails
     |  
     |  delete(self, url)
     |      Makes a DELETE request to Logforce server
     |      !Not implemented!
     |  
     |  get(self, url, data=None)
     |      Makes a get request to Logforce server
     |      @param {String} url
     |      @param {dictionary} data
     |      @param {string} client_version, LF_CLIENT_VERSION number
     |      @param {request.Response} response object from authentication request
     |      @return {LogforceRequest}
     |  
     |  post(self, url, data=None)
     |      Makes a POST request to Logforce server
     |      @param {String} url
     |      @param {dictionary} data
     |      @param {string} client_version, LF_CLIENT_VERSION number
     |      @param {request.Response} response object from authentication request
     |      @return {LogforceRequest}
     |  
     |  pretty_response(self)
     |      Return last response reponses jsos as prettyfied
     |      @return {string}
     |  
     |  put(self, url, data)
     |      Makes a PUT request to Logforce server
     |      @param {String} url
     |      @param {dictionary} data
     |      @param {string} client_version, LF_CLIENT_VERSION number
     |      @param {request.Response} response object from authentication request
     |      @return {LogforceRequest}


