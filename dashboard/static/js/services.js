angular.module('starter.services', [])

/**
 * A simple example service that returns some data.
 */
.factory('api', function($http, apiEndpointUrl) {
  // Might use a resource here that returns a JSON array
  var response;

  //var api_endpoint = 'http://localhost:8001';

  //Injected during server deployment via gulp task
  var api_endpoint = apiEndpointUrl;

  return {
    getOrganizations: function() {
      return $http.get(api_endpoint+'/organizations/').then(function(data){
          console.log(data.data);
          response = data.data;
          return response;
      });
    },

    getOrganization: function(organizationId) {
      return $http.get(api_endpoint+'/organizations/'+organizationId+'/').then(function(data){
          console.log(data.data);
          response = data.data;
          return response;
      })
    },

    getTeam: function(teamId) {
      return $http.get(api_endpoint+'/teams/'+teamId+'/').then(function(data){
          console.log(data.data);
          response = data.data;
          return response;
      });
    }    
  }
});