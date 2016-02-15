// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
// 'starter.controllers' is found in controllers.js
angular.module('starter', ['ionic', 'starter.controllers', 'starter.config'])

.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
    // for form inputs)
    if (window.cordova && window.cordova.plugins.Keyboard) {
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
      cordova.plugins.Keyboard.disableScroll(true);

      //To enable requests from an actual device.
      $httpProvider.defaults.useXDomain=true;
      delete $httpProvider.defaults.headers.common['X-Requested-With'];

    }
    if (window.StatusBar) {
      // org.apache.cordova.statusbar required
      StatusBar.styleDefault();
    }
  });
})

.config(function($stateProvider, $urlRouterProvider) {
  $stateProvider

    .state('app', {
    url: '/app',
    abstract: true,
    templateUrl: 'templates/menu.html',
    controller: 'AppCtrl'
    })  
    .state('app.organizations', {
      url: '/organizations',
      views: {
        'menuContent': {
          templateUrl: 'templates/organizations.html',
          controller: 'OrganizationsCtrl'
        }
      }
    })
    .state('app.organization', {
      url: '/organization/:organizationId',
      views: {
        'menuContent': {
          templateUrl: 'templates/organization.html',
          controller: 'OrganizationCtrl'
        }
      }
    })      
    .state('app.team', {
      url: '/team/:teamId',
      views: {
        'menuContent': {
          templateUrl: 'templates/team.html',
          controller: 'TeamCtrl'
        }
      }
    });
  // if none of the above states are matched, use this as the fallback
  $urlRouterProvider.otherwise('/app/organizations');
});
