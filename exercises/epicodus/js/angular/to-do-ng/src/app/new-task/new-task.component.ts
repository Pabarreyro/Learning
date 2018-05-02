import { Component, Output, EventEmitter } from '@angular/core';
import { Task } from '../models/task.model';

@Component({
  selector: 'app-new-task',
  templateUrl: './new-task.component.html',
  styleUrls: ['./new-task.component.css']
})
export class NewTaskComponent {
  @Output() sendTask = new EventEmitter();
  newTask: boolean = false;

  addTask() {
    if (this.newTask === false) {
      this.newTask = true;
    } else {
      this.newTask = false;
    }
  }
  submitForm(description: string, priority: string) {
    let newTask: Task = new Task(description, parseInt(priority));
    this.sendTask.emit(newTask);
  }

  constructor() { }

  ngOnInit() {
  }

}
