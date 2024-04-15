import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Person } from '../../models/person.model';
import { PersonService } from '../../services/person.service';
import { HttpClientModule } from '@angular/common/http';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatTableModule } from '@angular/material/table';

@Component({
  selector: 'app-person-form',
  templateUrl: './person-form.component.html',
  styleUrls: ['./person-form.component.css'],
  imports: [
    FormsModule,
    CommonModule,
    HttpClientModule,
    MatInputModule,
    MatButtonModule,
    MatTableModule
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
    }
  );
  }
}