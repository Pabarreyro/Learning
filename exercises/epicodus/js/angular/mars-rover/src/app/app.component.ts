import { Component } from '@angular/core';
import { AuthenticationService } from './authentication.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [AuthenticationService]
})
export class AppComponent {
  title = 'MarsRoverCamLib';
  private isLoggedIn: Boolean;
  private userName: string;
  user;

  constructor(public authService: AuthenticationService, private router: Router){
    this.authService.user.subscribe(user => {
      console.log(user);
      if (user === null) {
        this.isLoggedIn = false;
      } else {
        this.isLoggedIn = true;
        this.userName = user.displayName;
        this.router.navigate([]);
      }
    })
  }

  login() {
    this.authService.login();
  }

  logout() {
    this.authService.logout();
  }
}
