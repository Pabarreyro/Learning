import { Component } from '@angular/core';
import { WelcomeComponent } from './welcome/welcome.component';
import { routing } from './app.routing';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Epicodus Tunes';
}
