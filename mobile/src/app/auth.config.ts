import { isPlatform } from '@ionic/angular';
import config from '../../capacitor.config';

export const domain = 'dev-codeiain.us.auth0.com';
export const clientId = 'sNjX38pTiG4b8ZPlft81689j914AzivC';
const { appId } = config;

// Use `auth0Domain` in string interpolation below so that it doesn't
// get replaced by the quickstart auto-packager
const auth0Domain = domain;
const iosOrAndroid = isPlatform('hybrid');

export const callbackUri = iosOrAndroid
  ? `${appId}://${auth0Domain}/capacitor/${appId}/callback`
  : 'https://4200-codeiain-openaidm-2ginbwaibrm.ws-eu97.gitpod.io/';
