import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouteReuseStrategy } from '@angular/router';
import { SocketIoModule } from 'ngx-socket-io';
import { IonicModule, IonicRouteStrategy } from '@ionic/angular';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { environment } from '../environments/environment';

import { AuthConfig, AuthModule } from '@auth0/auth0-angular';
import { domain, clientId, callbackUri } from './auth.config';
import { SharedModule } from './shared';
import { HttpClientModule } from '@angular/common/http';
import { environment as env } from '../environments/environment';

const config: AuthConfig = {
  domain,
  clientId,
  authorizationParams: {
    redirect_uri: callbackUri,
  },
  // For using Auth0-Angular with Ionic on Android and iOS,
  // it's important to use refresh tokens without the falback
  useRefreshTokens: true,
  useRefreshTokensFallback: false,
};

// <2>
@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule,
    IonicModule.forRoot(),
    AppRoutingModule,
    SharedModule,
    HttpClientModule,
    SocketIoModule.forRoot(environment.socketIoConfig),
    AuthModule.forRoot({
      ...env.auth0,
    })],
  providers: [{ provide: RouteReuseStrategy, useClass: IonicRouteStrategy }],
  bootstrap: [AppComponent],
})
export class AppModule {}
