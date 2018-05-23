import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';
import { FormsModule } from '@angular/forms';
import { masterConfig } from './api-keys';
import { AngularFireModule } from 'angularfire2';
import { AngularFireDatabaseModule } from 'angularfire2/database';
import { AngularFireAuthModule } from 'angularfire2/auth';

import { AppComponent } from './app.component';
import { routing } from './app.routing';
import { RoverFormComponent } from './rover-form/rover-form.component';
import { PhotosListComponent } from './photos-list/photos-list.component';

import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import { UserPhotosListComponent } from './user-photos-list/user-photos-list.component';
import { PublicComponent } from './public/public.component';
import { PrivateComponent } from './private/private.component';

import { AuthGard } from './auth-guard.service';
import { AuthenticationService } from './authentication/authentication.service';

export const firebaseConfig = {
  apiKey: masterConfig.apiKey,
  authDomain: masterConfig.authDomain,
  databaseURL: masterConfig.databaseURL,
  storageBucket: masterConfig.storageBucket
};

@NgModule({
  declarations: [
    AppComponent,
    RoverFormComponent,
    PhotosListComponent,
    UserPhotosListComponent,
    PublicComponent,
    PrivateComponent
  ],
  imports: [
    HttpModule,
    BrowserModule,
    routing,
    NgbModule.forRoot(),
    FormsModule,
    AngularFireModule.initializeApp(firebaseConfig),
    AngularFireDatabaseModule,
    AngularFireAuthModule
  ],
  providers: [AuthGard, AuthenticationService],
  bootstrap: [AppComponent]
})
export class AppModule { }
