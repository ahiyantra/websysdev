import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Person } from '../../models/person.model';
import { PersonService } from '../../services/person.service';
import { HttpClientModule } from '@angular/common/http'; // Import HttpClientModule

@Component({
  selector: 'app-person-form',
  templateUrl: './person-form.component.html',
  styleUrls: ['./person-form.component.css'],
  imports: [
    FormsModule,
    CommonModule,
    HttpClientModule // Add HttpClientModule to imports
  ],
  standalone: true
})
export class PersonFormComponent {
  person: Person = new Person();
  persons: Person[] = [];

  constructor(private personService: PersonService) {}

  ngOnInit() {
    this.fetchPersons();
  }

  onSubmit() {
    this.personService.createPerson(this.person).subscribe(() => {
      this.fetchPersons();
      this.person = new Person();
    });
  }

  private fetchPersons() {
    this.personService.getPeople().subscribe((persons) => {
      this.persons = persons;
    });
  }
}