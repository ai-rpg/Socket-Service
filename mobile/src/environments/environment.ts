// This file can be replaced during build by using the `fileReplacements` array.
// `ng build` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.

export const environment = {
  production: false,
  socketIoConfig: { // <1>
    url: '5001-codeiain-openaidm-2ginbwaibrm.ws-eu97.gitpod.io', // <2>
    options: {}
  },
  auth0: {
    domain: 'dev-codeiain.us.auth0.com',
    clientId: 'sNjX38pTiG4b8ZPlft81689j914AzivC',
    authorizationParams: {
      redirect_uri: 'https://4200-codeiain-openaidm-2ginbwaibrm.ws-eu97.gitpod.io',
    },
    errorPath: '/callback',
  },
  api: {
    serverUrl: 'https://6060-codeiain-openaidm-2ginbwaibrm.ws-eu97.gitpod.io',
  },
};

/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/plugins/zone-error';  // Included with Angular CLI.
