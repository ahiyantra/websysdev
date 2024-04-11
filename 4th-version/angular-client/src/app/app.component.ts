import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { PersonFormComponent } from './components/person-form/person-form.component';
import { HttpClientModule } from '@angular/common/http'; // Import HttpClientModule
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    PersonFormComponent,
    HttpClientModule, // Add HttpClientModule to imports
    RouterModule
  ],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'angular-client';
}